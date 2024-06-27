from django.core.exceptions import ValidationError

def image_size_validator(file):
    # 2mb
    max_size_mb = 2 
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"As of now we cannot accept an image more than {max_size_mb}MB.")