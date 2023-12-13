import numpy as np
import pandas as pd
import cv2


def analizar_pixeles(imagen):
    coordenada_x = []
    coordenada_y = []
    razon_blue_red = []
    
    imagen = cv2.imread(imagen)
    
    centro = (1456, 2184)
    radio = 1324
        
    for x in range(centro[0] - radio, centro[0] + radio):
        for y in range(centro[1] - radio, centro[1] + radio):
            distancia = np.sqrt((x - centro[0])**2 + (y - centro[1])**2)
            if distancia <= radio: 
               coordenada_x.append(x)
               coordenada_y.append(y)
               bgr = imagen[x, y]
               razon_blue_red.append(bgr[2]/bgr[0])
    
    df = pd.DataFrame({
        'x' : coordenada_x,
        'y' : coordenada_y,
        'razon' : razon_blue_red
    }) 
    return df