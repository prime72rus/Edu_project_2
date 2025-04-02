import pytest

from src.utils import (
    filter_vacancies,
    get_salary_range,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)


def test_filter_vacancies(vacancies_list):
    """
    Тесты для filter_vacancies
    """
    filtered = filter_vacancies(vacancies_list, "developing")
    assert len(filtered) == 2
    assert filtered[0].name == "Python Dev"
    assert filtered[1].name == "Frontend Dev"

    filtered_empty = filter_vacancies(vacancies_list, "")
    assert len(filtered_empty) == 4

    filtered_empty = filter_vacancies(vacancies_list, "failed_filter_words")
    assert len(filtered_empty) == 0


def test_get_salary_range():
    """
    Тесты для get_salary_range
    """
    salary_range = "100 - 500"
    start, end = get_salary_range(salary_range)
    assert start == "100"
    assert end == "500"

    with pytest.raises(ValueError):
        get_salary_range("invalid input")


def test_get_vacancies_by_salary(vacancies_list):
    """
    Тесты для get_vacancies_by_salary
    """
    filtered = get_vacancies_by_salary(vacancies_list, "60000 - 160000")
    assert len(filtered) == 3
    assert filtered[0].name == "Python Dev"

    filtered_empty = get_vacancies_by_salary(vacancies_list, "200000 - 300000")
    assert len(filtered_empty) == 0


def test_sort_vacancies(vacancies_list):
    """
    Тесты для sort_vacancies
    """
    sorted_vacancies = sort_vacancies(vacancies_list)
    assert sorted_vacancies[0].name == "Java Dev"
    assert sorted_vacancies[-1].name == "C++ Dev"


def test_sort_vacancies_empty_list():
    """
    Тест сортировки пустого списка
    """
    sorted_vacancies = sort_vacancies([])
    assert len(sorted_vacancies) == 0


def test_get_top_vacancies(vacancies_list):
    """
    Тесты для get_top_vacancies
    """
    top_vacancies = get_top_vacancies(vacancies_list, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].name == "Java Dev"
    assert top_vacancies[1].name == "Frontend Dev"


def test_print_vacancies(capsys, vacancies_list):
    """
    Тесты для print_vacancies
    """
    print_vacancies(vacancies_list)
    captured = capsys.readouterr()
    assert "Python Dev" in captured.out
    assert "Список вакансий пуст" not in captured.out

    print_vacancies([])
    captured = capsys.readouterr()
    assert "Список вакансий пуст" in captured.out
