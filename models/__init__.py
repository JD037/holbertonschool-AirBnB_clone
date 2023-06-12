from models.engines.file_stoage import FileStorage

storage = FileStorage()
storage.reload()

def save(self):
    """ Update the instance's updated_at attribute """
    self.updated_at = datetim.now()