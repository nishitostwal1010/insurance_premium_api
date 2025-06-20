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
├── app.py                      # FastAPI routes (entrypoint)
├── Dockerfile                  # Docker image setup
├── requirements.txt            # Project dependencies
├── model/
│   ├── model.pkl               # Trained RandomForest model
│   └── predict.py              # Logic to generate predictions
├── schema/
│   ├── user_input.py           # Validates and transforms user input
│   └── prediction_response.py  # Defines API response schema
├── notebooks/
│   └── fastapi_ml_model.ipynb # Notebook for training the model
├── data/
│   └── insurance.csv # Dataset used for training

````

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
