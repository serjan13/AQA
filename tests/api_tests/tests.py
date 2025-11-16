import requests


def test_delete_user(api_session):
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiI2OGFhYzEyZi01YWRlLTQwZjgtYTNhMi0zOGNhZDUxODE1OTAiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzYzODI1NDU3LCJpYXQiOjE3NjMyMjU0NTcsImVtYWlsIjoic2VyZWdhMTk5NkBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImdpdGh1YiIsInByb3ZpZGVycyI6WyJnaXRodWIiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vYXZhdGFycy5naXRodWJ1c2VyY29udGVudC5jb20vdS8yNDQyMDI0Mzk_dj00IiwiZW1haWwiOiJzZXJlZ2ExOTk2QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FwaS5naXRodWIuY29tIiwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJqYW4xMyIsInByb3ZpZGVyX2lkIjoiMjQ0MjAyNDM5Iiwic3ViIjoiMjQ0MjAyNDM5IiwidXNlcl9uYW1lIjoic2VyamFuMTMifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTc2MzIyNTQ1N31dLCJzZXNzaW9uX2lkIjoiNzk2YmIwMDgtNmI3Ni00MTY5LTg3ZjQtYmY0MzI5ODQ3NGNlIiwiaXNfYW5vbnltb3VzIjpmYWxzZX0.j1JQPAWC9AK5nzVgT--3jbbHjIgoPrHayHDJ5Puu-ao",
"X-Task-Id": "API-1"}
    base_url = "https://release-gs.qa-playground.com/api/v1"
    session = api_session
    setup_response = session.post(url=base_url + "/setup")
    assert setup_response.status_code == 205
    users_response = session.get(url=base_url + "/users")
    assert users_response.status_code == 200
    users_json = users_response.json()
    user_uuid = users_json["users"][0]["uuid"]
    delete_response = session.delete(url = base_url + f"/users/{user_uuid}")
    assert delete_response.status_code == 204
    users_after_delete = session.get(url=base_url + "/users")
    users_after_delete_json = users_after_delete.json()
    uuid_list = [i["uuid"] for i in users_after_delete_json["users"]]
    assert user_uuid not in uuid_list
    user_info = session.get(url = base_url + f"/users/{user_uuid}")
    assert user_info.status_code == 404