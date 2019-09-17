from simpleutil.config import cfg
from gogamechen2.api.wsgi.config import register_opts

from gogamechen2 import common

CONF = cfg.CONF

register_opts(CONF.find_group(common.NAME))
