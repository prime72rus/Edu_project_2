from src.external_api_hh import HeadHunterAPI
from src.vacancies import Vacancy


def main() -> None:
    vacancies = HeadHunterAPI()
    list_vacancies = vacancies.get_vacancies("Инженер АСУ ТП")
    # data = json.dumps(vacancies.vacancies[0], ensure_ascii=False, indent=4)
    # data = vacancies.vacancies[0]
    # print(data)
    # vac1 = Vacancy(data)
    # print(vac1)
    list_data = Vacancy.cast_to_object_list(list_vacancies)
    print(list_data[0].salary)
    print(list_data[1].salary)
    print(list_data[0] > list_data[1])
    print(list_data[0] < list_data[1])
    print(list_data[0] >= list_data[1])
    print(list_data[0] <= list_data[1])
    print(list_data[0] == list_data[1])
    print(list_data[0] != list_data[1])


if __name__ == "__main__":
    main()
