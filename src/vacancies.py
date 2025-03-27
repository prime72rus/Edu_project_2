from functools import total_ordering
from typing import Any, Dict, List, Optional


@total_ordering
class Vacancy:
    """
    Класс содержащий информацию о вакансии
    """

    def __init__(
        self, name: str, url: str, salary: int, currency: str, professional_role: str, responsibility: str
    ) -> None:
        """
        Конструктор класса Vacancy
        """
        self.name = name
        self.url = url
        self.salary = self.valid_salary(salary)
        self.currency = self.valid_currency(currency)
        self.professional_role = professional_role
        self.responsibility = responsibility

    @staticmethod
    def valid_salary(salary_data: Optional[int]) -> int:
        """
        Валидация данных о зарплате.
        Если зарплата не указана, возвращает 0.
        """
        if salary_data is None:
            return 0
        return salary_data

    @staticmethod
    def valid_currency(currency_name: Optional[str]) -> str:
        """
        Валидация данных о валюте.
        Если валюта не указана, возвращает "Не указано".
        """
        if currency_name is None:
            return "Не указано"
        return currency_name

    def __str__(self) -> str:
        """
        Строковое представление вакансии
        """
        return (
            f"Вакансия: {self.name}\n"
            f"Url: {self.url}\n"
            f"Зарплата: {self.salary} {self.currency}\n"
            f"Профессиональные роли: {self.professional_role}\n"
            f"Обязанности: {self.responsibility}"
        )

    @classmethod
    def cast_to_object_list(cls, vacancy_data: List[Dict[str, Any]]) -> list["Vacancy"]:
        """
        Метод создания списка объектов класса Vacancy из списка словарей вакансий.
        Пропускает элементы, которые равны None или содержат некорректные данные.
        """
        list_object_vacancies: List[Vacancy] = []
        for vacancy in vacancy_data:
            name = vacancy.get("name", "Не указано")
            url = vacancy.get("area", {}).get("url", "Не указано")
            salary_data = vacancy.get("salary", {})
            salary = cls.valid_salary(salary_data.get("from"))
            currency = cls.valid_currency(salary_data.get("currency"))
            professional_roles = vacancy.get("professional_roles", [])
            professional_role = " ".join(role.get("name", "Не указано") for role in professional_roles)
            responsibility = vacancy.get("snippet", {}).get("responsibility", "Не указано")

            list_object_vacancies.append(
                Vacancy(
                    name=name,
                    url=url,
                    salary=salary,
                    currency=currency,
                    professional_role=professional_role,
                    responsibility=responsibility,
                )
            )
        return list_object_vacancies

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary
