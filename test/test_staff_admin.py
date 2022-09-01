from json import dumps


def test_update_availability_to_available_failure(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    book_id = 41865

    # test call to /update_availability_to_available/<int:book_id>
    response = client.put(f"/api/staff/admin/update_availability_to_available/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 404
    assert response.content_type == content_type
    assert response.json == {
                   "Msg": f"The book with the book_id {book_id} is already available for pickup",
                   "Status": "Declined to update the availability"
               }


def test_update_availability_to_available_success(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    book_id = 41865

    # change the book availability to Borrowed hence it can be put onto the wishlist
    response = client.put(f"/api/staff/admin/update_availability_to_borrowed/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
        "Msg": f"The book with the book_id {book_id} is now in Borrowed status",
        "Status": "Successfully updated availability to Borrowed"
    }

    # test call to /update_availability_to_available/<int:book_id>
    response = client.put(f"/api/staff/admin/update_availability_to_available/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
                   "Msg": f"The book with the book_id {book_id} is now in Available status",
                   "Status": "Successfully updated availability to Available"
               }


def test_update_availability_to_borrowed_success(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    book_id = 41865

    # test call to /update_availability_to_borrowed/<int:book_id>
    response = client.put(f"/api/staff/admin/update_availability_to_borrowed/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
                   "Msg": f"The book with the book_id {book_id} is now in Borrowed status",
                   "Status": "Successfully updated availability to Borrowed"
               }

    # change the book availability to Available
    response = client.put(f"/api/staff/admin/update_availability_to_available/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
                   "Msg": f"The book with the book_id {book_id} is now in Available status",
                   "Status": "Successfully updated availability to Available"
    }


def test_update_availability_to_borrowed_failure(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    book_id = 41865

    # change the book availability to Borrowed hence it can be put onto the wishlist
    response = client.put(f"/api/staff/admin/update_availability_to_borrowed/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
        "Msg": f"The book with the book_id {book_id} is now in Borrowed status",
        "Status": "Successfully updated availability to Borrowed"
    }

    # test call to /update_availability_to_borrowed/<int:book_id>
    response = client.put(f"/api/staff/admin/update_availability_to_borrowed/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 404
    assert response.content_type == content_type
    assert response.json == {
                   "Msg": f"The book with the book_id {book_id} is already borrowed",
                   "Status": "Declined to update the availability"
               }

    # change the book availability to Available
    response = client.put(f"/api/staff/admin/update_availability_to_available/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
        "Msg": f"The book with the book_id {book_id} is now in Available status",
        "Status": "Successfully updated availability to Available"
    }


def test_generate_report_empty(client):
    # test call to /generate_report
    response = client.get("/api/staff/admin/generate_report")

    # Validate
    assert response.status_code == 201
    assert response.content_type == "application/json"
    assert type(response.json) == list
    assert len(response.json) == 0


def test_generate_report_populated(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }

    book_id = 41865

    # change the book availability to Borrowed hence it can show up in the report
    response = client.put(f"/api/staff/admin/update_availability_to_borrowed/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
        "Msg": f"The book with the book_id {book_id} is now in Borrowed status",
        "Status": "Successfully updated availability to Borrowed"
    }

    # test call to /generate_report
    response = client.get("/api/staff/admin/generate_report")

    # Validate
    assert response.status_code == 201
    assert response.content_type == "application/json"
    assert type(response.json) == list
    assert len(response.json) == 1

    # change the book availability to Available
    response = client.put(f"/api/staff/admin/update_availability_to_available/{book_id}", headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json == {
        "Msg": f"The book with the book_id {book_id} is now in Available status",
        "Status": "Successfully updated availability to Available"
    }

