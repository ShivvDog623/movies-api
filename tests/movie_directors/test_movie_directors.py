"""
pytest for Movie_Directors
"""

import pytest
from faker import Faker
from blueprints.movie_directors import service


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
    faker_data["director_id"] = fake.pyint()
    faker_data["movie_id"] = fake.pyint()

    return faker_data

@pytest.fixture
def fake_movie_director_data():
    """
    makes fake data
    returns fake data object
    """
    fake = Faker()
    faker_data = {}
    faker_data["movie_id"] = fake.pyint()
    faker_data["director_id"] = fake.pyint()
    faker_data["first_name"] = fake.pystr()
    faker_data["middle_name"] = fake.pystr()
    faker_data["last_name"] = fake.pystr()
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


def test_svc_get_all(mocker, fake_data):
    """
    get all movie_director service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_all_movie_directors` to return the result of `doQuery`
    mocker.patch.object(service, "get_all_movie_directors", return_value=mocker_sql.return_value)

    result = service.get_all_movie_directors()
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["director_id"] == fake_data["director_id"]
    assert data[0]["movie_id"] == fake_data["movie_id"]


def test_svc_movie_directors_by_id(mocker, fake_movie_director_data, fields_payload, fake_id, fake_data):
    """
    test service to return director and movie data by director_id
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `movie_directors_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "get_id", return_value={"status": 200, "data": [fake_movie_director_data]})


    result = service.get_id(fields_payload, fake_id)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["movie_id"] == fake_movie_director_data["movie_id"]
    assert data[0]["director_id"] == fake_movie_director_data["director_id"]
    assert data[0]["first_name"] == fake_movie_director_data["first_name"]
    assert data[0]["middle_name"] == fake_movie_director_data["middle_name"]
    assert data[0]["last_name"] == fake_movie_director_data["last_name"]
    assert data[0]["title"] == fake_movie_director_data["title"]
    assert data[0]["year"] == fake_movie_director_data["year"]
    assert data[0]["description"] == fake_movie_director_data["description"]
    assert data[0]["time"] == fake_movie_director_data["time"]
    assert data[0]["rating"] == fake_movie_director_data["rating"]
    assert data[0]["vote"] == fake_movie_director_data["vote"]
    assert data[0]["revenue"] == fake_movie_director_data["revenue"]
    assert data[0]["metascore"] == fake_movie_director_data["metascore"]

