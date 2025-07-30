import streamlit as st
import math

# Page setup
st.set_page_config(page_title="Cipher Tool", layout="centered")

# Light-themed and styled output
st.markdown("""
    <style>
        .stApp {
            background-color: #f9f9f9;
        }
        .title {
            font-size: 36px;
            text-align: center;
            color: #003366;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 20px;
            color: #333;
            margin-top: 30px;
            font-weight: bold;
        }
        .output-box {
            background-color: #ffffff;
            border: 2px solid #336699;
            padding: 20px;
            font-size: 16px;
            font-family: monospace;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
        textarea {
            font-size: 16px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Transposition Techniques</div>', unsafe_allow_html=True)

# Input for plain text
st.markdown('<div class="subtitle">Enter Plaintext</div>', unsafe_allow_html=True)
plain_text = st.text_area("Plaintext", placeholder="e.g., meet at the school house", key="plain", label_visibility="collapsed")

# Method selection
method = st.selectbox("Choose Cipher Method", ["Row Transposition", "Rail Fence"])

# Row Transposition: needs numeric key
if method == "Row Transposition":
    st.markdown('<div class="subtitle">Enter Numeric Key</div>', unsafe_allow_html=True)
    key_input = st.text_input(label="", placeholder="e.g., 4312567", key="key", label_visibility="collapsed")

# Encrypt/Decrypt button
if st.button("Encrypt and Decrypt"):
    if not plain_text.strip():
        st.warning("Please enter some plaintext.")
    else:
        cleaned_text = plain_text.replace(" ", "").lower()

        # ----- ROW TRANSPOSITION -----
        if method == "Row Transposition":
            if not key_input or not key_input.isdigit():
                st.error("Please enter a valid numeric key (digits only).")
            else:
                key_digits = [int(k) for k in key_input]
                len_key = len(key_digits)
                len_text = len(cleaned_text)
                row = int(math.ceil(len_text / len_key))

                # Fill matrix row-wise
                matrix = [['X'] * len_key for _ in range(row)]
                t = 0
                for r in range(row):
                    for c in range(len_key):
                        if t < len_text:
                            matrix[r][c] = cleaned_text[t]
                            t += 1

                # Encrypt: read columns in key order
                col_order = [key_digits.index(i + 1) for i in range(len_key)]
                cipher_text = ''
                for c in col_order:
                    for r in range(row):
                        cipher_text += matrix[r][c]

                # Decrypt: fill columns back
                matrix_new = [['X'] * len_key for _ in range(row)]
                t = 0
                for c in col_order:
                    for r in range(row):
                        if t < len(cipher_text):
                            matrix_new[r][c] = cipher_text[t]
                            t += 1

                decrypted_text = ''
                for r in range(row):
                    for c in range(len_key):
                        if matrix_new[r][c] != 'X':
                            decrypted_text += matrix_new[r][c]

                # Output
                st.markdown('<div class="subtitle">Row Transposition Cipher Output</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box"><b>Cipher Text:</b><br>{cipher_text}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box"><b>Decrypted Text:</b><br>{decrypted_text}</div>', unsafe_allow_html=True)

        # ----- RAIL FENCE (2-Rail) -----
        elif method == "Rail Fence":
            # Encryption
            row1, row2 = [], []
            for i, ch in enumerate(cleaned_text):
                (row1 if i % 2 == 0 else row2).append(ch)

            cipher = ''.join(row1 + row2)

            # Decryption
            mid = (len(cleaned_text) + 1) // 2
            row1 = list(cipher[:mid])
            row2 = list(cipher[mid:])

            decrypted = ''
            for i in range(len(cleaned_text)):
                if i % 2 == 0:
                    decrypted += row1.pop(0)
                else:
                    decrypted += row2.pop(0)

            # Output
            st.markdown('<div class="subtitle">Rail Fence Cipher Output</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="output-box"><b>Cipher Text:</b><br>{cipher}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="output-box"><b>Decrypted Text:</b><br>{decrypted}</div>', unsafe_allow_html=True)
