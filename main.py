from Analizar_pixeles import analizar_pixeles
from Cobertura_nubos import cci
from CloudCoverage import determinar_nube
from Imagen_byn import img_bn 
from Verifica_imagen import verificar_img

def main():
    try:
        entrada = input("Introduzca unicamemte el archivo JPEG a analizar puede añadir la bandera '-s' si lo desea:\n ")
        entrada_dividida = entrada.split()
        bandera_s = "-S" in entrada_dividida or "-s" in entrada_dividida
        nombre_imagen = entrada_dividida[0]
        ruta = "imagenes/" + nombre_imagen
        if verificar_img(ruta):
            dataPrueba = analizar_pixeles(ruta)
            data_nube = determinar_nube(dataPrueba)
            nombre_solo = nombre_imagen.split('.')[0]

            print(f"\nEl indice de cobertura nubosa en {nombre_imagen} es: {cci(data_nube, dataPrueba)}\n")

            if bandera_s:
                img_bn(data_nube, nombre_solo)
        else:
            print("La imagen no cuenta con alguna de las características solicitadas para analizar una imagen.")
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {e}\n")

if __name__ == "__main__":
  main()