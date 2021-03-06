
from fixture.application import Application
from fixture.db import DbFixture
from fixture.orm import ORMFixture
import pytest
import json
import jsonpickle
import os.path
import importlib

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    webconfig = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseUrl=webconfig["baseUrl"])
    fixture.session.ensure_login(username=webconfig["username"], password=webconfig["password"])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    dbconfig = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=dbconfig["host"], name=dbconfig["name"], user=dbconfig["user"], password=dbconfig["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session")
def dbOrm(request):
    dbconfig = load_config(request.config.getoption("--target"))['db']
    dbOrmfixture = ORMFixture(host=dbconfig["host"], name=dbconfig["name"], user=dbconfig["user"], password=dbconfig["password"])
    return dbOrmfixture

@pytest.fixture(scope="session", autouse=True )
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" %module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\%s.json" %file)) as f:
        return jsonpickle.decode(f.read())

