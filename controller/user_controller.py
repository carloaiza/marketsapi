from flask import Response,Blueprint, json, request
from service.user_service import UserService

app_user = Blueprint('app_user',__name__)
user_service = UserService()

@app_user.route('/user', methods=['GET'])
def get_all_users():  # put application's code here
    return Response(response=json.dumps(user_service.get_all_users()),status=200,
                    mimetype='application/json')

@app_user.route('/user',methods=['POST'])
def save_user():
    data = request.json
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error":
                        "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = user_service.save_user(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app_user.route('/user', methods=['PUT'])
def update_user():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = user_service.update_user(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app_user.route('/user', methods=['DELETE'])
def delete_user():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = user_service.delete_user(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')