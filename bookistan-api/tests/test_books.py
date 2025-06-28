def test_create_book(client):
    response = client.post(
        "/books",
        json={
            "title": "The Pragmatic Programmer",
            "author": "Andrew Hunt",
            "price": 499.99,
            "description": "A classic programming book",
            "rating": 4.8,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "The Pragmatic Programmer"
    assert data["author"] == "Andrew Hunt"
    assert "id" in data


def test_get_books(client):
    # Add a book first
    client.post(
        "/books",
        json={
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "price": 350.0,
            "description": "A guide to writing clean code",
            "rating": 4.7,
        },
    )

    # Now fetch books
    response = client.get("/books")
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, list)
    assert any(book["title"] == "Clean Code" for book in data)
