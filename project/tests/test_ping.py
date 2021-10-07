def test_ping(test_app):
    # Given the state in test_app

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "ping": "the long pong",
        "testing": True,
    }
