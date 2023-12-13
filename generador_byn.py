import cv2
import numpy as np

def img_bn(df ,name_image):
    ancho, altura = 4368, 2912
    
    #crea imagen en blanco con altura y ancho de la imagen de entrada
    blank_image = np.zeros((altura, ancho, 3), np.uint8)

    for row in df.itertuples(index=False):
        x = row.x
        y = row.y
        blank_image[x, y] = [255, 255, 255]# Cambia un píxel a blanco
    
    cv2.imwrite(name_image + "-seg.jpg", blank_image)    
    ventana = input("Presione '1' si desea abrir la imagen segmentada en una ventana nueva\n o presione'ctr + z' para salir del programa: ")
    if(ventana == 1):
        cv2.imshow(name_image + "-seg", blank_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
