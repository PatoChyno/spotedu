from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Task,
    )

from pyramid.httpexceptions import (
    HTTPException,
    HTTPNotFound,
    HTTPFound,
    HTTPForbidden,
    )


@view_config(route_name='pokus', renderer='project:templates/pokus.mako')
def pokus_view(request):
    return {}

@view_config(route_name='tasks', renderer='project:templates/tasks.mako')
def tasks(request):
    tasks=DBSession.query(Task).all()
    return {'tasks': tasks}

#@view_config(route_name='create', request_method="GET", renderer='project:templates/create.mako')

#TODO: ostatne views
