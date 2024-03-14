from rest_framework.permissions import BasePermission

class IsStaffUserPermission(BasePermission):
	def has_permission(self, request, view):
		user = request.user
		if user.is_staff:
			return True
		return False

class IsHomeworkReceiver(BasePermission):
	def has_object_permission(self, request, view, obj):
		return request.user.student.grade == obj.grade

class IsTeacherPermission(BasePermission):
	def has_permission(self, request, view):
		return request.user.is_staff