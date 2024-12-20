import streamlit as st
import numpy as np
import bisect

def IndexSorted(seq, ln):
    index = []
    for i in range(len(seq) - ln + 1):
        index.append((seq[i:i + ln], i))
    index.sort()
    return index

def query(t, p, index):
    keys = [r[0] for r in index]
    start = bisect.bisect_left(keys, p[:len(keys[0])])
    end = bisect.bisect(keys, p[:len(keys[0])])
    hits = index[start:end]
    l = [h[1] for h in hits]
    offsets = []
    for i in l:
        if t[i:i + len(p)] == p:
            offsets.append(i)
    return offsets

st.title("DNA Sequence Search with Indexed Query")

st.write("Upload a DNA file (fasta format) and input a subsequence to search for.")

uploaded_file = st.file_uploader("Choose a fasta file", type='fasta')

if uploaded_file is not None:
    try:
        file_content = uploaded_file.read().decode("utf-8")
        lines = file_content.splitlines()
        if len(lines) < 2:
            st.error("Invalid fasta file format. Ensure it contains a header and sequence.")
        else:
            sequence = "".join(lines[1:]).replace("\n", "").upper()  

            if not set(sequence).issubset({"A", "C", "G", "T"}):
                st.error("The DNA sequence contains invalid characters. Only A, C, G, and T are allowed.")
            else:
                st.write(f"DNA Sequence:\n{sequence[:200]}...")  
                subsequence = st.text_input("Enter the subsequence to search for:")

                if subsequence:
                    subsequence = subsequence.upper()  
                    if not set(subsequence).issubset({"A", "C", "G", "T"}):
                        st.error("Invalid subsequence. Please use only A, C, G, and T.")
                    else:
                        index_length = st.number_input(
                            "Enter the index length for subsequences (default is 3):",
                            min_value=1,
                            max_value=len(sequence),
                            value=3,
                        )
                        index = IndexSorted(sequence, index_length)

                        result = query(sequence, subsequence, index)

                        if result:
                            st.write(f"Subsequence '{subsequence}' found at positions: {result}")
                        else:
                            st.write(f"Subsequence '{subsequence}' not found.")
                else:
                    st.write("Please enter a subsequence to search for.")
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")
else:
    st.write("Please upload a fasta file to start the analysis.")
