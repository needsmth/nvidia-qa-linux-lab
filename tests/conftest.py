import pytest


@pytest.fixture
def os_release():
    with open("/etc/os-release") as file:
        return file.read()
