"""
pytest for Actors
"""

import pytest
from faker import Faker
from blueprints.actors import service 



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


def test_svc_get_all(mocker, fake_data):
    """
    get all actor service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `get_all_actors` to return the result of `doQuery`
    mocker.patch.object(service, "get_all_actors", return_value=mocker_sql.return_value)


    result = service.get_all_actors()
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["actor_id"] == fake_data["actor_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]


def test_svc_get_by_id(mocker, fake_id, fake_data):
    """
    get by actor id service test
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

    assert data[0]["actor_id"] == fake_data["actor_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]


def test_svc_create_new_actor(mocker, fake_data):
    """
    post new actor service test
    """

    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `create_new_actor` to return the result of `doQuery`
    mocker.patch.object(service, "create_new_actor", return_value=mocker_sql.return_value)

    result = service.create_new_actor(fake_data)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["actor_id"] == fake_data["actor_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]

def test_svc_update_actor(mocker, fake_data, fake_id):
    """
    update actor by id service test
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

    assert data[0]["actor_id"] == fake_data["actor_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]

def test_svc_delete_actor_by_id(mocker, fake_id, fake_data):
    """
    delete actor by id service test
    """

    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `delete_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "delete_by_id", return_value=mocker_sql.return_value)

    result = service.delete_by_id(fake_id)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["actor_id"] == fake_data["actor_id"]
    assert data[0]["first_name"] == fake_data["first_name"]
    assert data[0]["middle_name"] == fake_data["middle_name"]
    assert data[0]["last_name"] == fake_data["last_name"]



