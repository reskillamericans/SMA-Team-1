from django.contrib.auth.forms import UserCreationForm
#from django.core.exceptions import NON_FIELD_ERRORS
#from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

# Create the POST form class
class RegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email']

# Create the GET form class

# Create a form to add a user
form = RegisterForm()

# Create a form to edit a user
# user = User.objects.get()
# form = RegisterForm(instance=user)

