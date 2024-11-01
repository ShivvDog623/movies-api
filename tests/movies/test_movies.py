"""
pytest for Movies
"""

import pytest
from faker import Faker
from blueprints.movies import service 



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
    faker_data["movie_id"] = fake.pyint()
    faker_data["title"] = fake.pystr(min_chars=0, max_chars=25)
    faker_data["year"] = fake.pyint()
    faker_data["description"] = fake.pystr(min_chars=0, max_chars=1000)
    faker_data["time"] = fake.pyint()
    faker_data["rating"] = fake.pyfloat()
    faker_data["vote"] = fake.pyint()
    faker_data["revenue"] = fake.pyint()
    faker_data["metascore"] = fake.pyint()



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


def test_svc_get_all_movies(mocker, fake_data):
    """
    get all movies service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_all` to return the result of `doQuery`
    mocker.patch.object(service, "get_all", return_value=mocker_sql.return_value)


    result = service.get_all()
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["movie_id"] == fake_data["movie_id"]
    assert data[0]["title"] == fake_data["title"]
    assert data[0]["year"] == fake_data["year"]
    assert data[0]["description"] == fake_data["description"]
    assert data[0]["time"] == fake_data["time"]
    assert data[0]["rating"] == fake_data["rating"]
    assert data[0]["vote"] == fake_data["vote"]
    assert data[0]["revenue"] == fake_data["revenue"]
    assert data[0]["metascore"] == fake_data["metascore"]
