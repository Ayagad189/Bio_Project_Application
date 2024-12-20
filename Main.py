import streamlit as st
st.header("Welcome to Bioinformatics Applications Project 👋")
st.sidebar.success('select Demo above.')
import streamlit as st

# Set the title and introduction for the main page
st.title("Bioinformatics Algorithms for DNA Sequence Analysis")

st.write("""
Welcome to the Bioinformatics Algorithms portal. Here we have implemented various algorithms to process, search, and analyze DNA sequences. Below is a description of the different techniques used, each tailored to different tasks in sequence analysis. Feel free to explore and upload your own data for analysis.

### Algorithms Included:

1. **DNA Sequence Search Using Match Function**
2. **Bad Character Heuristic for Substring Search**
3. **Indexed Query with Suffix Array**
4. **Suffix Array Construction**
5. **DNA Sequence Overlap Calculator**
6. **FASTA to CSV Conversion (HAPPENN Dataset)**

### 1. DNA Sequence Search Using Match Function
This algorithm searches for a subsequence within a given DNA sequence using a straightforward brute-force approach. The function looks for an exact match of the subsequence in the main sequence and returns the starting position of the match, or `-1` if no match is found.

### 2. Bad Character Heuristic for Substring Search
The Bad Character Heuristic is an optimization technique for string matching that improves upon the brute-force approach. It uses a preprocessed table of characters to skip over parts of the sequence, significantly reducing the number of comparisons required. This algorithm is faster than the naive search when there are mismatches.

### 3. Indexed Query with Suffix Array
This algorithm uses a suffix array for efficient substring matching. A suffix array is a sorted array of all suffixes of a string. By indexing all substrings of length `k` and then using binary search, the algorithm can quickly find occurrences of a subsequence in a given DNA sequence.

### 4. Suffix Array Construction
A suffix array is an array of integers representing the starting positions of all suffixes of a string in lexicographical order. This algorithm constructs the suffix array and can be useful in various DNA sequence analysis tasks, such as fast searching and sequence alignment.

### 5. DNA Sequence Overlap Calculator
This algorithm calculates the overlap between pairs of DNA sequences. It finds the longest suffix of one sequence that matches the prefix of another sequence, based on a user-defined minimum overlap length. It’s useful for assembling DNA sequences from smaller fragments or identifying overlaps in metagenomic studies.

### 6. FASTA to CSV Conversion (HAPPENN Dataset)
This algorithm processes FASTA files containing DNA sequences and converts them into a structured CSV format. It reads sequences, along with their associated labels (e.g., `non-hemolytic`), and stores them in a tabular format. This makes the data easier to analyze or use in machine learning tasks.

### How to Use:
1. **DNA Sequence Search**: Upload a FASTA file, input a subsequence, and run the algorithm to find the match.
2. **Bad Character Heuristic**: Similar to the match function but optimized using the Bad Character Heuristic.
3. **Indexed Query**: Generate an index of subsequences and query it for fast matching.
4. **Suffix Array**: Enter a DNA sequence, and the algorithm will generate its suffix array and display it.
5. **Overlap Calculator**: Upload multiple sequences, define the minimum overlap length, and calculate overlaps.
6. **FASTA to CSV**: Upload a FASTA file containing sequences and convert it into a CSV file for easy analysis.

Enjoy exploring these algorithms for DNA sequence analysis!
""")

# You can add more information here, such as links to documentation or references to relevant papers if needed.


