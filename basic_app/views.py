from rest_framework.response import Response
from rest_framework import permissions, viewsets


class AbstractViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(create_user=self.request.user, update_user=self.request.user)

		
	def response(self, data):
		page = self.paginate_queryset(data)
		if page:
		    serializer = self.get_serializer(page, many=not self.detail)
		    return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(data, many=not self.detail)
		return Response(serializer.data)