# 🧾 Sistema de Facturación

Aplicación web desarrollada en Django para la gestión de clientes, productos y facturación, diseñada para facilitar el control de ventas y el manejo básico de inventario en un negocio.

---

## 🚀 Características principales

* 🔐 Autenticación de usuarios (login y logout)
* 👥 Gestión de clientes (CRUD)
* 📦 Gestión de productos (CRUD)
* 🧾 Creación y administración de facturas
* 💰 Cálculo automático de totales
* 📊 Dashboard con métricas del negocio
* ⚠️ Alerta de productos con bajo stock
* 🎨 Interfaz moderna con Bootstrap

---

## 🛠️ Tecnologías utilizadas

* Python
* Django
* HTML5
* CSS3
* Bootstrap 5
* SQLite (base de datos por defecto)

---

## 📊 Dashboard

El sistema cuenta con un panel de control donde se visualiza:

* Total facturado
* Número de facturas
* Total de clientes
* Ventas del día
* Productos con bajo stock

---

## ⚙️ Instalación y ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

```bash
# Clonar el repositorio
git clone https://github.com/esteban4012/django-facturacion-app.git

# Entrar al proyecto
cd django-facturacion-app

# Crear entorno virtual
python -m venv env

# Activar entorno
env\Scripts\activate   # Windows

# Instalar requirements.txt
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

Luego abre en el navegador:

```
http://127.0.0.1:8000/
```

---

## 🔐 Acceso al sistema

Puedes acceder con el usuario creado mediante `createsuperuser` o crear usuarios desde el panel de administración:

```
http://127.0.0.1:8000/admin/
```

---

## 📁 Estructura del proyecto

El sistema está organizado en aplicaciones Django para manejar:

* Clientes
* Productos
* Facturación

---

## 🎯 Objetivo del proyecto

Este proyecto fue desarrollado como práctica para fortalecer habilidades en desarrollo web con Django, aplicando conceptos como:

* Arquitectura MVT
* Manejo de bases de datos
* Autenticación de usuarios
* Buenas prácticas de UI/UX

---

## 💼 Autor

**Esteban Agudelo**

Desarrollador en formación enfocado en desarrollo web con Python y Django.

---

## 📌 Estado del proyecto

✅ Funcional
🚧 En mejora continua

---

## ⭐ Notas

Este proyecto puede escalarse a:

* Sistema multiusuario por empresa
* Roles y permisos
* Deploy en la nube
* Integración con pagos

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes hacer un fork del proyecto y enviar un pull request.

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.
