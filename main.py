from src.external_api_hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancies import Vacancy


def main() -> None:
    vacancies = HeadHunterAPI()
    list_vacancies = vacancies.get_vacancies("Инженер АСУ ТП")
    list_data = Vacancy.cast_to_object_list(list_vacancies)
    json_saver = JSONSaver()
    # json_saver.save_to_file(list_vacancies)
    json_saver.save_to_file(list_data)
    vacancy = Vacancy("Вакансия", "https://url.url", 500000, "RUB", "Дрессировщик", "Ни чего не делать")
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)


if __name__ == "__main__":
    main()
