import json

from src.external_api_hh import HeadHunterAPI


if __name__ == "__main__":
    vacancies = HeadHunterAPI()
    vacancies.load_vacancies("Developer")
    print(json.dumps(vacancies.vacancies[:3], ensure_ascii=False, indent=4))