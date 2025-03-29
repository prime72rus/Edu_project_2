from unittest.mock import MagicMock, patch

from src.external_api_hh import HeadHunterAPI


def test_get_vacancies_success():
    """Тест успешного получения вакансий."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "items": [
            {
                "name": "Python Dev",
                "alternate_url": "https://example.com",
                "salary": {"from": 100000, "currency": "RUR"},
            },
            {
                "name": "Java Dev",
                "alternate_url": "https://example.org",
                "salary": {"from": 120000, "currency": "USD"},
            },
        ]
    }
    with patch("src.external_api_hh.requests.get", return_value=mock_response):
        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Python")
        assert len(vacancies) == 2
        assert vacancies[0]["name"] == "Python Dev"
        assert vacancies[1]["name"] == "Java Dev"


def test_get_vacancies_failure():
    """Тест обработки ошибок при получении вакансий."""
    mock_response = MagicMock()
    mock_response.status_code = 400
    with patch("src.external_api_hh.requests.get", return_value=mock_response):
        api = HeadHunterAPI()
        try:
            api.get_vacancies("Python")
        except Exception as e:
            assert str(e) == "Ошибка при запросе к API: 400"
