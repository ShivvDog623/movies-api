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
def in_payload():
    """
    in clause payload
    """
    faker_data = {}
    faker_data["field"] = "id"
    faker_data["values"] = [
        {"value" : 1},
        {"value" : 2}
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
def fake_movie_actor_data():
    """
    makes fake data
    returns fake data object
    """
    fake = Faker()
    faker_data = {}
    faker_data["movie_id"] = fake.pyint()
    faker_data["actor_id"] = fake.pyint()
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
def fake_movie_genre_data():
    """
    makes fake data
    returns fake data object
    """
    fake = Faker()
    faker_data = {}
    faker_data["movie_id"] = fake.pyint()
    faker_data["genre_id"] = fake.pyint()
    faker_data["genre"] = fake.pystr()
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
def multi_fake_ids():
    """
    fake id(s)
    """
    return "1, 2"


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

def test_svc_get_movie_by_id(mocker, fake_data, fake_id):
    """
    get movie by id service test
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

    assert data[0]["movie_id"] == fake_data["movie_id"]
    assert data[0]["title"] == fake_data["title"]
    assert data[0]["year"] == fake_data["year"]
    assert data[0]["description"] == fake_data["description"]
    assert data[0]["time"] == fake_data["time"]
    assert data[0]["rating"] == fake_data["rating"]
    assert data[0]["vote"] == fake_data["vote"]
    assert data[0]["revenue"] == fake_data["revenue"]
    assert data[0]["metascore"] == fake_data["metascore"]

def test_svc_create_movie(mocker, fake_data):
    """
    create a movie service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `create_movie` to return the result of `doQuery`
    mocker.patch.object(service, "create_movie", return_value=mocker_sql.return_value)


    result = service.create_movie(fake_data)
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

def test_svc_update_movie(mocker, fake_data, fake_id):
    """
    update a movie by id service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `update_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "update_by_id", return_value=mocker_sql.return_value)


    result = service.update_by_id(fake_data, fake_id)
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

def test_svc_by_in(mocker, in_payload, fake_data):
    """
    test byin endpoint service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `in_search` to return the result of `doQuery`
    mocker.patch.object(service, "in_search", return_value=mocker_sql.return_value)


    result = service.in_search(in_payload)
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

def test_svc_like_search(mocker, fake_data, fields_payload):
    """
    test by like search service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `like_search` to return the result of `doQuery`
    mocker.patch.object(service, "like_search", return_value=mocker_sql.return_value)


    result = service.like_search(fields_payload)
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

def test_svc_exact_search(mocker, fake_data, fields_payload):
    """
    test by exact search service test
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `exact_search` to return the result of `doQuery`
    mocker.patch.object(service, "exact_search", return_value=mocker_sql.return_value)


    result = service.exact_search(fields_payload)
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


def test_svc_movie_directors_by_id(mocker, fake_movie_director_data, fields_payload, fake_id, fake_data):
    """
    test service to return director and movie data by movie_id
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `movie_directors_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "movie_directors_by_id", return_value={"status": 200, "data": [fake_movie_director_data]})


    result = service.movie_directors_by_id(fields_payload, fake_id)
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



def test_svc_movie_actors_by_id(mocker, fake_movie_actor_data, fields_payload, fake_id, fake_data):
    """
    test service to return actor and movie data by movie_id
    """
    # Mock `doQuery` to return data
    mocker_sql = mocker.patch.object(service, "doQuery")
    mocker_sql.return_value = {"status": 200, "data" : [fake_data]}

    # Mock `movie_actors_by_id` to return the result of `doQuery`
    mocker.patch.object(service, "movie_actors_by_id", return_value={"status": 200, "data": [fake_movie_actor_data]})


    result = service.movie_actors_by_id(fields_payload, fake_id)
    data = result["data"]
    status = result["status"]

    # assertions
    assert isinstance(data, list)
    assert status == 200

    assert data[0]["movie_id"] == fake_movie_actor_data["movie_id"]
    assert data[0]["actor_id"] == fake_movie_actor_data["actor_id"]
    assert data[0]["first_name"] == fake_movie_actor_data["first_name"]
    assert data[0]["middle_name"] == fake_movie_actor_data["middle_name"]
    assert data[0]["last_name"] == fake_movie_actor_data["last_name"]
    assert data[0]["title"] == fake_movie_actor_data["title"]
    assert data[0]["year"] == fake_movie_actor_data["year"]
    assert data[0]["description"] == fake_movie_actor_data["description"]
    assert data[0]["time"] == fake_movie_actor_data["time"]
    assert data[0]["rating"] == fake_movie_actor_data["rating"]
    assert data[0]["vote"] == fake_movie_actor_data["vote"]
    assert data[0]["revenue"] == fake_movie_actor_data["revenue"]
    assert data[0]["metascore"] == fake_movie_actor_data["metascore"]