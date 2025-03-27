from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def load_vacancies(self, search_query: str) -> list:
        """Метод для получения вакансий."""
        pass