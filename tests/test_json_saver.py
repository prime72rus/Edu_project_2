import json
from pathlib import Path
from src.json_saver import JSONSaver
from src.vacancies import Vacancy

def setup_test_file():
    """Создание временного файла для тестов."""
    test_file = Path("test_vacancies.json")
    if test_file.exists():
        test_file.unlink()
    return test_file

def test_save_to_file_rw():
    """Тест сохранения данных в файл с перезаписью."""
    test_file = setup_test_file()
    JSONSaver.file_name = test_file
    vacancies = [
        Vacancy("Python Dev", "https://example.com", 100000, "RUR", "Backend", "Code"),
        Vacancy("Java Dev", "https://example.org", 120000, "USD", "Frontend", "Design")
    ]
    JSONSaver.save_to_file_rw(vacancies)
    assert test_file.exists()
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 2
    assert data[0]["name"] == "Python Dev"
    assert data[1]["name"] == "Java Dev"

def test_add_vacancy():
    """Тест добавления вакансии."""
    test_file = setup_test_file()
    JSONSaver.file_name = test_file
    vacancy = Vacancy("Python Dev", "https://example.com", 100000, "RUR", "Backend", "Code")
    JSONSaver.add_vacancy(vacancy)
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]["name"] == "Python Dev"

def test_delete_vacancy():
    """Тест удаления вакансии."""
    test_file = setup_test_file()
    JSONSaver.file_name = test_file
    vacancy = Vacancy("Python Dev", "https://example.com", 100000, "RUR", "Backend", "Code")
    JSONSaver.add_vacancy(vacancy)
    JSONSaver.delete_vacancy(vacancy)
    with open(test_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 0

def test_load_from_file():
    """Тест загрузки данных из файла."""
    test_file = setup_test_file()
    JSONSaver.file_name = test_file
    data_to_save = [
        {"name": "Python Dev", "alternate_url": "https://example.com", "salary": {"from": 100000, "currency": "RUR"}},
        {"name": "Java Dev", "alternate_url": "https://example.org", "salary": {"from": 120000, "currency": "USD"}}
    ]
    with open(test_file, "w", encoding="utf-8") as file:
        json.dump(data_to_save, file, ensure_ascii=False, indent=4)  # type: ignore
    loaded_data = JSONSaver.load_from_file()
    assert len(loaded_data) == 2
    assert loaded_data[0]["name"] == "Python Dev"
    assert loaded_data[1]["name"] == "Java Dev"
