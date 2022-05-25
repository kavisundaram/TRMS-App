import flask
from flask import request, jsonify
from exceptions.resource_notfound import ResourceNotFound
from models.trms_classes import Employees
from repositories.emp_repoimp import ReimburseImp
from services.trms_service import TRMSService


trp = ReimburseImp()
trs = TRMSService(trp)


def route(app):
    @app.route("/employee", methods=['GET'])
    def get_all():
        return jsonify([data.json() for data in trs.get_all()])

    @app.route("/employee/<e_id>", methods=['GET'])
    def get_details(e_id):
        try:
            return trs.get_details(e_id).json(), 200
        except ValueError as v:
            return "Not a valid integer id", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee", methods=['POST'])
    def add_emp():
        body = request.json
        em1 = Employees(emp_id=body['emp_id'], name=body['name'], supervisor_id=body['supervisor_id'],
                        sup_name=body['sup_name'], dept_id=body['dept_id'],
                        designation=body['designation'], email=body['email'])
        em1 = trs.create_data(em1)
        response = flask.Response(em1)
        response.headers['Content-Type'] = 'application/json'
        return response

        # return em1.json()

