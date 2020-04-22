from rest_framework import serializers

class AbstractSerializer(serializers.ModelSerializer):
	create_user = serializers.ReadOnlyField(source='create_user.id')
	update_user = serializers.ReadOnlyField(source='update_user.id')

	class Meta:
		exclude = ('create_dttm', 'update_dttm', )