# Eliminar fondo

## Descripción general

El nodo Remove Background utiliza un modelo de eliminación de fondo para generar una máscara que separa el sujeto en primer plano del fondo de una imagen de entrada. Toma una imagen y un modelo de eliminación de fondo, y produce una máscara que resalta el sujeto principal.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | Imagen de entrada a la que se le eliminará el fondo | IMAGE | Sí | N/A |
| `modelo_de_eliminación_de_fondo` | Modelo de eliminación de fondo utilizado para generar la máscara | BACKGROUND_REMOVAL_MODEL | Sí | N/A |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `mask` | Máscara de primer plano generada que resalta el sujeto principal de la imagen de entrada | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/es.md)

---
**Source fingerprint (SHA-256):** `cd19134e6afed4d31096b613dd534eacad39afe7de2c8b74feab512bd5f09f66`
