import streamlit as st
import numpy as np

def match(seq, sub_seq):
    for i in range(len(seq) - len(sub_seq) + 1):
        if sub_seq == seq[i:i + len(sub_seq)]:
            return i  
    return -1  

def Badchars(seq, sub_seq):
    table = np.zeros((4, len(sub_seq)), dtype=int)
    row = ["A", "C", "G", "T"]
    for i in range(4):
        last_seen = -1
        for j in range(len(sub_seq)):
            if row[i] == sub_seq[j]:
                last_seen = -1
            else:
                last_seen += 1
            table[i, j] = last_seen

    i = 0
    while i <= len(seq) - len(sub_seq):
        mismatch_found = False
        for j in range(len(sub_seq) - 1, -1, -1):
            if seq[i + j] != sub_seq[j]:
                mismatch_found = True
                bad_char = seq[i + j]
                if bad_char in row:
                    k = row.index(bad_char)
                    i += table[k, j]
                else:
                    i += len(sub_seq)  
                break
        if not mismatch_found:
            return i  
        i += 1
    return -1  

st.title("DNA Sequence Search")

st.write("Upload a DNA file (fasta format) and input a subsequence to search for.")

uploaded_file = st.file_uploader("Choose a fasta file", type="fasta")

if uploaded_file is not None:
    try:
        file_content = uploaded_file.read().decode("utf-8")

        lines = file_content.splitlines()
        sequence = "".join(lines[1:]).replace("\n", "").upper()  
        st.write(f"DNA Sequence:\n{sequence}")
        subsequence = st.text_input("Enter the subsequence to search for:")

        if subsequence:
            subsequence = subsequence.upper()  

            if not set(subsequence).issubset({"A", "C", "G", "T"}):
                st.error("Invalid subsequence. Please use only A, C, G, and T.")
            else:
                match_result = match(sequence, subsequence)
                st.write(f"Match result (using match function): {match_result if match_result != -1 else 'Not found'}")

                badchars_result = Badchars(sequence, subsequence)
                st.write(f"Match result (using Bad Character Heuristic): {badchars_result if badchars_result != -1 else 'Not found'}")
        else:
            st.write("Please enter a subsequence to search for.")
    except Exception as e:
        st.error("An error occurred while processing the file. Please ensure it is in valid fasta format.")
else:
    st.write("Please upload a fasta file to start the analysis.")
