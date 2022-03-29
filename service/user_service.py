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
        key = data['key']
        validation = connection.read_by_filter({key:data['Document'][key]})
        if(len(validation)>0):
            raise Exception("Ya existe un usuario con los datos suministrados")
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

    def get_all_users_by_filter(self,filter):
        connection = MongoApi(self.data)
        response = connection.read_by_filter(filter)
        return response

