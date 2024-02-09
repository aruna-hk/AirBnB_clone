try:
    from .engine import file_storage
    storage = file_storage.FileStorage()
    storage.reload()
except ImportError as e:
    pass


try:
    from . import base_model
except Exception as e:
    pass
x = "kiptoo haron"
