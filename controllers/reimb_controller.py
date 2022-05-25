import flask
from flask import request, jsonify
from exceptions.resource_notfound import ResourceNotFound
from models.trms_classes import ReimburseStatus
from repositories.reimb_repoimp import ReimbImp
from services.reimb_service import TRMSReimbService

t1 = ReimbImp()
t2 = TRMSReimbService(t1)


# trp = ReimburseImp()
# trs = TRMSService(trp)


def route(app):
    @app.route("/reimburse/<ed>", methods=['GET'])
    def get_reim(ed):
        try:
            return t2.get_reim(ed).json(), 200
        except ValueError as v:
            return "Not a valid integer id", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reimburse", methods=['POST'])
    def sub_reim():
        body = request.json
        tm = ReimburseStatus(eid=body['eid'], e_name=body['e_name'], s_name=body['s_name'],
                             dept=body['dept'], course=body['course'], price=body['price'],
                             grade=body['grade'], amt=body['amt'], email_add=body['email_add'])
        tm = t2.sub_data(tm)
        response = flask.Response(tm)
        response.headers['Content-Type'] = 'application/json'
        return response


