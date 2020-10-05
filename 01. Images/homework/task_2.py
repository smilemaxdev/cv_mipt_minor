import cv2
import numpy as np

def find_roads(image: np.ndarray) -> tuple:
    
    """
    Функция определяющая количество и диапозон дорожек по характерному цвету разделителей

    :param image: исходное изображение
    :return: координаты старта и конца дорожек
    """
    
    coords = np.where(image[0] == [255, 252, 121])[0]    # Найдем все пиксели в строке с характерным желтым цветом
    value  = coords[0]
    start  = []
    end    = []
    
    """
    Будем искать в полученных координатах характерные изменения в значениях для сепарации дорожек
    """
    for i in range(0, coords.shape[0] - 1):
        if coords[i] - value > 5:
            start.append(coords[i - 1])
            end.append(coords[i])
        value = coords[i]
        
    return (start, end)


def find_road_number(image: np.ndarray) -> int:
    """
    Найти номер дороги, на которой нет препятсвия в конце пути.

    :param image: исходное изображение
    :return: номер дороги, на котором нет препятсвия на дороге
    """
    start, end = find_roads(image)   # Найдем количество и диапозон дорожек
    
    road_number = None
    
    """
    В полученных диапозонах будем искать количество характерных красных объектов.
    Для устранения шумовых значений от границ дорожек будем рассматривать немного смещенную область
    """
    
    for x, y, i in zip(start, end, range(0, len(start))):
        
        if len(np.where( image[:, x + 20 : y - 20] == [255, 0, 0] )[2]) == 0:
            road_number = i

    return road_number