from typing import Any, Dict, List

import requests

from src.base_api import AbstractAPI
from src.exceptions import RequestsAPIError


class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self) -> None:
        self.__url: str = "https://api.hh.ru/vacancies"
        self.__headers: dict[str, str] = {"User-Agent": "HH-User-Agent"}
        self.__params: dict[str, Any] = {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}
        self.__vacancies: List[Dict[str, Any]] = []

    def __get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        count_error_request = 3
        self.__params["text"] = search_query
        while self.__params.get("page") != 1:
            if count_error_request != 0:
                try:
                    response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                    if response.status_code != 200:
                        raise RequestsAPIError(f"Ошибка при запросе к API: {response.status_code}")
                except RequestsAPIError:
                    count_error_request -= 1
                    print("Ошибка при запросе к API")
                    continue
                else:
                    vacancies = response.json().get("items", [])
                    self.__vacancies.extend(vacancies)
                    self.__params["page"] += 1
            else:
                print("Количество попыток запроса исчерпано")
                break
        return self.__vacancies

    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        return self.__get_vacancies(search_query)
