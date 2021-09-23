import imageio
from imageio import imread, imwrite # It is possible using another python "picture-working" library
import DBScanModule as DBScan
from DBScanModule import Point

def MakeScan(nameOfPicture, eps, minPts):

    # Import picture in 3D array // Импорт изображения в трёхмерный массив
    img = imread('images\\' + nameOfPicture)

    #Creating set of Points (without white points) from 3D array
    # // Перевод из трёхмерного массива во множество (set) объектов Point, исключая белые пикселы
    points = set()  # Множество точек
    for i in range(img.shape[0]):
        for k in range(img.shape[1]):
            #Checking whiteness // Проверка на белый пиксель
            if (int(img[i, k, 0]) != 255 and int(img[i, k, 1]) != 255 and int(img[i, k, 2]) != 255):
                points.add(Point(i, k, img[i, k, 0], img[i, k, 1], img[i, k, 2]))

    # DBSCAN
    DBScan.Scan(points, eps, minPts)
    # Painting 3D array according to labels of points
    # // Согласно элементам из points "разукрашиваем" массив img
    for P in points:
        if P.label == 'Noise':
            img[P.x, P.y, 0] = 150
            img[P.x, P.y, 1] = 150
            img[P.x, P.y, 2] = 150
        elif (int(P.label) % 3 == 0):
            img[P.x, P.y, 0] = (int(P.label) * 150) % 255
            img[P.x, P.y, 1] = (int(P.label) * 150) % 10
            img[P.x, P.y, 2] = (int(P.label) * 150) % 5
        elif (int(P.label) % 3 == 1):
            img[P.x, P.y, 0] = (int(P.label) * 150) % 5
            img[P.x, P.y, 1] = (int(P.label) * 150) % 255
            img[P.x, P.y, 2] = (int(P.label) * 150) % 10
        else:
            img[P.x, P.y, 0] = (int(P.label) * 150) % 5
            img[P.x, P.y, 1] = (int(P.label) * 150) % 10
            img[P.x, P.y, 2] = (int(P.label) * 150) % 255

        # if P.label == '1':
        #     img[P.x, P.y, 0] = 255
        #     img[P.x, P.y, 1] = 0
        #     img[P.x, P.y, 2] = 0
        # if P.label == '2':
        #     img[P.x, P.y, 0] = 0
        #     img[P.x, P.y, 1] = 255
        #     img[P.x, P.y, 2] = 0
        # if P.label == '3':
        #     img[P.x, P.y, 0] = 0
        #     img[P.x, P.y, 1] = 0
        #     img[P.x, P.y, 2] = 255
        # if P.label == '4':
        #     img[P.x, P.y, 0] = 255
        #     img[P.x, P.y, 1] = 255
        #     img[P.x, P.y, 2] = 0
        # if P.label == '5':
        #     img[P.x, P.y, 0] = 255
        #     img[P.x, P.y, 1] = 0
        #     img[P.x, P.y, 2] = 255
        # if P.label == '6':
        #     img[P.x, P.y, 0] = 0
        #     img[P.x, P.y, 1] = 255
        #     img[P.x, P.y, 2] = 255

    # Writing a picture
    # // Запись в изображение
    imwrite(
        str('images\\{0}\\{1} Scanned (e{2} minpts{3}).png'.format(nameOfPicture[:4], nameOfPicture[:4], eps, minPts)),
        img)

nameOfPicture='lab10.png'
for eps in 10, 80, 160:
    for minPts in 10, 80, 160:
        MakeScan(nameOfPicture, eps, minPts)
        print('File {0} has scanned with eps = {1} and minPts = {2}'.format(nameOfPicture, eps, minPts))