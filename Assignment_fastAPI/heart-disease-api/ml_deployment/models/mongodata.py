import mongoengine

class HeartDiseasePrediction(mongoengine.Document):
    age=mongoengine.IntField(required=True)
    sex=mongoengine.IntField(required=True)
    cp=mongoengine.IntField(required=True)
    trtbps=mongoengine.IntField(required=True)
    chol=mongoengine.IntField(required=True)
    fbs=mongoengine.IntField(required=True)
    restecg=mongoengine.IntField(required=True)
    thalachh=mongoengine.IntField(required=True)
    exng=mongoengine.IntField(required=True)
    oldpeak=mongoengine.FloatField(required=True)
    slp=mongoengine.IntField(required=True)
    caa=mongoengine.IntField(required=True)
    thall=mongoengine.IntField(required=True)
    output=mongoengine.StringField()

    metadata={
      'collection':"Predictions"
    }