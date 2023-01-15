from pydantic import BaseModel


class BaseOperation(BaseModel):
    file_name: str
    content: str
    
    
class GetData(BaseOperation):
    pass


class PutData(BaseOperation):
    pass
    