''' #This class will provide the authentication system through a LDAP server. 

isn't locally running can be downloaded from https://pypi.org/project/python-ldap/


from django.contrib.auth.backends import ModelBackend
from django_auth_ldap.backend import LDAPBackend
from django.contrib.auth import get_user_model

class MyLDAPBackend(LDAPBackend):
   #A custom LDAP authentication backend

    def authenticate(self, username, password):

        user = LDAPBackend.authenticate(self, username, password)

        # If user has successfully logged, save his password in django database
        if user:
            user.set_password(password)
            user.save()

        return user
        

in order to combine the ldap authentication a custom authentication class can be done and mix both systems fro user validation

class MyAuthBackend(ModelBackend):
   A custom authentication backend overriding django ModelBackend 
'''