import strawberry_django
from strawberry import auto

from . import models

@strawberry_django.type(models.Companies)
class Company:
    id: auto
    name: auto
    address: auto
    

class