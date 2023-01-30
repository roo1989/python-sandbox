from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Joe Doe'
    signup_ts = '2023-01-02 12:12'
    friends: list[int] = []

external_data = {
    'id': 10,
    'name': 'Ragnar',
    'signup_ts': '2023-01-02 13:08',
    'friends': [ 1, 2, 3, 4 ]
}

user = User(**external_data)
