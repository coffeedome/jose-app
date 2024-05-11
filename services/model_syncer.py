import boto3

class ModelSyncerService():
    def __init__(self, models:list[str]) -> None:
        self._models = models
    
    def get_model_info(self):
        return self._models
    
    def sync_model(self, model_name):
        if model_name in self._models:
            client = boto3.client("s3")
            
        