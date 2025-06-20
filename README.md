# 🛡️ Insurance Premium Prediction API

This is a machine learning-powered REST API built with **FastAPI** that predicts the insurance premium category (`Low`, `Medium`, or `High`) based on user attributes such as age, weight, height, income, lifestyle, and city.

🛠️ This project was developed as part of the learning journey to understand and implement containerization using Docker.

---

## 📌 Features

- 🚀 FastAPI-based backend for high performance
- ✅ Input validation using Pydantic models
- 📊 Auto-computed features: BMI, lifestyle risk, city tier, and age group
- 🔍 Model confidence and class probability scores returned
- 🐳 Docker support for containerized deployment
- 📓 Jupyter notebook and dataset available for training

---

## 📁 Project Structure

```

insurance_premium_api/
├── app.py                      # Main FastAPI app with API routes
├── Dockerfile                  # Docker image configuration to containerize the app
├── requirements.txt            # Python dependencies for the project
│
├── model/
│   ├── model.pkl               # Trained machine learning model (Random Forest)
│   └── predict.py              # Prediction logic using the trained model
│
├── schema/
│   ├── user_input.py           # Pydantic model for validating and transforming incoming user data
│   └── prediction_response.py  # Pydantic model for formatting prediction response
│
├── config/
│   └── city_tier.py            # Lists of Tier 1 and Tier 2 cities used to compute city_tier
│
├── notebooks/
│   └── fastapi_ml_model.ipynb  # Jupyter notebook for training and exporting the ML model
│
├── data/
│   └── insurance.csv           # Dataset used for training the model (optional for reproducibility)


```

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.9+
- `pip` package manager

### ⚙️ Installation

```bash
git clone https://github.com/nishitostwal1010/insurance_premium_api.git
cd insurance_premium_api
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
````

### ▶️ Run the API Locally

```bash
uvicorn app:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 🔗 API Endpoints

| Method | Endpoint   | Description                        |
| ------ | ---------- | ---------------------------------- |
| GET    | `/`        | Root endpoint                      |
| GET    | `/health`  | Health and model status check      |
| POST   | `/predict` | Predict insurance premium category |

---

## 🧪 Example Input (POST /predict)

```json
{
  "age": 35,
  "weight": 78,
  "height": 1.76,
  "income_lpa": 12,
  "smoker": false,
  "city": "Pune",
  "occupation": "private_job"
}
```

### ✅ Sample Response

```json
{
  "predicted_category": "Medium",
  "confidence": 0.82,
  "class_probabilities": {
    "Low": 0.05,
    "Medium": 0.82,
    "High": 0.13
  }
}
```

---

## 📓 Model Training

You can retrain the model using the Jupyter notebook provided in:

```
notebooks/fastapi_ml_model.ipynb
```

* Features: BMI, lifestyle risk, income, age group, city tier, etc.
* Model: Random Forest Classifier
* Output: `model/model.pkl`

---

## 📊 Dataset

The dataset is located at:

```
data/insurance.csv
```

## 🧠 Tech Stack

* **FastAPI**
* **Pydantic**
* **Scikit-learn**
* **Docker**
* **Uvicorn**

---

## 📦 Docker Image

Public Docker image available at:

🔗 [`nishitostwal123/insurance_premium_api`](https://hub.docker.com/r/nishitostwal123/insurance_premium_api)

The Docker image is meant for **serving the prediction API only**.  
Training notebooks and datasets are excluded.

---

## 🙋‍♂️ Author

**Nishit Ostwal**
📬 [GitHub Profile](https://github.com/nishitostwal1010)
