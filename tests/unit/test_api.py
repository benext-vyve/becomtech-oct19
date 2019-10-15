def test_healthcheck(client):
    '''
    GIVEN a Flask application
    WHEN a GET request to '/healthcheck' is triggered
    THEN the application return 200 and a valid message
    '''
    response = client.get('/healthcheck')
    print(dir(response))
    assert response.status_code == 200
    assert response.data == b"I'm okay dude"
