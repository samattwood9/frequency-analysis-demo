import streamlit as st
import string
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Frequency analysis', page_icon='📊')

st.title("📊 Frequency analysis")

user_text = st.text_area(
    "Enter text:",
    "Write here and observe how the frequency of characters changes!"
)

user_text = user_text.lower().replace(" ", "")

user_text = [l for l in user_text if l not in string.punctuation]

letter_counts = Counter(user_text)

freq_data = []
for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    freq_data.append([letter, letter_counts[letter], 'Plain text'])

df = pd.DataFrame(freq_data, columns=['letter', 'count', 'Key'])
    
fig1 = plt.figure()
sns.barplot(df, x='letter', y='count', hue='Key')

st.pyplot(fig1)

st.write('## Breaking the Caesar Cipher')

cipher_text = st.text_area(
    "Enter an encrypted text here (why not use: https://ciphereditor.com/explore/caesar-cipher):",
    "Zulwh khuh dqg revhuyh krz wkh iuhtxhqfb ri fkdudfwhuv fkdqjhv!"
)

cipher_text  = cipher_text .lower().replace(" ", "")

cipher_text  = [l for l in cipher_text  if l not in string.punctuation]

letter_counts = Counter(cipher_text )

for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    freq_data.append([letter, letter_counts[letter], 'Cipher text'])

df_combined = pd.DataFrame(freq_data, columns=['letter', 'count', 'Key'])
    
fig2 = plt.figure()
sns.barplot(df_combined, x='letter', y='count', hue='Key')

st.pyplot(fig2)
    

