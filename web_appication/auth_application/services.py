from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """
    Построение пути к файлу (media)/avatar/user_id/photo.jpg
    :return:
    """
    return f'avatar/{instance.id}/{file}'


def validate_size_image(file_obj):
    """
    Проверка размера файла
    :param file_obj: 
    :return: 
    """

    limit_size_mb = 2

    if file_obj.size > limit_size_mb * 1024 * 1024:
        raise ValidationError("Максимальный размер файла 2мб")
    
    pass