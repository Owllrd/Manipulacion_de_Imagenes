from PIL  import  Image
from PIL import ImageFilter #Modulo de filtros

try:
	img = Image.open("image/im2.jpg") #abre la imagen, recibe la ruta 

	#print(img.mode) #devuelve en que modo vectorial esta la imagen

	#print(img.getpixel( (100,200) )) #Muestra los colores de los pixeles

	#img.convert("L") #Cambia la imagen a vlanco y negro

	#img = img.rotate(40, expand = True) #rota la imagen, 
	#recibe cuantos grados se va a rotar, expand, modifica el tamano de la imagen

	#img.save("image/news/im2.jpg") #Guarda la imagen en el disco, recibe la ruta

	#print(img.size) #obtener el tamano de la imagen


	#img = img.resize( (100,200) ) #Redimenciona la imagen, recibe una tupla con ancho, alto

	#box = (300,100,400,900) 

	#img = img.crop(box) #Extrae la porcion de una imagen 

	#img = img.filter(ImageFilter.BLUR) #aplica un filtro que se encuentre dentro de la libreria

	copy = im.resize(  (100,200)  )
	img.paste(copy,  (100,200)   ) #copia una imagen, en este caso dentro de si misma

	img.show() #abre la imagen 
except IOError:
	print("No es posible abrir la imagen")
