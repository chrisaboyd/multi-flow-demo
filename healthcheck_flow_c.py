import platform
import sys

import prefect
from prefect.runtime import deployment 
from prefect.context import get_run_context
from prefect import task, flow, get_run_logger
from prefect.server.api.server import SERVER_API_VERSION


@task
def log_platform_info():
    logger = get_run_logger()
    logger.info(
        f"Host's network name = {platform.node()}\n"
        f"Python version = {platform.python_version()}\n"
        f"Platform information (instance type) = {platform.platform()}\n"
        f"OS/Arch = {sys.platform}/{platform.machine()}\n"
        f"Prefect Version = {prefect.__version__} 🚀\n"
        f"Prefect API Version = {SERVER_API_VERSION}\n"
    )


@flow(name="Flow_C")
def healthcheck():
    logger = get_run_logger()
    logger.info(deployment.name)
    logger.info(get_run_context().flow.name)
    log_platform_info()


if __name__ == "__main__":
    healthcheck()
