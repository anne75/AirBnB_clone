"""
Declares the models directory as a package

Imports file_storage and creates an instance of FileStorage
"""

# import sys
# sys.path.insert(1, '..')

import models.engine.file_storage
storage = models.engine.file_storage.FileStorage()
storage.reload()
