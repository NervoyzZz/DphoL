import cv2

def addEffect(pathIn, effect=0, power=1, pathOut='', show=False):
    """
    --------------------------------------------------------------------------------------
    addEffect(pathIn, effect=0, power=1, pathOut='', show=False)

    pathIn <str> - путь входного изображения
    effect <int> - номер необходимого эффекта
            0 - размытие (по умолчанию)
            1 - черно-белый фильтр
    power <int> - сила эффекта (работает не для всех эффектов)
            0 - предоставить ползунок
            1 - без эффекта(по умолчанию)
            2... - ?
    pathOut <str> - путь сохранения изображения с эффектом.
            '' - Если пустая то заменяется на значение pathIn.(по умолчанию) Не знаю можно ли сделать это здесь
    show <bool> - показывать ли результат в отдельном окне
            True - показать
            False - не показывать(по умолчанию)
    --------------------------------------------------------------------------------------
    """

    #Check variables types
    if type(pathIn) != str:
        raise IOError("Wrong type of pathIn")
    if type(effect) != int:
        raise IOError("Wrong type of effect")
    if type(power) != int:
        raise IOError("Wrong type of power")
    if type(pathOut) != str:
        raise IOError("Wrong type of pathOut")
    if type(show) != bool:
        raise IOError("Wrong type of show")

    if pathOut == '':
        pathOut = pathIn

    # import image from pathIn
    image = cv2.imread(pathIn)

    #Apply effect
    if effect == 0:
        image = cv2.blur(image, (power, power))
    elif effect == 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        raise IOError("Unknown filter: check variable 'effect'")

    #Save
    cv2.imwrite(pathOut, image)

    #Show
    if show == True:
        cv2.imshow("Image", image)
        cv2.waitKey(0)