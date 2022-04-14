from dj_rest_auth.serializers import PasswordResetSerializer
from accounts.forms import CustomResetPasswordForm


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomResetPasswordForm

    def get_email_options(self):
        return {
            "email_template": "account/email/user_password_reset",
        }
