from django.contrib.auth.forms import UserCreationForm
#from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User

# Create the form class
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# Create a form to add a user
form = RegisterForm()

# Create a form to edit a user
# user = User.objects.get()
# form = RegisterForm(instance=user)

