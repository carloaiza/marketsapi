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
    if 'key' not in data or data['key'] not in data['Document']:
        return Response(response=json.dumps({"Error":
                                                 "Key not configured"}),
                        status=400,
                        mimetype='application/json')
    try:
        response = user_service.save_user(data)
        return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
    except Exception as e:
        return Response(response=json.dumps({"message":str(e)}),
                        status=409,
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

@app_user.route('/user/byfilter',methods=['POST'])
def get_users_by_filter():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error":
                        "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = user_service.get_all_users_by_filter(data['Filter'])
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')