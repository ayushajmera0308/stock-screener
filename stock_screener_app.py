
import streamlit as st
import pandas as pd

# Load pre-saved Excel files
@st.cache_data
def load_data():
    nifty50 = pd.read_excel("Nifty50_Top.xlsx")
    nifty200 = pd.read_excel("Nifty200_Top.xlsx")
    midcap = pd.read_excel("Midcap_Top.xlsx")
    smallcap = pd.read_excel("Smallcap_Top.xlsx")
    return nifty50, nifty200, midcap, smallcap

nifty50_df, nifty200_df, midcap_df, smallcap_df = load_data()

st.title("📊 Fundamental Stock Screener (India)")
st.markdown("Select a category to view the top fundamentally strong companies.")

menu = st.sidebar.selectbox("Choose Category", ("Nifty 50", "Nifty 200", "Midcap", "Smallcap"))

if menu == "Nifty 50":
    st.subheader("🏆 Top Fundamental Companies in Nifty 50")
    st.dataframe(nifty50_df.head(50))
elif menu == "Nifty 200":
    st.subheader("🏆 Top Fundamental Companies in Nifty 200")
    st.dataframe(nifty200_df.head(50))
elif menu == "Midcap":
    st.subheader("📈 Top Fundamental Midcap Companies")
    st.dataframe(midcap_df.head(50))
elif menu == "Smallcap":
    st.subheader("📉 Top Fundamental Smallcap Companies")
    st.dataframe(smallcap_df.head(50))

st.markdown("---")
st.markdown("Created by Ayush's AI Screener 🧠")
