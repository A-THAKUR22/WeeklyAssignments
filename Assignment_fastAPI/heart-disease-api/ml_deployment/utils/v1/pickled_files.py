import pickle 

with open('ml_deployment/datafiles/Classifier_HeartDisease_3.pkl','rb') as f:
    model=pickle.load(f)

with open('ml_deployment/datafiles/scaling(2).pkl','rb') as s:
    scaler=pickle.load(s)