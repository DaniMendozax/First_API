#Python
import json
from datetime import date, datetime
from unittest import result
from uuid import UUID
from typing import Optional, List, Dict



#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

#FastApi
from fastapi import FastAPI, status, Body
from fastapi.encoders import jsonable_encoder

app =  FastAPI()

#Models

class UserBase(BaseModel):
    userId: UUID = Field(...)
    email: EmailStr = Field(...)


class User(UserBase):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name:str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8
    )

class UserRegister(UserLogin, User):
    pass

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
 
#Path Operations

## Users

### Register an User
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register an user",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup

    This path operation register an user in the app

    Parameters:
        - Request body parameter
            - user: UserRegistrer

    Returns a json with the basic user information
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    json_complatible = jsonable_encoder(user)
    with open("users.json", "r+", encoding="utf-8") as file:
        results = json.load(file)
        results.append(json_complatible)
        file.seek(0)
        json.dump(results, file)
        return user

### Login an user 

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login an user",
    tags=["Users"]
)
def login():
    pass

### Show all users

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all user",
    tags=["Users"]
)
def Show_all_users():
    """
    This path operation show all users in the app

    Parameters:
        -

    Returns a json list with all users in the app, with the following keys
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r") as f:
        results = json.load(f)
        return results

### Show all users

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Register an user",
    tags=["Users"]
)
def Show_a_user():
    pass

### Deleted an users

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Deleted an user",
    tags=["Users"]
)
def deleted_a_user():
    pass

### Update an users

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update an user",
    tags=["Users"]
)
def update_a_user():
    pass

#Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all user",
    tags=["Tweets"]

)
def home():
    return {"twiter API:" "Working!"} 

### Post an Tweets
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"]
)
def past():
    pass

### Show a tweet
@app.get(
    path="/tweets/{teet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Deleted a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass