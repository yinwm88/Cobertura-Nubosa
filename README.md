<div align="center">

# **Cobertura Nubosa** #

</div>
<div>

  Es una calculadora para obtener el indice de cobertura nubosa(ICC) dada una imagen en formato JPEG de una boveda celeste, es decir calcula la   proporcion de la boveda celeste cubierta por nubes.

  Para la discriminación de pixeles se uso el metodo descrito en el articulo:
  > Roy, G., S. Hayman y W. Julian, "Sky analysis from CCD images: cloud cover", Lighting
Research Technology, Vol. 33, No. 4, pp. 211-222, 2001.
  
</div>


<div>
  
# **Usage**   

</div>

- Crear un entorno virtual
- Instalar las paqueterias del requirements.txt:
  ```
    pip install -r requirements.txt
  ```
- Clonar este repositorio:
  ```
   git clone https://github.com/yinwm88/Cobertura-Nubosa.git
  ```
- Entrar a la carpeta del repositorio clonado:
  ```
    git cd Cobertura-Nubosa
  ```
- Insertar en la carpeta imagenes la imagen de la foto del cielo tomada en una boveda celeste.
- Para calcular el ICC, corra en la terminal:
  ```
   python Calculadora/main.py
  ```
> Si proporciona la bandera -s, se generara una imagen en blanco y negro, donde los pixeles blancos representan las nubes y los negros el cielo.
