from pydantic import BaseModel


class Data(BaseModel):
    name: str


print(Data(name="taro"))
