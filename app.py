import streamlit as st
import pickle
import pandas as pd

# ----------------------------------
# Page setup
# ----------------------------------
st.set_page_config(page_title="Cafe Sales Prediction App")
st.title("☕ Cafe Sales Prediction")

# ----------------------------------
# Load model safely
# ----------------------------------
@st.cache_resource
def load_model():
    with open("cafe_sales.pkl", "rb") as f:
        return pickle.load(f)

try:
    model = load_model()
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error("❌ Failed to load model")
    st.exception(e)
    st.stop()

# ----------------------------------
# CSV Upload (CORRECT APPROACH)
# ----------------------------------
st.write("### Upload Input CSV File")
st.info(
    "The CSV file must have the **same columns and order** as the training data."
)

uploaded_file = st.file_uploader(
    "Upload CSV file", type=["csv"]
)

if uploaded_file is not None:
    try:
        input_df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data Preview")
        st.dataframe(input_df)

        if st.button("Predict"):
            predictions = model.predict(input_df)

            result_df = input_df.copy()
            result_df["Prediction"] = predictions

            st.success("✅ Prediction completed")
            st.dataframe(result_df)

            # Download results
            csv = result_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇️ Download Predictions",
                csv,
                "predictions.csv",
                "text/csv"
            )

    except Exception as e:
        st.error("❌ Prediction failed")
        st.exception(e)
