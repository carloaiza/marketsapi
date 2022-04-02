from.generic_service import GenericService

class UserService(GenericService):
    def __init__(self):
        super().__init__("arepitas_ricas","markets","user")
