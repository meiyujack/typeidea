from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract=True
    
    # def __init__(self, model_name):
    #     self.cls=model_name
    @classmethod
    def get_all(cls):
        return cls.objects.all()