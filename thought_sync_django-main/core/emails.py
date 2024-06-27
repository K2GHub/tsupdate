from djoser.email import ActivationEmail

class CustomActivationEmail(ActivationEmail):
    template_name = 'user_activation_email.html'  # Path to your custom activation.html template
    

    