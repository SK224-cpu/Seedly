from pydantic import BaseModel, fields

class LoginUserRequest(BaseModel):
    username:str
    password:str

class LoginUserResponse(BaseModel):
    message:str