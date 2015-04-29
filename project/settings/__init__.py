# -*- coding: utf-8 -*-
from project.exceptions import OpenCostLocalSettingsDoesNotExist

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

try:
    from .local import *
except ImportError:
    raise OpenCostLocalSettingsDoesNotExist("There is no local settings")

if DEBUG:
    from .production import *
else:
    from .development import *