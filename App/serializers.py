from rest_framework import serializers
from .models import CustomUser, ToDoItems, Tags


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = serializers.ListField(
        child=serializers.CharField(max_length=50),
        write_only=True
    )
    tag = TagSerializer(many=True, read_only=True, source='tags')

    class Meta:
        model = ToDoItems
        fields = '__all__'

    def create(self, validated_data):
        tags_list = validated_data.pop('tags', [])
        user = self.context['request'].user
        todo_item = ToDoItems.objects.create(user=user, **validated_data)

        for tag_name in tags_list:
            tag, created = Tags.objects.get_or_create(tag_name=tag_name)
            todo_item.tags.add(tag)

        return todo_item

    def update(self, instance, validated_data):
        tags_list = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)

        # Update tags
        instance.tags.clear()
        for tag_name in tags_list:
            tag, created = Tags.objects.get_or_create(tag_name=tag_name)
            instance.tags.add(tag)

        return instance
