from flask_restx import Namespace, fields

ns = Namespace('Tasks', description='Endpoints related to tasks.')

new_tasks_args_dto = ns.model('Args', {
    'arg': fields.String,
    'value': fields.String
})

new_task_post_dto = ns.model('Task', {
    'task': fields.String(required=True),
    'mu': fields.String(required=True),
    'processing_date': fields.String(required=True),
    'start_date': fields.String(required=True),
    'args': fields.List(
        fields.Nested(new_tasks_args_dto, required=True), required=True
        )
})
