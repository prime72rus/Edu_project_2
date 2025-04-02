from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    # @abstractmethod
    # def __connect_api(self) -> Any:
    #     """
    #     Метод для получения вакансий
    #     """
    #     pass

    @abstractmethod
    def get_data(self, search_query: str) -> List[Dict[str, Any]]:
        """
        Метод для получения вакансий
        """
        pass
