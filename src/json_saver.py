import json
from pathlib import Path
from typing import Any, Dict, List, Sequence, Union

from config import PATH_TO_JSON
from src.base_saver import AbstractSaver
from src.vacancies import Vacancy


class JSONSaver(AbstractSaver):
    """
    Класс для работы с JSON-файлом
    """

    file_name: Path = PATH_TO_JSON
    vacancies_list: List[Dict[str, Any]]
    vacancies_list_dict: List[Dict[str, Any]]

    @classmethod
    def save_to_file_rw(cls, vacancies_list: Sequence[Union[Dict[str, Any], "Vacancy"]]) -> None:
        """
        Метод сохранения данных в файл c перезаписью
        """
        if all(isinstance(vacancy, dict) for vacancy in vacancies_list):
            with open(cls.file_name, "w", encoding="utf-8") as file:
                json.dump(vacancies_list, file, ensure_ascii=False, indent=4)  # type: ignore
        elif all(isinstance(vacancy, Vacancy) for vacancy in vacancies_list):
            vacancies_list_only_vacancies = [vacancy for vacancy in vacancies_list if isinstance(vacancy, Vacancy)]
            cls.vacancies_list_dict = cls.obj_vacancy_to_list(vacancies_list_only_vacancies)
            with open(cls.file_name, "w", encoding="utf-8") as file:
                json.dump(cls.vacancies_list_dict, file, ensure_ascii=False, indent=4)  # type: ignore
        else:
            raise TypeError("Тип входных данных не соответствует требованиям")

    @classmethod
    def save_to_file(cls, vacancies_list: Sequence[Union[Dict[str, Any], "Vacancy"]]) -> None:
        """
        Метод добавления данных в файл
        """
        if all(isinstance(vacancy, dict) for vacancy in vacancies_list):
            vacancies_list_only_dict = [vacancy for vacancy in vacancies_list if isinstance(vacancy, dict)]
            extend_list = cls.load_from_file() + vacancies_list_only_dict
            with open(cls.file_name, "w", encoding="utf-8") as file:
                json.dump(extend_list, file, ensure_ascii=False, indent=4)  # type: ignore
        elif all(isinstance(vacancy, Vacancy) for vacancy in vacancies_list):
            vacancies_list_only_vacancies = [vacancy for vacancy in vacancies_list if isinstance(vacancy, Vacancy)]
            cls.vacancies_list_dict = cls.obj_vacancy_to_list(vacancies_list_only_vacancies)
            extend_list = cls.load_from_file() + cls.vacancies_list_dict
            with open(cls.file_name, "w", encoding="utf-8") as file:
                json.dump(extend_list, file, ensure_ascii=False, indent=4)  # type: ignore
        else:
            raise TypeError("Тип входных данных не соответствует требованиям")

    @classmethod
    def add_vacancy(cls, vacancy: "Vacancy") -> None:
        """
        Метод добавления вакансии в файл
        """
        data = cls.obj_vacancy_to_list([vacancy])[0]
        data_from_file = cls.load_from_file()
        data_from_file.append(data)
        cls.save_to_file_rw(data_from_file)

    @classmethod
    def delete_vacancy(cls, vacancy: "Vacancy") -> None:
        """
        Метод удаления вакансии из файла
        """
        data = cls.obj_vacancy_to_list([vacancy])[0]
        data_from_file = cls.load_from_file()
        try:
            data_from_file.remove(data)
        except ValueError:
            print("Элемент для удаления не найден")
        else:
            cls.save_to_file_rw(data_from_file)

    @classmethod
    def load_from_file(cls) -> List[Dict[str, Any]]:
        """
        Метод для загрузки данных из файла
        """
        try:
            with open(cls.file_name, "r", encoding="utf-8") as file:
                cls.vacancies_list = json.load(file)
        except json.decoder.JSONDecodeError:
            cls.vacancies_list = []
        except FileNotFoundError:
            cls.vacancies_list = []
        return cls.vacancies_list

    @classmethod
    def obj_vacancy_to_list(cls, vacancies_list: Sequence["Vacancy"]) -> List[Dict[str, Any]]:
        """
        Метод конвертации списка объектов Vacancy в список словарей
        """
        cls.vacancies_list_dict = []
        for vacancy in vacancies_list:
            cls.vacancies_list_dict.append(
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
        return cls.vacancies_list_dict
