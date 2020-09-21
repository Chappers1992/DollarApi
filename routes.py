from flask import request, redirect
from flask_restx import Resource

from api.uprocs.function import NewTask
from api.uprocs.dto import ns, new_task_post_dto


@ns.route('/RunUprocs')
class RunTask(Resource):
    @staticmethod
    @ns.expect(new_task_post_dto, required=True)
    def post():
        request_data = request.get_json()
        command_line = NewTask.generate_commandline(request_data['task'], request_data['mu'], request_data['processing_date'], request_data['start_date'],
                                                    request_data['args'])
        if command_line:
            return command_line
        # return request_data
        return None, 400
