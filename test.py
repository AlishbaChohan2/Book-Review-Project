import requests
import json
import unittest
from unittest.mock import patch, Mock, MagicMock


def get_data(isbn):
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
    data = json.loads(response.text)
    return data

class TestGetData(unittest.TestCase):
    @patch('requests.get')
    def test_get_data(self, mock_get_data):
        mock_response = MagicMock()
        mock_response.text = json.dumps({"items": [{"title": "Inferno"}]})
        mock_get_data.return_value = mock_response
        isbn = "9780593072493"
        result = get_data(isbn)
        self.assertIn("items", result)
        self.assertEquals(result["items"][0]["title"], "Inferno")
        mock_get_data.assert_called_with(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')

if __name__ == '__main__':
    unittest.main()
