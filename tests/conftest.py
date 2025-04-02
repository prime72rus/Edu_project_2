import os

import pytest

from src.external_api_hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancies import Vacancy


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


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
def json_saver(tmp_path):
    """Фикстура для создания экземпляра JSONSaver с временным файлом"""
    test_file = str(tmp_path / "test_vacancies.json")
    saver = JSONSaver(test_file)
    yield saver
    if os.path.exists(test_file):
        os.remove(test_file)


@pytest.fixture
def sample_vacancy():
    """Фикстура для создания тестовой вакансии"""
    return Vacancy(
        name="Python Developer",
        url="https://example.com",
        salary=100000,
        currency="RUR",
        professional_roles="Developer, Backend",
        responsibility="Write code",
    )


@pytest.fixture
def sample_vacancy_dict():
    """Фикстура для создания тестового словаря вакансии"""
    return {
        "name": "Python Developer",
        "alternate_url": "https://example.com",
        "salary": {"from": 100000, "currency": "RUR"},
        "professional_roles": [{"name": "Developer"}, {"name": "Backend"}],
        "snippet": {"responsibility": "Write code"},
    }


@pytest.fixture
def vacancies_list():
    return [
        Vacancy("Python Dev", "https://example.com", 100000, "RUR", "Backend", "Developing applications"),
        Vacancy("Java Dev", "https://example.org", 150000, "USD", "Frontend", "Creating solutions"),
        Vacancy("C++ Dev", "https://example.net", 50000, "EUR", "Backend", "Code optimization"),
        Vacancy("Frontend Dev", "https://example.io", 120000, "RUR", "Frontend", "Developing UI"),
    ]
