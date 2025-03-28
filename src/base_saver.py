from abc import ABC, abstractmethod
from typing import Any, Dict, List, Sequence, Union

from src.vacancies import Vacancy


class AbstractSaver(ABC):
    """
    Абстрактный класс для работы с файлом
    """

    @abstractmethod
    def save_to_file(self, vacancies_list: Sequence[Union[Dict[str, Any], "Vacancy"]]) -> None:
        """
        Метод сохранения вакансий в файл
        """
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: "Vacancy") -> None:
        """
        Метод добавления вакансии в файл
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: "Vacancy") -> None:
        """
        Метод удаления вакансии из файла
        """
        pass

    @abstractmethod
    def load_from_file(self) -> List[Dict[str, Any]]:
        """
        Загрузка вакансий из файла
        """
        pass
