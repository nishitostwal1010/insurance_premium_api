from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictedResponse
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

# Human readable - Humans know that API is working
@app.get('/')
def home():
    return {'message': 'Insurance Premium Prediction API'}

# Machine Readable - Used so that machine know our API is working (Used in cloud)
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None # To know if model is loaded or not
    }

@app.post('/predict', response_model=PredictedResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation 
    }

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content=prediction)

    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))
