# -*- coding: utf-8 -*-
from project.exceptions import ProjectLocalSettingsDoesNotExist

##################################################################
# ALL INCLUDES OF SETTINGS FILES
#
# Add your new settings file here, order can be important
##################################################################
from .base import *
from .apps import *
from .auth import *
from .datetime import *
from .development import *
from .languages import *
from .logging import *
from .middlewares import *
from .static import *
from .templates import *
from .rest import *

try:
    from .local import *
except ImportError:
    from .production import *
    print("There is no local settings")
