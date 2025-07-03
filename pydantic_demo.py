from pydantic import BaseModel,EmailStr,Field
from typing import Optional
#Pydantic allows data validation
class Student(BaseModel):
    name : str = "Speed"
    age : Optional[int] = None
    # email : EmailStr
    cgpa : float = Field(gt=0,lt=10)

new_student = {'age':'50','cgpa':1} #Pydantic does type coersion

student = Student(**new_student)

student_dict = dict(student) #converting a pydantic object to normal  disctionary

print(student_dict['name'])
#print(student)