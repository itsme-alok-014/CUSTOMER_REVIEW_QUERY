
# 🛒 Customer Review Insights

This project explores key insights from customer review data using Python and Streamlit.

---

## ❓ Key Questions & Answers

### 1. **Which product categories have the most 1-star reviews in Canada?**

| Product Category | 1-Star Reviews |
|------------------|----------------|
| Prom Dresses     | 2              |
| Unknown          | 2              |

📌 *Note: Limited data from Canada may affect representation.*

---

### 2. **Do higher order values correlate with lower ratings?**

📉 **Correlation coefficient between Order Value and Rating**: `-0.0095`

➡️ This shows **almost no correlation** between order value and customer rating.

---

### 3. **What are the top 5 complaints and top 5 compliments in reviews?**

Based on most frequent keywords in review content:

#### 😠 Top 5 Complaint Keywords (1-star reviews):
team, those, hard, international, second

#### 😊 Top 5 Compliment Keywords (5-star reviews):
author, social, threat, office, financial

📌 *These keywords are based on word frequency and may represent themes or repeated issues/praise.*

---

### 4. **Which fulfillment statuses are most associated with negative feedback?**

| Fulfillment Status | # of Low Ratings (1–2 stars) |
|---------------------|-----------------------------|
| Unknown             | 10                          |
| Fulfilled           | 8                           |
| Returned            | 7                           |
| Delayedd            | 6                           |
| Cancelled           | 4                           |
| Delayeddd           | 3                           |

➡️ **"Unknown" and "Fulfilled"** status show the highest number of negative reviews.

---

## 🔗 Live Project

👉 <a href="https://itsme-alok-014-customer-review-query-streamlit-app-htzwzo.streamlit.app/" style="font-size: 20px; font-weight: bold;">🚀 Open the Customer Review Dashboard</a>

---

## 📁 Repository Structure

```bash
├── cleaned_customer_reviews.csv   # Pre-processed dataset
├── app.py                         # Streamlit dashboard
├── analysis_notebook.ipynb        # Jupyter notebook used for insights
├── README.md                      # Project overview and Q&A summary
```
