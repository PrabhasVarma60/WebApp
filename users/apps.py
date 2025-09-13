from django.apps import AppConfig
import os

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
        if os.environ.get('DJANGO_SETTINGS_MODULE') != 'webapp_django.settings.production':
            return
        from django.contrib.auth.models import User
        from .models import Profile
        if not User.objects.filter(username='prabhasvarma').exists():
            admin_user = User.objects.create_superuser(
                'prabhasvarma',
                'prabhasvarma6061@gmail.com',
                'tixxy007'
            )
            Profile.objects.create(user=admin_user)
