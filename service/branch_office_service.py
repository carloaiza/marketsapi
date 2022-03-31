from config.mongo_db import MongoApi
from .generic_service import GenericService

class BranchOfficeService(GenericService):
    def __init__(self):
        super().__init__("arepitas_ricas","markets","branch_office")

