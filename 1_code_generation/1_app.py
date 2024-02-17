from typing import Dict, Union

from IPython import get_ipython
from IPython.display import display, Image

import autogen 

confg_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST"
)