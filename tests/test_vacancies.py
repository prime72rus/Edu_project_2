from src.vacancies import Vacancy

def test_vacancy_creation():
    """Тест создания объекта Vacancy."""
    vacancy = Vacancy(
        name="Python Developer",
        url="https://example.com",
        salary=100000,
        currency="RUR",
        professional_roles="Backend",
        responsibility="Developing applications"
    )
    assert vacancy.name == "Python Developer"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary == 100000
    assert vacancy.currency == "RUR"
    assert vacancy.professional_roles == "Backend"
    assert vacancy.responsibility == "Developing applications"

def test_salary_validation():
    """Тест валидации зарплаты."""
    assert Vacancy.valid_salary(None) == 0
    assert Vacancy.valid_salary(50000) == 50000

def test_currency_validation():
    """Тест валидации валюты."""
    assert Vacancy.valid_currency(None) == "Не указано"
    assert Vacancy.valid_currency("USD") == "USD"

def test_string_representation():
    """Тест строкового представления объекта."""
    vacancy = Vacancy(
        name="Python Developer",
        url="https://example.com",
        salary=100000,
        currency="RUR",
        professional_roles="Backend",
        responsibility="Developing applications"
    )
    expected_output = (
        "Вакансия: Python Developer\n"
        "Url: https://example.com\n"
        "Зарплата: 100000 RUR\n"
        "Профессиональные роли: Backend\n"
        "Обязанности: Developing applications"
    )
    assert str(vacancy) == expected_output

def test_cast_to_object_list():
    """Тест метода cast_to_object_list."""
    data = [
        {
            "name": "Python Developer",
            "alternate_url": "https://example.com",
            "salary": {"from": 100000, "currency": "RUR"},
            "professional_roles": [{"name": "Backend"}],
            "snippet": {"responsibility": "Developing applications"}
        }
    ]
    vacancies = Vacancy.cast_to_object_list(data)
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].name == "Python Developer"
    assert vacancies[0].salary == 100000
    assert vacancies[0].currency == "RUR"
    assert vacancies[0].professional_roles == "Backend"
    assert vacancies[0].responsibility == "Developing applications"
