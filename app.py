import streamlit as st
import pandas as pd

st.title("AI Candidate Ranking Engine")
jd = st.text_area("Enter Job Description")
file = st.file_uploader("Upload Candidate CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.write("Candidate Data")
    st.dataframe(df)
    if jd:
        df["score"] = df["skills"].apply(lambda x: len(set(str(x).split()) & set(jd.split())))
        df = df.sort_values(by="score", ascending=False)
        st.write("Ranked Candidates")
        st.dataframe(df)
      st.write(f"Total Candidates: {len(df)}")
st.success("Top Candidate: " + df.iloc[0]['name'])
