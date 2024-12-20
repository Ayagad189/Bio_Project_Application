import streamlit as st

def generate_suffix_array(T):
    dec = {
        '$': 0,
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }

    T = T + '$'  
    table = []  
    i = 2 ** 0  
    n = 0  
    suffix_arrays = []  
    while True:
        l = []  
        dec2 = {}  

        if i > 1:
            for j in range(len(T)):
                if table[n-1][j:j+i] not in l:
                    l.append(table[n-1][j:j+i])
            l.sort()

            for j in range(len(l)):
                dec2[tuple(l[j])] = j

        row = []
        for j in range(len(T)):
            if i == 1:
                row.append(dec[T[j]]) 
            else:
                row.append(dec2[tuple(table[n-1][j:j+i])])

        table.append(row)

        flag = 0
        for j in range(len(row)):
            if row.count(j) > 1:
                flag = 1
                break

        suffix_arrays.append(row)  
        if flag == 0:
            break
        n += 1
        i = 2 ** n  

    return suffix_arrays

st.title("Suffix Array Generator")

st.write("Enter a DNA sequence and view how the suffix array.")

input_string = st.text_input("Enter a DNA sequence:")

if input_string:
    suffix_arrays = generate_suffix_array(input_string)

    st.write("Suffix Array at each iteration:")
    for idx, arr in enumerate(suffix_arrays):
        st.write(f"Iteration {idx + 1}: {arr}")
else:
    st.write("Please enter a DNA sequence to generate the suffix array.")
