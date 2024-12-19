import sys

def min_moves(nums: list[int]) -> int:
    median = sorted(nums)[len(nums) // 2]    
    res = sum(abs(num - median) for num in nums)

    return res

def read_numbers(filename: str) -> list[int]:

    try:
        with open(filename, encoding='utf-8') as file:
            digits = [int(line.strip()) for line in file]
            return digits
        
    except FileNotFoundError:
        print(f'файл {filename} не найден')
        sys.exit(1)
    except ValueError:
        print('файл содержит некорректные данные')
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print('Нужно передать имя файла в качестве аргумента')
        sys.exit(1)

    filename = sys.argv[1]
    nums = read_numbers(filename)
    result = min_moves(nums)
    print(result)

if __name__ == '__main__':
    main()
