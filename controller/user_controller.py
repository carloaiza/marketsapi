from flask import Response,Blueprint, json
from service.user_service import UserService

app_user = Blueprint('app_user',__name__)
user_service = UserService()

@app_user.route('/user', methods=['GET'])
def get_all_users():  # put application's code here
    return Response(response=json.dumps(user_service.get_all_users()),status=200,
                    mimetype='application/json')
