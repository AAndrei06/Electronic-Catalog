from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .permissions import IsStaffUserPermission

class AuthAndPermissionMixin(object):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticated, IsStaffUserPermission]