import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Data Explorer", layout="wide")

st.title("📊 Universal CSV Data Explorer")

# --- Upload or Load CSV ---
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

@st.cache_data
def load_default_data():
    return pd.read_csv("data/cleaned_customer_reviews.csv")


@st.cache_data
def load_uploaded_data(uploaded_file):
    return pd.read_csv(uploaded_file)

# --- Load Data ---
if uploaded_file:
    df = load_uploaded_data(uploaded_file)
else:
    df = load_default_data()

st.success(f"Loaded {len(df)} rows and {len(df.columns)} columns.")

# --- Display All Columns ---
st.markdown("### 🔍 Choose Filters to Apply")

# Create column-specific filters
filtered_df = df.copy()
columns = df.columns.tolist()

for col in columns:
    col_data = df[col]
    with st.expander(f"🔧 Filter: {col}"):
        if pd.api.types.is_numeric_dtype(col_data):
            min_val, max_val = float(col_data.min()), float(col_data.max())
            selected_range = st.slider(f"Select range for {col}", min_val, max_val, (min_val, max_val))
            filtered_df = filtered_df[(filtered_df[col] >= selected_range[0]) & (filtered_df[col] <= selected_range[1])]
        elif pd.api.types.is_string_dtype(col_data) or pd.api.types.is_object_dtype(col_data):
            unique_values = col_data.dropna().unique()
            if len(unique_values) <= 100:
                selected_values = st.multiselect(f"Select values for {col}", options=unique_values)
                if selected_values:
                    filtered_df = filtered_df[filtered_df[col].isin(selected_values)]
            keyword = st.text_input(f"Search in {col} (optional)", key=col)
            if keyword:
                filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(keyword, case=False, na=False)]
        else:
            st.info("Column type not supported for filtering.")

# --- Show Result ---
st.markdown("## 📄 Filtered Data")
st.write(f"Total results: {len(filtered_df)}")
st.dataframe(filtered_df, use_container_width=True)

# --- Download Filtered Result ---
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

if not filtered_df.empty:
    csv = convert_df(filtered_df)
    st.download_button("⬇️ Download Filtered CSV", csv, "filtered_data.csv", "text/csv")
else:
    st.warning("No data to download!")
