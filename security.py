from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .models import User
from passlib.hash import bcrypt

def groupfinder(userid, request):
    user = request.dbsession.query(User).filter_by(username=userid).first()
    return ['admin'] if user and user.username == 'admin' else []

authentication_policy = AuthTktAuthenticationPolicy('supersecret', callback=groupfinder, hashalg='sha512')
authorization_policy = ACLAuthorizationPolicy()
