import json
import os

import pytest

from src.json_saver import JSONSaver


def test_save_to_file_rw_with_dict(json_saver, sample_vacancy_dict):
    """
    Тест сохранения списка словарей с перезаписью
    """
    json_saver.save_to_file_rw([sample_vacancy_dict])
    with open(json_saver._JSONSaver__file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert data == [sample_vacancy_dict]


def test_save_to_file_rw_with_vacancies(json_saver, sample_vacancy):
    """
    Тест сохранения списка вакансий с перезаписью
    """
    json_saver.save_to_file_rw([sample_vacancy])
    with open(json_saver._JSONSaver__file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"


def test_save_to_file_rw_type_error(json_saver):
    """
    Тест вызова TypeError при неверном типе данных
    """
    with pytest.raises(TypeError):
        json_saver.save_to_file_rw(["invalid_data"])


def test_save_to_file_type_error(json_saver):
    """
    Тест вызова TypeError при неверном типе данных
    """
    with pytest.raises(TypeError):
        json_saver.save_to_file(["invalid_data"])


def test_save_to_file_dict(json_saver, sample_vacancy_dict):
    """
    Тест добавления данных в файл (словарь)
    """
    json_saver.save_to_file_rw([sample_vacancy_dict])

    new_vacancy = {
        "name": "Java Developer",
        "alternate_url": "https://example.com/java",
        "salary": {"from": 120000, "currency": "RUR"},
        "professional_roles": [{"name": "Developer"}],
        "snippet": {"responsibility": "Write Java code"},
    }
    json_saver.save_to_file([new_vacancy])

    with open(json_saver._JSONSaver__file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == "Python Developer"
    assert data[1]["name"] == "Java Developer"


def test_save_to_file_vacancy(json_saver, vacancies_list):
    """
    Тест добавления данных в файл (экземпляр класса Vacancy)
    """
    json_saver.save_to_file_rw(vacancies_list)

    json_saver.save_to_file(vacancies_list)

    with open(json_saver._JSONSaver__file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 8
    assert data[0]["name"] == "Python Dev"
    assert data[1]["name"] == "Java Dev"


def test_add_vacancy(json_saver, sample_vacancy):
    """
    Тест добавления одной вакансии
    """
    json_saver.add_vacancy(sample_vacancy)
    data = json_saver.load_from_file()
    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"


def test_delete_vacancy(json_saver, sample_vacancy):
    """
    Тест удаления вакансии
    """
    json_saver.add_vacancy(sample_vacancy)
    data = json_saver.load_from_file()
    assert len(data) == 1

    json_saver.delete_vacancy(sample_vacancy)
    data = json_saver.load_from_file()
    assert len(data) == 0


def test_delete_nonexistent_vacancy(json_saver, sample_vacancy, capsys):
    """
    Тест попытки удаления несуществующей вакансии
    """
    json_saver.delete_vacancy(sample_vacancy)
    captured = capsys.readouterr()
    assert "Элемент для удаления не найден" in captured.out


def test_load_from_file_empty(json_saver):
    """
    Тест загрузки из пустого файла
    """
    data = json_saver.load_from_file()
    assert data == []


def test_load_from_file_invalid_json(json_saver, tmp_path):
    """
    Тест обработки JSONDecodeError
    """
    invalid_json_file = str(tmp_path / "invalid.json")
    with open(invalid_json_file, "w", encoding="utf-8") as file:
        file.write("{invalid json}")

    saver = JSONSaver(invalid_json_file)
    result = saver.load_from_file()

    assert result == []


def test_load_from_file_non_existent(json_saver):
    """
    Тест загрузки из несуществующего файла
    """
    non_existent_file = "non_existent.json"
    saver = JSONSaver(non_existent_file)
    data = saver.load_from_file()
    assert data == []
    if os.path.exists(non_existent_file):
        os.remove(non_existent_file)


def test_obj_vacancy_to_list(json_saver, sample_vacancy):
    """
    Тест конвертации вакансий в список словарей
    """
    result = json_saver.obj_vacancy_to_list([sample_vacancy])
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["name"] == "Python Developer"
    assert result[0]["professional_roles"] == [{"name": "Developer"}, {"name": "Backend"}]
