# Факультатив "Введение в компьютерное зрение"

**Описание:** Вы когда-нибудь задумывались, как роботы могут ориентироваться в пространстве и выполнять свои задачи, как поисковые системы могут индексировать миллиарды изображений и видео, как алгоритмы могут диагностировать медицинские изображения на предмет заболеваний, как автомобили с автоматическим управлением могут видеть и управлять автомобилем безопасно, или как Instagram создает фильтры?

В основе этих современных приложений ИИ лежат технологии компьютерного зрения, которые могут воспринимать, понимать и реконструировать сложный визуальный мир. Computer Vision – одна из самых быстрорастущих и захватывающих дисциплин искусственного интеллекта в современной академии и промышленности. Курс предназначен для того, чтобы познакомить студентов с постановками основных задач и основополагающих принципов на примерах частей реальных кейсов. В рамках программы будут рассмотрены классические подходы Computer Vison, знание которых является неотъемлемой частью и основой Computer Vision in Deep Learning.

**Продолжительность:** 1 семестр.

**Интенсивность занятий:** 1-2 пары в неделю.

**Содержание:** Классические методы обработки изображений, решение задач: классификации, распознавания и оценки параметров движения в видеопотоке.

**Что нужно знать и уметь:** владеть Python (numpy, matplotlib), элементы линейной алгебры, математического анализа, статистики.

Курс основан на материалах [CS131](https://github.com/StanfordVL/CS131_release)


# Программа курса:

00. [Вводное занятие:](https://github.com/ml-dafe/cv_mipt_minor/tree/master/00.%20Introduction)
	- введение в область Computer vision;
	- основные задачи и направления.

01. [Формирование изображений. Основные понятия:](https://github.com/ml-dafe/cv_mipt_minor/tree/master/01.%20Images)
	- представление изображений в компьютере;
	- работа с цветом;
	- аффинные преобразования;
	- знакомство с библиотеками cv2, skimage;
	- [домашнее задание](https://github.com/ml-dafe/cv_mipt_minor/tree/master/01.%20Images/homework).

02. [Введение в обработку сигналов:](https://github.com/ml-dafe/cv_mipt_minor/tree/master/02.%20Signal%20processing)
	- частотная область, преобразование Фурье;
	- спектральный анализ;
	- свертки, фильтры;
	- кросс-корреляция;
	- [домашнее задание](https://github.com/ml-dafe/cv_mipt_minor/tree/master/02.%20Signal%20processing/homework).

03. [Введение в обработку изображений:]()
	- гистограммы изображений;
	- цветовая коррекция;
	- пороговое выделение;
	- морфологические операции;
	- пирамиды изображений;
	- [домашнее задание]().

04. [Глобальные признаки изображений:]()
	- выделение границ и контуров;
	- характеристики контуров;
	- матрица смежности;
	- метрики качества изображений;
	- [домашнее задание]().

05. [Введение в машинное обучение:]()
	- линейные модели.

06. [Введение в машинное обучение:]()
	- SVM;
	- деревья;
	- boosting;
	- [домашнее задание]().

07. [Локальные признаки изображений:]()
	- локализация особых точек (Harris, Chi-Tomasi);	
	- дескрипторы особых точек (SIFT, SURF, ORB);
	- [домашнее задание]().

08. [Параметрические модели:]()
	- RANSAC;
	- Преобразования Хафа для поиска форм;
	- Пайплайн для сшивки изображений на базе RANSAC и SIFT;
	- [домашнее задание]().

09. [Задача сегментации и кластеризации:]()
	- постановка задачи;
	- метрики качества: IoU, GIoU;
	- supervised methods (snakes, random walker);
	- Unsupervised methods (Simple Linear Iterative Clustering (SLIC), Felzenszwalb);
	- [домашнее задание]().

10. [Задача классификации:]()
	- постановка задачи;
	- метрики качества;
	- методы решения;
	- [домашнее задание]().

11. [Задача обнаружения объектов:]()
	- Метод "Мешка слов";
	- формат Pascal VOCl
	- Метрика качества AP;
	- [домашнее задание]().

12. [Обработка оптических потоков:]()
	- оптические потоки;
	- фильтр калмана;
	- задача оценки параметров движения в оптическом потоке;
	- задача сопровождения объектов в оптическом потоке.


## Перечень библиотек

Можно взять [`requirements.txt`](https://github.com/ml-dafe/cv_mipt_minor/blob/master/requirements.txt) из репозитория или установить следующие пакеты:

| **Requirements** |
| :-- |
| `jupyter`        |
| `matplotlib`     |
| `cv2 (4.2)`      | 
| `skimage`        |
| `numpy`          |