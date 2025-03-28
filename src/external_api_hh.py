from typing import Any, Dict, List

import requests

from src.base_api import AbstractAPI
from src.exceptions import RequestsAPIError


class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self) -> None:
        self.__url: str = "https://api.hh.ru/vacancies"
        self.__headers: dict[str, str] = {"User-Agent": "HH-User-Agent"}
        self.params: dict[str, Any] = {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}
        self.vacancies: List[Dict[str, Any]] = []

    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        count_error_request = 3
        self.params["text"] = search_query
        while self.params.get("page") != 1:
            if count_error_request != 0:
                try:
                    response = requests.get(self.__url, headers=self.__headers, params=self.params)
                    if response.status_code != 200:
                        raise RequestsAPIError(f"Ошибка при запросе к API: {response.status_code}")
                except RequestsAPIError:
                    count_error_request -= 1
                    print("Ошибка при запросе к API")
                    continue
                except requests.exceptions.ConnectionError:
                    count_error_request -= 1
                    print("Connection error")
                    continue
                else:
                    vacancies = response.json().get("items", [])
                    self.vacancies.extend(vacancies)
                    self.params["page"] += 1
            else:
                print("Количество попыток запроса исчерпано")
                break
        return self.vacancies
