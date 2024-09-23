from rest_framework import serializers

from .models import NewsPost


class NewsPostSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=250)
    title_image = serializers.URLField(
        source='title_image.url'
    )

    date_creation = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=False)
    body = serializers.CharField()
    views_count = serializers.IntegerField(default=0)

    # def create(self, validated_data):
    #     return FilesCategory.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.category_name = validated_data.get('category_name', instance.category_name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance
    #
    class Meta:
        model = NewsPost
        fields = ['id', 'title', 'date_creation', 'is_published', 'body']