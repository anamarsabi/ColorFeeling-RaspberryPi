from SimpleCV import Camera, Display, Image, Color
import sys
import time
from sense_hat import SenseHat


cam = Camera()
display = Display()


#coge las imagenes que va tomando la camara
while display.isNotDone():
    #captura la imagen y guarda la imagen en el objeto img
    img = cam.getImage()

    #BUSCA LAS COORDENADAS DE LOS COLORES, EN LA EJECUCION NORMAL DEL PROGRAMA DEBE DE ESTAR COMENTADO
    #pixel = img.getPixel(img.width/2 , img.height/2)

    #print pixel


    # ********** COLOR AZUL*************

    #analiza el color de img
    blue_distance = img.colorDistance((120,140,130)).invert()

    #blue_distance.save(display)

    #toma el pixel del centro de la imagen
    pixel = blue_distance.getPixel(img.width/2 , img.height/2)

    #print pixel


    #Veamos si es AZUL
    if pixel[0] > 200:
        print "Veo color azul"

        X = (0, 128, 128)
        O = (255, 255, 0)

        Smilyface = [
            O, O, O, O, O, O, O, O,
            O, O, X, O, O, X, O, O,
            O, O, X, O, O, X, O, O,
            O, O, O, O, O, O, O, O,
            O, X, O, O, O, O, X, O,
            O, O, X, O, O, X, O, O,
            O, O, O, X, X, O, O, O,
            O, O, O, O, O, O, O, O
        ]
        sense = SenseHat()

        sense.set_pixels(Smilyface)

        time.sleep(2)


    else :
        print "no veo azul"

        X = (0, 128, 128)
        O = (255, 255, 255)

        BLANCO = [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O
        ]
        sense = SenseHat()

        sense.set_pixels(BLANCO)



    # ********** COLOR ROJO*************

    #analiza el color de img
    red_distance = img.colorDistance((235,100,45)).invert()

    #red_distance.save(display)

    #toma el pixel del centro de la imagen
    pixel = red_distance.getPixel(img.width/2 , img.height/2)

    #print pixel


    #Veamos si es ROJO
    if pixel[0] > 200:
        print "Veo color rojo"

        X = (255, 0, 0)
        O = (255, 255, 255)

        XD= [
            O, O, O, O, O, O, O, O,
            O, O, X, O, O, X, O, O,
            O, O, X, O, O, X, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, X, X, X, X, X, X, O,
            O, X, O, O, O, O, X, O,
            O, O, X, X, X, X, O, O
        ]
        sense = SenseHat()

        sense.set_pixels(XD)

        time.sleep(2)

    else :
        print "no veo rojo"

        sense = SenseHat()

        sense.set_pixels(BLANCO)

# ********** COLOR VERDE*************

    #analiza el color de img
    green_distance = img.colorDistance((95,110,85)).invert()

    #green_distance.save(display)

    #toma el pixel del centro de la imagen
    pixel = green_distance.getPixel(img.width/2 , img.height/2)


    #EN LA EJECUCION NORMAL DEL PROGRAMA DEBE ESTAR COMENTADO
    #print pixel


    #Veamos si es VERDE
    if pixel[0] > 200:
        print "Veo color verde"

        X = (0, 255, 0)
        O = (255, 255, 255)

        MEH= [
            O, O, O, O, O, O, O, O,
            O, X, X, O, O, X, X, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, X, X, X, X, X, X, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O
        ]
        sense = SenseHat()

        sense.set_pixels(MEH)

        time.sleep(2)

    else :
        print "no veo verde"
        X = (0, 255, 0)
        O = (255, 255, 255)

        BLANCO= [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O
        ]
        sense = SenseHat()

        sense.set_pixels(BLANCO)
