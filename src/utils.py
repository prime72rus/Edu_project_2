from typing import Sequence

from src.vacancies import Vacancy


def filter_vacancies(vacancies_list: Sequence["Vacancy"], filter_words: str) -> Sequence["Vacancy"]:
    """
    Фильтрация вакансий по ключевому слову описания
    """
    pass


def get_vacancies_by_salary(vacancies_list: Sequence["Vacancy"], salary_range: str) -> Sequence["Vacancy"]:
    """
    Фильтрация вакансий по зарплате
    """
    pass


def sort_vacancies(vacancies_list: Sequence["Vacancy"]) -> Sequence["Vacancy"]:
    """
    Сортировка вакансий
    """
    pass


def get_top_vacancies(vacancies_list: Sequence["Vacancy"], top_n: int) -> Sequence["Vacancy"]:
    """
    Получение ТОП-5 вакансий по зарплате
    """
    pass


def print_vacancies(vacancies_list: Sequence["Vacancy"]) -> None:
    """
    Вывод в консоль списка вакансий
    """
    if len(vacancies_list) > 0:
        for vacancy in vacancies_list:
            print(vacancy, "\n")
    else:
        print("Список вакансий пуст")