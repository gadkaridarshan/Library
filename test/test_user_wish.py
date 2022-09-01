from json import dumps


def test_wish_add_failure(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }
    data = {
        "book_id": 41865,
        "user_id": 1
    }
    # test call to users/wish/wish_add
    response = client.post("/api/users/wish/wish_add", data=dumps(data), headers=headers)

    # Validate
    assert response.status_code == 404
    assert response.content_type == content_type
    assert response.json == {
        "Msg": "The book with the book_id 41865 is already available for pickup",
        "Status": "Declined to be added to the Wishlist"
    }


def test_wish_add_success(client):
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

    # change the book availability to Available
    response = client.put(f"/api/staff/admin/update_availability_to_available/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type


def test_wish_delete_failure(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    book_id = 41865

    # test call to users/wish/wish_delete
    response = client.delete(f"/api/users/wish/wish_delete/{book_id}/1", headers=headers)

    # Validate
    assert response.status_code == 404
    assert response.content_type == content_type
    assert response.json == {
        "Error Msg": f"The book with the book_id {book_id} is not on your wishlist",
        "Status": "Failure"
    }


def test_wish_delete_success(client):
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


def test_wish_list_1(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    # test call to users/wish/wishlist/<string:user_id>
    response = client.get(f"/api/users/wish/wishlist/1", headers=headers)

    # Validate
    assert response.status_code == 204
    assert response.content_type == content_type


def test_wish_list_2(client):
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

    # test call to users/wish/wishlist/<string:user_id>
    response = client.get(f"/api/users/wish/wishlist/1", headers=headers)

    # Validate
    assert response.status_code == 200
    assert response.content_type == content_type

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

