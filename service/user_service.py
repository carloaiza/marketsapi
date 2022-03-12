from config.mongo_db import MongoApi

class UserService:
    def get_all_users(self):
        connection = MongoApi({"database":"arepitas_ricas",
                         "collection":"users"})
        response = connection.read()
        return response

