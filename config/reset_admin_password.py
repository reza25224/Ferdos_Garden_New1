import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ferdos_Garden_New - 1.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'  # نام کاربری مدیر شما
new_password = '309654@Ebm'  # رمز جدید

try:
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    print(f"Password for {username} updated successfully.")
except User.DoesNotExist:
    print(f"User '{username}' does not exist.")