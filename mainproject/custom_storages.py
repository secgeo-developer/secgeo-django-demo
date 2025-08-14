from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import FileSystemStorage


if settings.DEBUG:
    class MediaStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

    class DocumentStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

    class ImageSettingStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'
else:
    class MediaStorage(S3Boto3Storage):
        file_overwrite = False
        location = settings.MEDIA_LOCATION
        default_acl = 'public-read'

    class DocumentStorage(S3Boto3Storage):
        file_overwrite = False
        location = settings.DOCUMENT_LOCATION
        default_acl = 'public-read'

    class ImageSettingStorage(S3Boto3Storage):
        file_overwrite = False
        location = settings.IMAGE_SETTING_LOCATION
        default_acl = 'public-read'
