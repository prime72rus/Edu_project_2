from src.external_api_hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.utils import print_vacancies, sort_vacancies, get_top_vacancies, filter_vacancies, get_vacancies_by_salary
from src.vacancies import Vacancy


def main() -> None:
    vacancy = Vacancy("Java Dev", "https://example.org", 120000, "USD", "Frontend", "Design")
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ")
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    json_saver.save_to_file_rw(top_vacancies)


if __name__ == "__main__":
    main()
