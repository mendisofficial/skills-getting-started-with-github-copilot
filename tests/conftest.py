from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def isolated_activities(monkeypatch):
    monkeypatch.setattr(app_module, "activities",
                        deepcopy(app_module.activities))


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client
