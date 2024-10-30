"""
pytest for Directors
"""

import pytest
from faker import Faker
from blueprints.directors import service 



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
    faker_data["first_name"] = fake.pystr(min_chars=0, max_chars=25)
    faker_data["middle_name"] = fake.pystr(min_chars=0, max_chars=25)
    faker_data["last_name"] = fake.pystr(min_chars=0, max_chars=25)

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


def test_svc_get_all(mocker, fake_data, fake_id):
    """
    get all director service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_movie_directors_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "get_movie_directors_by_id", return_value=mocker_sql.return_value)


    result = service.get_movie_directors_by_id(fake_id)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["director_id"] == fake_data["director_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]


def test_svc_get_director_by_id(mocker, fake_data, fake_id):
    """
    get director by id service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_movie_directors_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "get_movie_directors_by_id", return_value=mocker_sql.return_value)


    result = service.get_movie_directors_by_id(fake_id, fake_data)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["director_id"] == fake_data["director_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]   


def test_svc_create_director(mocker, fake_data):
    """
    create director service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `create_director` to return the result of `doQuery`
    mocker.patch.object(service, "create_director", return_value=mocker_sql.return_value)


    result = service.create_director(fake_data)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["director_id"] == fake_data["director_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]

def test_svc_update_director(mocker, fake_data, fake_id):
    """
    update director service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `update_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "update_by_id", return_value=mocker_sql.return_value)


    result = service.update_by_id(fake_id, fake_data)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["director_id"] == fake_data["director_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]


def test_svc_delete_director(mocker, fake_id, fake_data):
    """
    delete director service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `delete_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "delete_by_id", return_value=mocker_sql.return_value)


    result = service.update_by_id(fake_id, fake_data)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["director_id"] == fake_data["director_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]
