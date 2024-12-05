# Utilizamos la imagen oficial de Python
FROM python:3.9.21-alpine3.20
# Dentro del contendor instalamos python, pip y flask con run, alpine utiliza el administrador de paquetes apk
RUN pip install flask
# Le decimos al contenedor que se ponga en el directorio app
WORKDIR /app
# copiamos nuestro proyecto a la carpta /app
COPY . .
# exponemos el puerto en el contenedor
EXPOSE 3000
#ejecutamos el servidor
CMD ["python", "src/app.py"]