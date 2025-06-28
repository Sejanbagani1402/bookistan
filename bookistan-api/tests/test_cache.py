from unittest.mock import patch


def test_cache_miss_and_db_fallback(client):
    with patch("app.routers.book.get_book_cache", return_value=None), patch(
        "app.routers.book.set_book_cache"
    ) as mock_set_cache:

        client.post(
            "/books",
            json={
                "title": "Design Patterns",
                "author": "Erich Gamma",
                "price": 399.0,
                "description": "GoF Design Patterns",
                "rating": "4.6",
            },
        )

        response = client.get("/books")
        assert response.status_code == 201
        data = response.json()
        assert any(book["title"] == "Design Patterns" for book in data)

        mock_set_cache.assert_called()
