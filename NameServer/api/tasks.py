from background_task import background
from logging import getLogger


logger = getLogger(__name__)


@background
def periodic_check_alive(name):
    # lookup user by id and send them a message
    logger.info("ciao " + name)