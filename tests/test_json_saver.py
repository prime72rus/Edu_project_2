import json
from pathlib import Path

from src.json_saver import JSONSaver
from src.vacancies import Vacancy


def test_save_to_file_rw(create_vacancy_1, create_vacancy_2, setup_test_file):
    """
    Тест сохранения данных в файл с перезаписью
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file
    vacancies = [create_vacancy_1, create_vacancy_2]
    JSONSaver.save_to_file_rw(vacancies)
    assert test_file.exists()
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 2
    assert data[0]["name"] == "Python Dev"
    assert data[1]["name"] == "Java Dev"


def test_add_vacancy(create_vacancy_1, setup_test_file):
    """
    Тест добавления вакансии
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file
    JSONSaver.add_vacancy(create_vacancy_1)
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]["name"] == "Python Dev"


def test_delete_vacancy(create_vacancy_1, setup_test_file):
    """
    Тест удаления вакансии
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file
    JSONSaver.add_vacancy(create_vacancy_1)
    JSONSaver.delete_vacancy(create_vacancy_1)
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 0


def test_delete_vacancy_value_error(create_data, setup_test_file):
    """
    Тест удаления несуществующей вакансии
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    with open(test_file, "w", encoding="utf-8") as file:
        json.dump(create_data, file, ensure_ascii=False, indent=4)  # type: ignore

    non_existent_vacancy = Vacancy(
        name="C++ Dev",
        url="https://example.net",
        salary=150000,
        currency="EUR",
        professional_roles="Backend",
        responsibility="Code",
    )

    try:
        JSONSaver.delete_vacancy(non_existent_vacancy)
    except ValueError:
        assert False

    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 2
    assert data[0]["name"] == "Python Dev"
    assert data[1]["name"] == "Java Dev"


def test_load_from_file(create_data, setup_test_file):
    """
    Тест загрузки данных из файла
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    with open(test_file, "w", encoding="utf-8") as file:
        json.dump(create_data, file, ensure_ascii=False, indent=4)  # type: ignore
    loaded_data = JSONSaver.load_from_file()
    assert len(loaded_data) == 2
    assert loaded_data[0]["name"] == "Python Dev"
    assert loaded_data[1]["name"] == "Java Dev"


def test_load_from_file_invalid_json(setup_test_file):
    """
    Тест загрузки данных из файла с некорректным JSON
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    with open(test_file, "w", encoding="utf-8") as file:
        file.write("invalid_json_data")

    loaded_data = JSONSaver.load_from_file()
    assert isinstance(loaded_data, list)
    assert len(loaded_data) == 0


def test_save_to_file_success(create_vacancy_1, create_vacancy_2, setup_test_file):
    """
    Тест успешного добавления данных в файл
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    JSONSaver.save_to_file([create_vacancy_1, create_vacancy_2])

    assert test_file.exists()
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 2
    assert data[0]["name"] == "Python Dev"
    assert data[1]["name"] == "Java Dev"


def test_save_to_file_with_empty_list(setup_test_file):
    """
    Тест добавления пустого списка в файл
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    JSONSaver.save_to_file([])

    assert test_file.exists()
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 0


def test_save_to_file_invalid_data_type(setup_test_file):
    """
    Тест обработки исключения при некорректном типе данных
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    invalid_data = [123, "string", None]
    try:
        JSONSaver.save_to_file(invalid_data)  # type: ignore
    except TypeError as e:
        assert str(e) == "Тип входных данных не соответствует требованиям"
    else:
        assert False


def test_save_to_file_rw_invalid_data_type(setup_test_file):
    """
    Тест обработки исключения при некорректном типе данных
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    invalid_data = [123, "string", None]
    try:
        JSONSaver.save_to_file_rw(invalid_data)  # type: ignore
    except TypeError as e:
        assert str(e) == "Тип входных данных не соответствует требованиям"
    else:
        assert False


def test_save_to_file_nonexistent_file(create_vacancy_1):
    """
    Тест создания нового файла при его отсутствии
    """
    test_file = Path("nonexistent_file.json")
    JSONSaver.file_name = test_file

    if test_file.exists():
        test_file.unlink()

    JSONSaver.save_to_file([create_vacancy_1])

    assert test_file.exists()

    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]["name"] == "Python Dev"

    test_file.unlink()


def test_save_to_file_existing_data(create_vacancy_1, setup_test_file):
    """
    Тест добавления данных в существующий файл
    """
    test_file = setup_test_file
    JSONSaver.file_name = test_file

    initial_data = [
        {
            "name": "Initial Vacancy",
            "alternate_url": "https://example.com",
            "salary": {"from": 50000, "currency": "RUR"},
        }
    ]
    with open(test_file, "w", encoding="utf-8") as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=4)  # type: ignore

    JSONSaver.save_to_file([create_vacancy_1])

    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 2
    assert data[0]["name"] == "Initial Vacancy"
    assert data[1]["name"] == "Python Dev"
