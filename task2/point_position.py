import sys

def point_position(center_x: float, center_y: float, radius: float, point_x: float, point_y: float) -> int:
    '''
    0 - точка лежит на окружности
    1 - точка внутри
    2 - точка снаружи
    '''
    sq_distance, sq_radius = (point_x - center_x) ** 2 + (point_y - center_y) ** 2, radius ** 2   
    if sq_distance < sq_radius:
        return 1
    elif sq_distance == sq_radius:
        return 0
    else:
        return 2

def main():
    try:
        with open(sys.argv[1], encoding='utf-8') as file_1:
            line_1 = file_1.readline().split()
            if len(line_1) == 2:
                center_x, center_y = float(line_1[0]), float(line_1[1])
            else:
                print('неверное количество данных в первой строке первого файла')
                return  
        
            line_2 = file_1.readline().split()
            if len(line_2) == 1:
                radius = float(line_2[0])
            else:
                print('неверное количество данных во второй строке первого файла')
                return  

        with open(sys.argv[2], encoding='utf-8') as file_2:
            line_count = sum(1 for line in file_2)
            file_2.seek(0)

            if line_count > 100:
                print('точек больше ста')
            else:
                for i, line in enumerate(file_2, start= 1):
                    points = line.split()
                    if len(points) == 2:
                        point_x, point_y = float(points[0]), float(points[1])

                        result = point_position(center_x, center_y, radius, point_x, point_y)
                        print(result)
                    else:
                        print(f'неверное количество данных в {i} строке второго файла')
                
    except FileNotFoundError as file_name:
        print(f'файл {file_name.filename} не найден')
    except ValueError:
        print('ошибка преобразования данных в числа')
    except Exception as file_name:
        print(f'ошибка при работе с файлом: {file_name}')

if __name__ == '__main__':
    main()
