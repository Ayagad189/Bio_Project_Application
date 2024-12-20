import streamlit as st
from itertools import permutations

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def native_overlap(reads, k):
    olap = {}
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, k)
        if olen > 0:
            olap[(a, b)] = olen
    return olap

st.title("DNA Sequence Overlap Calculator")
input_reads = st.text_area("Enter DNA sequences (comma_separated):")

k = st.slider("Select minimum overlap length", min_value=1, max_value=5, value=3)

if st.button("Calculate Overlaps"):
    reads = [read.strip() for read in input_reads.split(",")]

    if reads:
        overlaps = native_overlap(reads, k)

        if overlaps:
            st.write("Calculated overlaps between sequences:")
            for (a, b), olen in overlaps.items():
                st.write(f"{a} -> {b}: Overlap length = {olen}")
        else:
            st.write("No overlaps found with the specified minimum length.")
    else:
        st.write("Please enter valid DNA sequences.")
