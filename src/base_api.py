from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, search_query: str) -> list[dict]:
        """
        Метод для получения вакансий
        """
        pass
