import cv2
import argparse

def main(parser):
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

    #Import variables from parser
    pathIn = parser.pathIn
    effect = parser.effect
    power = parser.power
    pathOut = parser.pathOut
    show = parser.show

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
    if show:
        cv2.imshow("Image", image)
        cv2.waitKey()
        cv2.destroyAllWindows()

def args_parse():
    parcer = argparse.ArgumentParser()

    #parcer.add_argument('--pathIn',default='G:/Users/Ruslan/PycharmProjects/DphoL/py_demo/matrix-sunglasses.jpg',type=str)
    parcer.add_argument('--pathIn', type=str)

    parcer.add_argument('--effect','-e',    default=0, type=int)
    parcer.add_argument('--power','-p',     default=1, type=int)
    parcer.add_argument('--pathOut','-Out', default='', type=str)
    parcer.add_argument('--show','-s',      default=True, type=bool)
    return parcer.parse_args()

if __name__ == "__main__":
    main(args_parse())