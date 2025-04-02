import re
from typing import Sequence

from src.vacancies import Vacancy


def filter_vacancies(vacancies_list: Sequence["Vacancy"], filter_words: str) -> Sequence["Vacancy"]:
    """
    Фильтрация вакансий по ключевому слову описания
    """

    if not filter_words:
        return vacancies_list
    filter_words_to_list = filter_words.split()
    filtered_vacancies = [
        vacancy
        for vacancy in vacancies_list
        if any(keyword.lower() in vacancy.responsibility.lower() for keyword in filter_words_to_list)
    ]
    if len(filtered_vacancies) > 0:
        return filtered_vacancies
    else:
        return []


def get_salary_range(salary_range: str) -> tuple[str, str]:
    """
    Функция получения диапазона зарплат для фильтрации из пользовательского ввода
    """
    pattern = r"^(?:[^0]\d*|0) - [1-9]\d*$"
    result = re.fullmatch(pattern, salary_range)
    if result is None:
        raise ValueError("Введенная строка не соответствует шаблону ввода")
    else:
        start_range = salary_range.split(" - ")[0]
        end_range = salary_range.split(" - ")[1]
        return start_range, end_range


def get_vacancies_by_salary(vacancies_list: Sequence["Vacancy"], salary_range: str) -> Sequence["Vacancy"]:
    """
    Фильтрация вакансий по зарплате
    """
    start_range, end_range = get_salary_range(salary_range)
    filtered_vacancies = [
        vacancy for vacancy in vacancies_list if int(start_range) <= vacancy.salary <= int(end_range)
    ]
    if len(filtered_vacancies) > 0:
        return filtered_vacancies
    else:
        return []


def sort_vacancies(vacancies_list: Sequence["Vacancy"]) -> Sequence["Vacancy"]:
    """
    Сортировка вакансий по зарплате
    """
    if len(vacancies_list) > 0:
        return sorted(vacancies_list, key=lambda x: x.salary, reverse=True)
    else:
        return []


def get_top_vacancies(vacancies_list: Sequence["Vacancy"], top_n: int) -> Sequence["Vacancy"]:
    """
    Получение ТОП-5 вакансий по зарплате
    """
    return sort_vacancies(vacancies_list)[:top_n]


def print_vacancies(vacancies_list: Sequence["Vacancy"]) -> None:
    """
    Вывод в консоль списка вакансий
    """
    if len(vacancies_list) > 0:
        for vacancy in range(0, len(vacancies_list)):
            print(vacancies_list[vacancy], "\n")
    else:
        print("Список вакансий пуст")
