"""Module providing create and finilize fixture"""
import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.enshure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def the_end():
        fixture.session.enshure_logout()
        fixture.destroy()
    request.addfinalizer(the_end)
    return fixture
