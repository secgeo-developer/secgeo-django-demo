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
