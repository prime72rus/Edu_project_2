import requests
from src.base_api import AbstractAPI

class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}
        self.vacancies = []


    def load_vacancies(self, search_query: str) -> list[dict]:
        self.params["text"] = search_query
        while self.params.get("page") != 1:
            response = requests.get(self.__url, headers=self.__headers, params=self.params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1
            else:
                raise Exception(f"Ошибка при запросе к API: {response.status_code}")
        return self.vacancies


