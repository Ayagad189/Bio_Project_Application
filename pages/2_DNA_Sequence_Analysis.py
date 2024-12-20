import streamlit as st

def GC_Content(seq):
    l = len(seq)
    num_G = seq.count("G")
    num_C = seq.count("C")
    total = num_C + num_G
    return total / l

def Complement(seq):
    dic = {"G": "C", "C": "G", "A": "T", "T": "A"}
    s = list(seq)
    for i in range(len(seq)):
        s[i] = dic.get(seq[i], "?")  
    s = "".join(s)
    return s

def Reverse(seq):
    return "".join(reversed(seq))

def Reverse_Complement(seq):
    return Complement(Reverse(seq))

def Translation_Table(seq):
    dic = {
        "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
        "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
        "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
        "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
        "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
        "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
        "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
        "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
        "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
        "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
        "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
        "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
        "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
        "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    s = ""
    for i in range(0, len(seq) - 2, 3):
        s += dic.get(seq[i:i + 3], "?") 
    return s

st.title("DNA Sequence Analysis")

st.write("Enter a DNA sequence and choose a function to perform:")

seq = st.text_area("DNA Sequence", height=200)

function = st.selectbox(
    "Select a function to perform",
    ["GC Content", "Reverse Complement", "Complement", "Translation"]
)

if st.button("Submit"):
    if seq:
        if function == "GC Content":
            gc_content = GC_Content(seq)
            st.write(f"GC Content: {gc_content:.2f}")
        elif function == "Reverse Complement":
            reverse_complement = Reverse_Complement(seq)
            st.write(f"Reverse Complement: {reverse_complement}")
        elif function == "Complement":
            complement = Complement(seq)
            st.write(f"Complement: {complement}")
        elif function == "Translation":
            translated_seq = Translation_Table(seq)
            st.write(f"Translated Sequence: {translated_seq}")
    else:
        st.error("Please enter a valid DNA sequence.")
