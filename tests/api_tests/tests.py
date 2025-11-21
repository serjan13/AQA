import requests
from models.user_models import UsersResponse


def test_delete_user(api_session):
    base_url = "https://release-gs.qa-playground.com/api/v1"
    session = api_session(task_id="API-1")
    setup_response = session.post(url=base_url + "/setup")
    assert setup_response.status_code == 205
    users_response = session.get(url=base_url + "/users")
    assert users_response.status_code == 200
    users_json = users_response.json()
    validate = UsersResponse.model_validate(users_json)
    user_uuid = users_json["users"][0]["uuid"]
    delete_response = session.delete(url = base_url + f"/users/{user_uuid}")
    assert delete_response.status_code == 204
    users_after_delete = session.get(url=base_url + "/users")
    users_after_delete_json = users_after_delete.json()
    validate = UsersResponse.model_validate(users_after_delete_json)
    uuid_list = [i["uuid"] for i in users_after_delete_json["users"]]
    assert user_uuid not in uuid_list
    user_info = session.get(url = base_url + f"/users/{user_uuid}")
    assert user_info.status_code == 404