from django.apps import AppConfig




class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
        import users.signals
         # Create admin if it doesn't exist
        from django.contrib.auth.models import User
        if not User.objects.filter(username='prabhasvarma').exists():
            User.objects.create_superuser(
                'prabhasvarma',
                'prabhasvarma6061@gmail.com',
                'tixxy007'
            )
    
       
