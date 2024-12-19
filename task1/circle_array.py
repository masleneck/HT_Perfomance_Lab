import sys

def circle_array(arr: list[int], n: int, m: int) -> str:
    res = []  
    index = 0  

    for _ in range(n):
        res.append(arr[index])
        index = (index + m - 1) % n

    return ''.join(map(str, res))  

def main():
    if len(sys.argv) != 3:
        print('на вход подаются только 2 аргумента через пробел: python circle_array.py <n> <m>')
        sys.exit(1)
    try:
        n, m = int(sys.argv[1]), int(sys.argv[2])  
    except ValueError:
        print('ожидаются целые числа для n и m.')
        sys.exit(1)

    if n < 1 or m < 1:
        print('ожидается n >= 1 и m >= 1')
        sys.exit(1)

    array = [i for i in range(1, n + 1)]

    result = (circle_array(array, n, m))
    print(result)

if __name__ == '__main__':
    main()