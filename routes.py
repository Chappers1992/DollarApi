from flask import request, redirect
from flask_restx import Resource

from api.tasks.function import NewTask
from api.tasks.dto import ns, new_task_post_dto


@ns.route('/RunTask')
class RunTask(Resource):
    @staticmethod
    @ns.expect(new_task_post_dto, validate=True)
    def post():
        request_data = request.get_json()
        command_line = NewTask.run_commandline(request_data['task'], request_data['mu'], request_data['processing_date'], request_data['start_date'],
                                                    request_data['args'])
        if command_line:
            return command_line
        return None, 400
