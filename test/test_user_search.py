

def test_book_search_by_title(client):
    # test call to /search_by_title/<string:book_title>
    response = client.get("/api/users/search/search_by_title/Time")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == list
    assert len(response.json) > 0


def test_book_search_by_author(client):
    # test call to /search_by_title/<string:book_author>
    response = client.get("/api/users/search/search_by_author/Hawk")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == list
    assert len(response.json) > 0


def test_book_search_by_title_and_author(client):
    # test call to /search_by_title_and_author/<string:book_title>/<string:book_author>
    response = client.get("/api/users/search/search_by_title_and_author/Train/Hawk")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == list
    assert len(response.json) > 0


def test_book_search_by_title_and_author_2(client):
    # test call to /search_by_title_and_author/<string:book_title>/<string:book_author>
    response = client.get("/api/users/search/search_by_title_and_author/Time/Hawk")

    # Validate
    assert response.status_code == 204

