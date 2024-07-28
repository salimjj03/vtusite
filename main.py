# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool win

from modules.base import Base
from modules.user import User
dic = {
    "full_name": "salim aliyu",
    "user_name": "jj",
    "email": "sali@gmail.com"
}
obj = User(**dic)
print(obj.id)
print(obj.created_at)
print(obj.email)