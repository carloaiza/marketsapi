from config.mongo_db import MongoApi

class UserService:
    data = {"database":"arepitas_ricas",
                         "collection":"users"}

    def get_all_users(self):
        connection = MongoApi(self.data)
        response = connection.read()
        return response

    def save_user(self,data):
        connection = MongoApi(self.data)
        response = connection.write(data)
        return response

    def update_user(self, data):
        self.data['Filter']=data['Filter']
        self.data['DataToBeUpdated'] = data['DataToBeUpdated']
        connection = MongoApi(self.data)
        response = connection.update()
        return response

    def delete_user(self, data):
        connection = MongoApi(self.data)
        response = connection.delete(data)
        return response