try:
    from . import file_storage
except Exception as e:
    pass
try:
    print("importing base model")
    from .models import base_model
    print("imported")
except Exception as e:
    pass
