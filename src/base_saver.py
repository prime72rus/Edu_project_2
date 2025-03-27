from abc import ABC, abstractmethod


class AbstractSaver(ABC):
    """
    Абстрактный класс для работы с файлом
    """

    @abstractmethod
    def save_to_file(self) -> None:
        """
        Метод сохранения вакансий в файл
        """
        pass

    @abstractmethod
    def add_vacancy(self) -> None:
        """
        Метод добавления вакансии в файл
        """
        pass

    @abstractmethod
    def delete_vacancy(self) -> None:
        """
        Метод удаления вакансии из файла
        """
        pass

    @abstractmethod
    def load_from_file(self) -> None:
        """
        Загрузка вакансий из файла
        """
        pass

