# this is an actions package for user related actions
# to define packages create an __init__.py file
# it can be empty or contain package initialization code
from ..gestion.crud import save

def pay_taxes():
    print("User taxes paid")
    save()
