from flask import Blueprint
from .schema import TeacherSchema
from core.apis import decorators, APIResponse
from core.models import Teacher
principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)


@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_all_teachers(p):
    all_teachers = Teacher.get_all_teachers()
    all_teaches_list_dump = TeacherSchema().dump(all_teachers, many=True)
    return APIResponse.respond(data=all_teaches_list_dump)