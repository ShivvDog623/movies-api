"""
pytest for Movie_Actor
"""

import pytest
from faker import Faker
from blueprints.movie_actor import service


@pytest.fixture
def fields_payload():
    """
    creates a fake field value data
    """

    faker_data = {}
    
    faker_data["fields"] = [
        {
            "fields" : "id",
            "value" : 1
        }
    ]

    return faker_data


@pytest.fixture
def fake_data():
    """
    makes fake data
    returns fake data object
    """

    fake = Faker()
    faker_data = {}
    faker_data["actor_id"] = fake.pyint()
    faker_data["movie_id"] = fake.pyint()

    return faker_data

@pytest.fixture
def fake_id():
    """
    fake id
    """
    return "1"


@pytest.fixture
def fake_ids():
    """
    fake id(s)
    """
    return "1"


def test_svc_get_all(mocker, fake_data):
    """
    get all movie_actor service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_all_actors` to return the result of `doQuery`
    mocker.patch.object(service, "get_all_movieactors", return_value=mocker_sql.return_value)

    result = service.get_all_movieactors()
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["actor_id"] == fake_data["actor_id"]
    assert data[0]["movie_id"] == fake_data["movie_id"]
