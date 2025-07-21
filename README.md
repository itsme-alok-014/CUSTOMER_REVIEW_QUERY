# CUSTOMER_REVIEW_QUERY
iew Data Explorer

A simple and interactive Streamlit web application to **explore, filter, and download** customer review datasets (CSV format).  
Built using Python, pandas, and Streamlit.

---

## 🚀 [🟢 CLICK HERE TO OPEN THE LIVE APP](https://itsme-alok-014-customer-review-query.streamlit.app)

<h2 align="center" style="color:#00c851">
  🔗 <a href="https://itsme-alok-014-customer-review-query-streamlit-app-htzwzo.streamlit.app/" target="_blank">CLICK HERE TO OPEN THE APP</a>
</h2>

---

## 🗂️ Project Structure

```

customer\_review\_query/
├── File\_Cleaning.ipynb              # Jupyter notebook for data cleaning
├── cleaned\_customer\_reviews.csv     # Final cleaned data
├── streamlit\_app.py                 # Main Streamlit frontend
├── requirements.txt                 # Project dependencies
└── README.md                        # This file

````

---

## 🔧 Features

- Upload your own `.csv` file or use default data
- Automatic loading of `cleaned_customer_reviews.csv`
- Filter by any column:
  - 🔢 Numerical: slider range
  - 🏷️ Categorical: multiselect options
  - 🔍 Text columns: search by keyword
- View filtered data in real time
- 📥 Download filtered data as CSV

---

## 🧼 Data Cleaning Process

Performed in `File_Cleaning.ipynb` using pandas:

- Removed duplicate rows
- Handled missing/null values
- Standardized text (lowercasing, trimming, etc.)
- Saved cleaned version as `cleaned_customer_reviews.csv`

---

## 🖥️ How to Use the App

1. Open the [Streamlit app](https://itsme-alok-014-customer-review-query.streamlit.app)
2. Upload a `.csv` file or use the built-in default data
3. Apply filters using sliders, multiselects, or search boxes
4. View the live filtered table
5. Click **⬇️ Download Filtered CSV** to save your custom dataset

---

## 🛠️ Run Locally (Optional)

```bash
# Clone the repository
git clone https://github.com/itsme-alok-014/customer_review_query.git
cd customer_review_query

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
````

---

## 🧰 Tech Stack

* Python 🐍
* pandas 📊
* Streamlit ⚡
* Jupyter Notebook 📓

---

## 🙋‍♂️ Author

**Alok Dubey**
[GitHub: @itsme-alok-014](https://github.com/itsme-alok-014)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

````

---

### ✅ Optional: Push to GitHub

```bash
git add README.md
git commit -m "Added stylish README with bold app link"
git push
````

---

Would you like me to:

* Generate a visual banner?
* Add shields (Streamlit, Python, License badges)?
  Just say the word — I’ll add it instantly.
