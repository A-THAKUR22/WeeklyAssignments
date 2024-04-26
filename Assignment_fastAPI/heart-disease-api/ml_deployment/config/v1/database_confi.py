from ml_deployment.config.v1 import BaseSettingWrapper

class MongoConfig(BaseSettingWrapper):
    mongo_host: str="localhost"

mongo_config=MongoConfig()