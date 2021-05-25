from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Keys(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    key = fields.DatetimeField(auto_now_add=True)
    uuid = fields.CharField(max_length=50, null=True)


    class Meta:
        ordering = ["-key"]
   

Keys_Pydantic = pydantic_model_creator(Keys, name="Keys", exclude = ['id'])
