import getpass


def test_linux_os(os_release):
    assert "Ubuntu" in os_release

def test_current_user():
    assert getpass.getuser() == "leonid"
