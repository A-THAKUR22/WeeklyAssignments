import mongoengine
from fastapi import FastAPI
from ml_deployment.utils.v1.preprocessing import helper_func
from ml_deployment.utils.v1.pickled_files import model, scaler
from ml_deployment.models.mongodata import HeartDiseasePrediction
from ml_deployment.models.pydantic_model import HeartDiseaseFeatures
from ml_deployment.config.v1.database_confi import mongo_config

mongoengine.connect(db='HeartDiseasePrediction',host=mongo_config.mongo_host)
app=FastAPI()

@app.post('/predictions/')
async def disease_pred(features: HeartDiseaseFeatures):
    
    scaled=helper_func([
        features.age,
        features.sex,
        features.cp,
        features.trtbps,
        features.chol,
        features.fbs,
        features.restecg,
        features.thalachh,
        features.exng,
        features.oldpeak,
        features.slp,
        features.caa,
        features.thall],scaler)
    
    prediction=model.predict(scaled)
    prediction=int(prediction[0])

    if prediction==1:
        diagnosis='High'

    else:
        diagnosis='Low'

    predictions_made=HeartDiseasePrediction(
        age=features.age,
        sex=features.sex,
        cp=features.cp,
        trtbps=features.trtbps,
        chol=features.chol,
        fbs=features.fbs,
        restecg=features.restecg,
        thalachh=features.thalachh,
        exng=features.exng,
        oldpeak=features.oldpeak,
        slp=features.slp,
        caa=features.caa,
        thall=features.thall,
        output=diagnosis)
    predictions_made.save()
 
    return {'output': diagnosis}

@app.get("/health")
async def health():
    return {"status": "ok"}