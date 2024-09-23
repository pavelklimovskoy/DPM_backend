from rest_framework import serializers

from .models import Employee


class ResultEmployeeSerializer(serializers.Serializer):
    avatar = serializers.FileField()

    fullname = serializers.CharField(max_length=100)

    position = serializers.CharField(max_length=200)

    is_showed = serializers.BooleanField()

    class Meta:
        fields = ['avatar', 'fullname', 'position', 'is_showed']


class EmployeeSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    avatar = serializers.FileField()

    fullname_ru = serializers.CharField(
        max_length=100,
    )
    fullname_en = serializers.CharField(max_length=100)

    position_ru = serializers.CharField(
        max_length=200,
    )
    position_en = serializers.CharField(max_length=200)

    is_showed = serializers.BooleanField(
        default=True
    )

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
        model = Employee
        fields = ['id', 'avatar', 'fullname_ru', 'fullname_en', 'position_ru', 'position_en', 'is_showed']


class RuEmployeeSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    avatar = serializers.URLField(
        source='avatar.url'
    )

    fullname = serializers.CharField(
        max_length=100,
        source='fullname_ru'
    )

    position = serializers.CharField(
        max_length=200,
        source='position_ru'
    )

    is_showed = serializers.BooleanField(
        default=True
    )

    email = serializers.EmailField()

    show_email = serializers.BooleanField()

    class Meta:
        model = Employee
        fields = ['id', 'avatar', 'fullname', 'position', 'is_showed', 'email', 'show_email']


class EnEmployeeSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    avatar = serializers.URLField(
        source='avatar.url'
    )

    fullname = serializers.CharField(
        max_length=100,
        source='fullname_en'
    )

    position = serializers.CharField(
        max_length=200,
        source='position_en'
    )

    is_showed = serializers.BooleanField(
        default=True
    )

    email = serializers.EmailField()

    show_email = serializers.BooleanField()

    class Meta:
        model = Employee
        fields = ['id', 'avatar', 'fullname', 'position', 'is_showed', 'email', 'show_email']
