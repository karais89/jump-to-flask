# pylint: disable=redefined-outer-name
import pytest
from pybo import create_app


@pytest.fixture
def api():
    app = create_app()
    app.config["TEST"] = True
    api = app.test_client()
    return api


# pytest 에서 자동으로 실행된다 - 테스트가 실행 될때
def setup_function():
    pass


# pytest 에서 자동으로 실행된다 - 테스트가 종료 될때
def teardown_function():
    pass


def test_hello_pybo(api):
    resp = api.get("/")
    assert b"Hello, Pybo!" in resp.data
