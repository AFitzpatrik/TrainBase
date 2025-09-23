from django.contrib.auth.forms import UserCreationForm


# Registration form, expands on built-in form UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'first_name'
            'last_name'
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',

        ]
