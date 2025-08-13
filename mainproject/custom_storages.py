from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage

    class MediaStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'
else:
    from storages.backends.s3boto3 import S3Boto3Storage

    class MediaStorage(S3Boto3Storage):
        file_overwrite = False
        location = settings.MEDIA_LOCATION
        default_acl = 'public-read'