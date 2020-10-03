import cv2
import numpy as np

def find_start(image: np.ndarray):
    x = [0, image.shape[0] - 1]
    y = [0, image.shape[1] - 1]
    start_end = []
    tmp_bound =  np.array([image[0], image[image.shape[0] - 1], image[:, 0], image[:, image.shape[1] - 1]])
    for bound, i in zip(tmp_bound, range(0, 4)):
        result = np.where(bound == 255)
        if len(result[0]) != 0:
            if i < 2:
                start_end.append([x[i], result[0][0]])
            else:
                start_end.append([result[0][0], y[i - 2]])
    return start_end[0], start_end[1]
            
def find_way_from_maze(image: np.ndarray) -> tuple:
    """
    Найти путь через лабиринт.

    :param image: изображение лабиринта
    :return: координаты пути из лабиринта в виде (x, y), где x и y - это массивы координат
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Для удобства будем работать с одноканальным изображением
    start, end = find_start(gray) # Найдем точку входа и выхода пройдя по границами изоборажения
    
    # Для решения задачи будем использовать алгоиртм Ли
    route = np.zeros((gray.shape)) # Зададим планарный граф по нашему изображению
    route[gray == 0] = -1 # Зададим непроходимым пикселям значение -1
    curr = 1 # Зададим стартовое значение
    can = True # Параметер характеризующий возможность распространения волны
    is_end = False
    route[start[0], start[1]] = 1 # Присвоим стартовой точке стартовое значение
    # Процесс распростанения волны, пока не конец или волна может расспространятся
    while not is_end or can:
        # Находим ячейки с текущим значением
        x,y = np.where(route == curr)
        curr = curr + 1
        can = False
        # Заполняем соседние
        for _x,_y in zip(x,y):
            
            if _x - 1 >= 0:
                if route[_x - 1, _y] == 0:
                    route[_x - 1, _y] = curr
                    can = True
                    
            if _x + 1 < route.shape[0]:
                if route[_x + 1, _y] == 0:
                    route[_x + 1, _y] = curr
                    can = True
                    
            if _y - 1 >= 0:
                if route[_x, _y - 1] == 0:
                    route[_x, _y - 1] = curr
                    can = True
                    
            if _y + 1 < route.shape[1]:
                if route[_x, _y + 1] == 0:
                    route[_x, _y + 1] = curr
                    can = True
            
            if _x == end[0] and _y == end[1]:
                is_end = True
    
    #Если достигнут конец, то строим обратный маршрут
    if is_end:
        way_x  = [end[0]]
        x,y = end
        way_y = [end[1]]
        value = route[x, y]
        while x != start[0] or y != start[1]:
            if x - 1 >= 0:
                if route[x - 1, y] == value - 1:
                    value = route[x - 1, y]
                    x = x - 1
                    
            if x + 1 < route.shape[0]:
                if route[x + 1, y] == value - 1:
                    value = route[x + 1, y]
                    x = x + 1
                    
            if y - 1 >= 0:
                if route[x, y - 1] == value - 1:
                    value = route[x, y - 1]
                    y = y - 1
                    
            if y + 1 < route.shape[1]:
                if route[x, y + 1] == value - 1:
                    value = route[x, y + 1]
                    y = y + 1
            way_x.append(x)
            way_y.append(y)
    else:
        return None

    return (way_x, way_y)