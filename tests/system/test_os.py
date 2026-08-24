import getpass
from pathlib import Path


def test_linux_os():
    os_release = Path("/etc/os-release").read_text()

    assert "Ubuntu" in os_release


def test_current_user():
    assert getpass.getuser() == "leonid"