from src.external_api_hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.utils import print_vacancies
from src.vacancies import Vacancy


def main() -> None:
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Инженер АСУ ТП")
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    vacancy = Vacancy("Вакансия", "https://url.url", 500000, "RUB", "Дрессировщик", "Ни чего не делать")
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    # json_saver.delete_vacancy(vacancy)
    json_saver.save_to_file_rw(vacancies_list)
    json_saver.save_to_file(hh_vacancies)
    # json_saver.add_vacancy(vacancy)
    data = json_saver.load_from_file()
    list_vacancies = Vacancy.cast_to_object_list(data)
    print_vacancies(list_vacancies)



if __name__ == "__main__":
    main()
