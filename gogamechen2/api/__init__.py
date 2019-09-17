from simpleutil.log import log as logging
from simpleutil.config import cfg

from simpleservice.ormdb.api import MysqlDriver

from goperation import lock

from gogamechen2 import common

CONF = cfg.CONF

DbDriver = None
GameLock = None


LOG = logging.getLogger(__name__)


def init_endpoint_session():
    global DbDriver
    if DbDriver is None:
        with lock.get('mysql-gogamechen2'):
            if DbDriver is None:
                LOG.info("Try connect database for gogamechen2")
                mysql_driver = MysqlDriver(common.NAME,
                                           CONF[common.NAME])
                mysql_driver.start()
                DbDriver = mysql_driver
    else:
        LOG.warning("Do not call init_endpoint_session more then once")


def endpoint_session(readonly=False, autocommit=True):
    if DbDriver is None:
        init_endpoint_session()
    return DbDriver.get_session(read=readonly,
                                autocommit=autocommit,
                                expire_on_commit=False)


def init_gamelock():
    global GameLock
    if GameLock is None:
        with lock.get('gamelock-gogamechen2'):
            if GameLock is None:
                LOG.info("Try init gamelock for gogamechen2")
                from goperation.manager.api import get_global
                from gogamechen2.api import gamelock
                gogamechen2_lock = gamelock.GoGameLock(gdata=get_global())
                GameLock = gogamechen2_lock
    else:
        LOG.warning("Do not call init_gamelock more then once")


def get_gamelock():
    if GameLock is None:
        init_gamelock()
    return GameLock
