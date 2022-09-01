from json import dumps


def test_all_users_list(client):
    # test call to /all_users
    response = client.get("/api/staff/search/all_users")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == list
    assert len(response.json) > 0


def test_wishlist_empty(client):
    # test call to /wishlist
    response = client.get("/api/staff/search/wishlist")

    # Validate
    assert response.status_code == 204
    assert response.content_type == "application/json"


def test_wishlist(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    book_id = 41865

    # change the book availability to Borrowed so it can be put onto the wishlist
    response = client.put(f"/api/staff/admin/update_availability_to_borrowed/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type

    data = {
        "book_id": book_id,
        "user_id": 1
    }
    # test call to users/wish/wish_add
    response = client.post("/api/users/wish/wish_add", data=dumps(data), headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
        "Msg": f"The book with the book_id {book_id} has been added to your wishlist",
        "Status": "Successfully added to your Wishlist"
    }

    # test call to /wishlist
    response = client.get("/api/staff/search/wishlist")

    # Validate
    assert response.status_code == 200
    assert response.content_type == "application/json"

    # test call to users/wish/wish_delete
    response = client.delete(f"/api/users/wish/wish_delete/{book_id}/1", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
        "Msg": f"The book with the book_id {book_id} has been removed from your wishlist",
        "Status": "Success"
    }

    # change the book availability to Available
    response = client.put(f"/api/staff/admin/update_availability_to_available/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type

