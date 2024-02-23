from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.security import forget, remember
from .models import User

@view_config(route_name='login', renderer='templates/login.jinja2')
def login_view(request):
    if request.method == 'POST':
        username = request.params.get('username')
        password = request.params.get('password')

        user = request.dbsession.query(User).filter_by(username=username).first()

        if user and user.password_hash and bcrypt.verify(password, user.password_hash):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('home'), headers=headers)
        else:
            return HTTPForbidden()

    return {}

@view_config(route_name='logout')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('login'), headers=headers)
