from unittest.mock import MagicMock, patch

import pytest

from src.exceptions import RequestsAPIError


def test_initial_headhunterapi(hh_api):
    """
    Тест инициализации объекта класса HeadHunterAPI
    """
    assert hh_api.vacancies == []
    assert hh_api._HeadHunterAPI__url == "https://api.hh.ru/vacancies"
    assert hh_api._HeadHunterAPI__headers == {"User-Agent": "HH-User-Agent"}
    assert hh_api._HeadHunterAPI__params == {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}


@patch("requests.get")
def test_get_data(mock_get, hh_api):
    """
    Тест получения вакансий
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"id": 1, "name": "Python Developer"}]}
    mock_get.return_value = mock_response

    result = hh_api.get_data("Python")

    assert len(result) == 20
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Python Developer"
    assert hh_api._HeadHunterAPI__params["text"] == "Python"


@patch("requests.get")
def test_three_error_code_status(mock_get, hh_api, capsys):
    """
    Тест на ошибку запроса в трех попытках
    """
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    result = hh_api.get_data("C++")

    assert mock_get.call_count == 3
    assert result == []
    captured = capsys.readouterr()
    assert "Количество попыток запроса исчерпано" in captured.out


@patch("requests.get")
def test_empty_response_items(mock_get, hh_api):
    """
    Тест получения пустого ответа от API
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    result = hh_api.get_data("JavaScript")

    assert result == []
    assert hh_api._HeadHunterAPI__params["page"] == 20  # Увеличилось на 1


def test_requests_api_error_handling(hh_api):
    """
    Тест на вызов пользовательского исключения
    """
    with patch("requests.get", side_effect=RequestsAPIError("Connection error")):
        with pytest.raises(RequestsAPIError):
            hh_api._HeadHunterAPI__connect_api()
