from PIL import Image
import os


def verificar_img(imageFile):
   # ruta = "imagenes/" + imageFile
    imagen = Image.open(imageFile)
    if imagen.format == "JPEG":
        tamaño_bytes = os.path.getsize(imageFile)
        tamaño_mb = tamaño_bytes / (1024 * 1024)
        if(3<=tamaño_mb<=32):
            ancho, alto = imagen.size
            if 4268 <= ancho <= 4468:
                if 2812 <= alto <= 3012:
                    return True
                else:
                    return False
            else:
                return False 
        else:
            return False
    else:
        return False
         