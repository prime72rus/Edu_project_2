import json
from typing import Any, Dict, List, Sequence, Union

from config import PATH_TO_JSON
from src.base_saver import AbstractSaver
from src.vacancies import Vacancy


class JSONSaver(AbstractSaver):
    """
    Класс для работы с JSON-файлом
    """
    __file_name: str
    vacancies_list: List[Dict[str, Any]]
    vacancies_list_dict: List[Dict[str, Any]]

    def __init__(self, file_name: str = PATH_TO_JSON):
        self.__file_name = file_name

    def save_to_file_rw(self, vacancies_list: Sequence[Union[Dict[str, Any], "Vacancy"]]) -> None:
        """
        Метод сохранения данных в файл c перезаписью
        """
        if all(isinstance(vacancy, dict) for vacancy in vacancies_list):
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(vacancies_list, file, ensure_ascii=False, indent=4)  # type: ignore
        elif all(isinstance(vacancy, Vacancy) for vacancy in vacancies_list):
            vacancies_list_only_vacancies = [vacancy for vacancy in vacancies_list if isinstance(vacancy, Vacancy)]
            self.vacancies_list_dict = self.obj_vacancy_to_list(vacancies_list_only_vacancies)
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(self.vacancies_list_dict, file, ensure_ascii=False, indent=4)  # type: ignore
        else:
            raise TypeError("Тип входных данных не соответствует требованиям")

    def save_to_file(self, vacancies_list: Sequence[Union[Dict[str, Any], "Vacancy"]]) -> None:
        """
        Метод добавления данных в файл
        """
        if all(isinstance(vacancy, dict) for vacancy in vacancies_list):
            vacancies_list_only_dict = [vacancy for vacancy in vacancies_list if isinstance(vacancy, dict)]
            extend_list = self.load_from_file() + vacancies_list_only_dict
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(extend_list, file, ensure_ascii=False, indent=4)  # type: ignore
        elif all(isinstance(vacancy, Vacancy) for vacancy in vacancies_list):
            vacancies_list_only_vacancies = [vacancy for vacancy in vacancies_list if isinstance(vacancy, Vacancy)]
            self.vacancies_list_dict = self.obj_vacancy_to_list(vacancies_list_only_vacancies)
            extend_list = self.load_from_file() + self.vacancies_list_dict
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(extend_list, file, ensure_ascii=False, indent=4)  # type: ignore
        else:
            raise TypeError("Тип входных данных не соответствует требованиям")

    def add_vacancy(self, vacancy: "Vacancy") -> None:
        """
        Метод добавления вакансии в файл
        """
        data = self.obj_vacancy_to_list([vacancy])[0]
        data_from_file = self.load_from_file()
        data_from_file.append(data)
        self.save_to_file_rw(data_from_file)

    def delete_vacancy(self, vacancy: "Vacancy") -> None:
        """
        Метод удаления вакансии из файла
        """
        data = self.obj_vacancy_to_list([vacancy])[0]
        data_from_file = self.load_from_file()
        try:
            data_from_file.remove(data)
        except ValueError:
            print("Элемент для удаления не найден")
        else:
            self.save_to_file_rw(data_from_file)

    def load_from_file(self) -> List[Dict[str, Any]]:
        """
        Метод для загрузки данных из файла
        """
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                self.vacancies_list = json.load(file)
        except json.decoder.JSONDecodeError:
            self.vacancies_list = []
        except FileNotFoundError:
            self.vacancies_list = []
        return self.vacancies_list

    def obj_vacancy_to_list(self, vacancies_list: Sequence["Vacancy"]) -> List[Dict[str, Any]]:
        """
        Метод конвертации списка объектов Vacancy в список словарей
        """
        self.vacancies_list_dict = []
        for vacancy in vacancies_list:
            self.vacancies_list_dict.append(
                {
                    "name": vacancy.name,
                    "alternate_url": vacancy.url,
                    "salary": {"from": vacancy.salary, "currency": vacancy.currency},
                    "professional_roles": [
                        {"name": item.strip()} for item in vacancy.professional_roles.split(", ") if item.strip()
                    ],
                    "snippet": {"responsibility": vacancy.responsibility},
                }
            )
        return self.vacancies_list_dict
