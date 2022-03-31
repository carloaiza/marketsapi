from flask import Response,json,Blueprint,request
from service.branch_office_service import BranchOfficeService

app_branch = Blueprint('app_branch',__name__)
branch_office_service = BranchOfficeService()

@app_branch.route('/branchoffice', methods=['GET'])
def get_all_users():  # put application's code here
    return Response(response=json.dumps(branch_office_service.get_all()),status=200,
                    mimetype='application/json')

@app_branch.route('/branchoffice',methods=['POST'])
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
        response = branch_office_service.save(data,"Ya existe una sucursal para los datos suministrados")
        return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
    except Exception as e:
        return Response(response=json.dumps({"message":str(e)}),
                        status=409,
                        mimetype='application/json')

@app_branch.route('/branchoffice', methods=['PUT'])
def update_user():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = branch_office_service.update(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app_branch.route('/branchoffice', methods=['DELETE'])
def delete_user():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = branch_office_service.delete(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app_branch.route('/branchoffice/byfilter',methods=['POST'])
def get_users_by_filter():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error":
                        "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = branch_office_service.get_all_by_filter(data['Filter'])
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')