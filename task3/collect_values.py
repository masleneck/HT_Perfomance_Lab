import sys
import json
import copy

def load_json(file : str) -> dict[str, any]:
    try:
        with open(file, encoding='utf-8') as r_file:
            return json.load(r_file)
    except FileNotFoundError:
        print(f'файл {file} не найден.')
        sys.exit(1)

def save_json(file : str, data : dict[str, any]) -> None:
    try:
        with open(file, 'w', encoding='utf-8') as w_file:
            json.dump(data, w_file, indent= 2, ensure_ascii= False)
    except Exception as name_file:
        print(f'ошибка при записи в файл {file}: {name_file}')
        sys.exit(1)

def collect_values(tests : list[dict[str, any]], values_dict : dict[int, str]) -> list[dict[str, any]]:
    result = []
    for test in tests:
        res = copy.deepcopy(test)
        test_id = test['id']
        if test_id in values_dict:
            res['value'] = values_dict[test_id]
        if 'values' in test:
            res['value'] = collect_values(test['values'], values_dict)
        result.append(res)
    return result

def main():
    if len(sys.argv) != 4:
        print('введите корректные значения: python collect_values.py <values.json> <tests.json> <report.json>')
        sys.exit(1)
    values, tests, report = sys.argv[1], sys.argv[2], sys.argv[3]
    values, tests = load_json(values), load_json(tests)
    
    values_dict = {i['id']: i['value'] for i in values['values']}
    # print(values_dict)
    update_res = collect_values(tests['tests'], values_dict)
    # print(*update_res)
    save_json(report, update_res)

if __name__ == '__main__':
    main()
