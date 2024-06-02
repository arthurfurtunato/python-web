from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# users
# departament
# account

class ListOption(str, Enum):
  users = "users"
  department = "department"
  account = "account"

@app.get("/{list_option}/list")
async def generic_list(list_option: ListOption):
  if list_option == ListOption.users:
    data = ["user1", "user2", "user3"]
  elif list_option == ListOption.department:
    data = ["department", "department", "department"]
  elif list_option == ListOption.account:
    data = [1234, 8989, 33333]
  
  return {"accounts": data}

@app.get("/user/{username}")
async def user_profile(username: str):
  return {"data": username}

@app.get("/account/{number}")
async def account_detail(number: int):
  return {"account": number}

@app.get("/import/{filepath:path}")
async def import_file(filepath: str):
  return {"importing": filepath}