#!/usr/bin/python3


from models.engines.file_stoage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
