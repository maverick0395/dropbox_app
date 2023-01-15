import dropbox
from fastapi import HTTPException, status


from ..models import GetData, PutData
from ..settings import settings


class DropboxService:
    def __init__(self):
        print(settings.access_token)
        self.dbx = dropbox.Dropbox(settings.access_token)


    def get(
        self, 
        file_name: str
    ) -> GetData:
        try:
            data = {}
            data["file_name"] = file_name
            _, res = self.dbx.files_download(f"/{file_name}")
            data["content"] = res.content
            print(data)
            if not data["content"]:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            return data
            
        except Exception as e:
            print(e)
            return e
    
    def put(
        self,
        file_name: str,
        content: str
    ) -> PutData:
        try:
            data = {}
            data["file_name"] = file_name
            data["content"] = content
            self.dbx.files_upload(self.binarize(content), f'/{file_name}', mode=dropbox.files.WriteMode.overwrite)
            print(data)
            return data
            
        except Exception as e:
            print(e)
            return e
        
    def binarize(
        self,
        content: str
    ) -> str:
        return content.encode('ascii')
        
