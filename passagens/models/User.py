from django.contrib.auth.models import User

user = User.objects.create_user('joao','joao@hotmail.com','mypassword')

user.first_name = 'joão'
user.last_name = 'test'
user.save()