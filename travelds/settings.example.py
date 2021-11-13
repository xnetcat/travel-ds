SECRET_KEY = "fdgkhjdsfgjkdfbgkjsdfbgjkbkj423bvjk34bv543"
DEBUG = False
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["travelds"]
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "traveldb",
        "USER": "root",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    },
}