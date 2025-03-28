from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        """
        Метод для получения вакансий
        """
        pass
