"""
pytest for Genres
"""

import pytest
from faker import Faker
from blueprints.genres import service 



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
    faker_data["genre_id"] = fake.pyint()
    faker_data["genre"] = fake.pystr(min_chars=0, max_chars=25)


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
    get all genre service test
    """

    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_all` to return the result of `doQuery`
    mocker.patch.object(service, "get_id", return_value=mocker_sql.return_value)

    result = service.get_all()
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["genre_id"] == fake_data["genre_id"]
    assert data[0]["genre"] == fake_data["genre"]

def test_svc_get_genre_by_id(mocker, fake_data, fake_id):
    """
    get genre by id service test
    """

    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_id` to return the result of `doQuery`
    mocker.patch.object(service, "get_id", return_value=mocker_sql.return_value)

    result = service.get_id(fake_id)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["genre_id"] == fake_data["genre_id"]
    assert data[0]["genre"] == fake_data["genre"]

def test_svc_create_genre(mocker, fake_data, fake_id):
    """
    create genre service test
    """

    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `create_genre` to return the result of `doQuery`
    mocker.patch.object(service, "create_genre", return_value=mocker_sql.return_value)

    result = service.create_genre(fake_id, fake_data)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["genre_id"] == fake_data["genre_id"]
    assert data[0]["genre"] == fake_data["genre"]

def test_svc_update_genre(mocker, fake_data, fake_id):
    """
    update genre service test
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

    assert data[0]["genre_id"] == fake_data["genre_id"]
    assert data[0]["genre"] == fake_data["genre"]

def test_svc_delete_genre(mocker, fake_data, fake_id):
    """
    delete genre service test
    """

    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `delete_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "delete_by_id", return_value=mocker_sql.return_value)

    result = service.delete_by_id(fake_id, fake_data)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["genre_id"] == fake_data["genre_id"]
    assert data[0]["genre"] == fake_data["genre"]


