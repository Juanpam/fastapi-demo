from fastapi import FastAPI
from pydantic import BaseModel

# Creating basic model for holding people data
class Person(BaseModel):
    name: str
    description: str

# Creates web server application
app = FastAPI()

# In-memory database
people: dict[str, Person] = {}

# Adds health endpoint to check server is running
@app.get("/health")
def health():
    return "Hello world"

# Basic endpoint for listing people in database
@app.get("/people")
def list_people():
    return people

# Endpoint for adding people to the database
@app.post("/people")
def add_person(newPerson: Person):
    people[newPerson.name] = newPerson
    return newPerson

# Endpoint for getting a specific person by name
@app.get("/people/{person_name}")
def read_item(person_name: str):
    print(person_name, people)
    return people.get(person_name, 'No person found with that name')

# Endpoint for removing a person from the database
@app.delete("/people/{person_name}")
def read_item(person_name: str):
    del people[person_name]