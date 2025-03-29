from pathlib import Path

import pytest

from src.vacancies import Vacancy


@pytest.fixture
def create_vacancy_1():
    return Vacancy("Python Dev", "https://example.com", 100000, "RUR", "Backend", "Code")


@pytest.fixture
def create_vacancy_2():
    return Vacancy("Java Dev", "https://example.org", 120000, "USD", "Frontend", "Design")


@pytest.fixture
def create_data():
    return [
        {"name": "Python Dev", "alternate_url": "https://example.com", "salary": {"from": 100000, "currency": "RUR"}},
        {"name": "Java Dev", "alternate_url": "https://example.org", "salary": {"from": 120000, "currency": "USD"}},
    ]


@pytest.fixture
def setup_test_file():
    test_file = Path("test_vacancies.json")
    if test_file.exists():
        test_file.unlink()
    return test_file
