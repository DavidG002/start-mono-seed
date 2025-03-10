from django.contrib.auth import get_user_model

User = get_user_model()
superusers = User.objects.filter(is_superuser=True)
print('Superusers:', superusers.count())
if superusers.count() == 0:
    User.objects.create_superuser('admin', 'admin@example.com', 'password')