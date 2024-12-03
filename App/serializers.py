from rest_framework import serializers
from .models import CustomUser, ToDoItems


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ItemsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ToDoItems
        fields = '__all__'

    def validate_tags(self, tags):
        if not isinstance(tags, list):
            raise serializers.ValidationError("Tags must be a list.")
        return list(set(tags))

    def create(self, validated_data):

        user = self.context['request'].user
        validated_data['tags'] = list(set(validated_data.get('tags', [])))

        todo_item = ToDoItems.objects.create(user=user, **validated_data)
        return todo_item

    def update(self, instance, validated_data):
        tags = validated_data.get('tags', [])
        validated_data['tags'] = list(set(tags))
        return super().update(instance, validated_data)
