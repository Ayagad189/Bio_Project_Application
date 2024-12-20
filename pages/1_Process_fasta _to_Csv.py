import streamlit as st
import pandas as pd

def process_happenn(file):
    flag = 0
    tb = []
    for line in file:
        if flag == 0:
            s = line.split("|lcl|")
            flag = 1
        else:
            if s[3] == 'non-hemolytic' or s[3] == 'non-hemolytic\n':
                tb.append([line[:-1], 0])
            else:
                tb.append([line[:-1], 1])
            flag = 0
    
    head = ['Sequence', 'y']
    df = pd.DataFrame(tb, columns=head)
    return df

def process_sequences(file):
    tb = []
    for line in file:
        if line[0] == ">":
            x = line[1:-1]
        else:
            seq = line[:-1]
            tb.append([x, seq])
    
    head = ['ID', 'Sequence']
    df = pd.DataFrame(tb, columns=head)
    return df

st.title("fasta File Parser")

st.write("Choose one of the following options:")

option = st.selectbox("Select an example to process", ["Dataset", "Sequence"])

uploaded_file = st.file_uploader("Choose a fasta file", type="fasta")

if uploaded_file is not None:
    file = uploaded_file.read().decode("utf-8").splitlines()

    if option == "Dataset":
        df = process_happenn(file)
        st.write("Processed Data from Dataset:")
        st.dataframe(df)
        df.to_csv("HAPPENN.csv", index=False)
        st.write("CSV file saved as 'HAPPENN.csv'.")

    elif option == "Sequence":
        df = process_sequences(file)
        st.write("Processed Sequences:")
        st.dataframe(df)
        df.to_csv("seq.csv", index=False)
        st.write("CSV file saved as 'seq.csv'.")
else:
    st.write("Please upload a fasta file to start the analysis.")
