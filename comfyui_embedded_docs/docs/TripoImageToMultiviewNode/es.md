# TripoImageToMultiviewNode

Genera vistas frontal, izquierda, trasera y derecha del sujeto a partir de una única imagen de entrada, utilizando la API de Tripo. Esta es una tarea de pago que se factura aproximadamente a 0.10 USD. El nodo sube la imagen, espera a que finalice la tarea de generación de Tripo y luego devuelve las cuatro vistas junto con el ID de la tarea multivista.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | La imagen de origen del sujeto a partir de la cual Tripo genera las vistas frontal, izquierda, trasera y derecha. Se utiliza exactamente una imagen para la solicitud. | IMAGE | Sí | Single image |

Nota: El nodo llama a la API en la nube de Tripo y espera a que finalice la tarea de generación. Una tarea típica tarda alrededor de 25 segundos. La autenticación se gestiona automáticamente a través de las entradas ocultas del nodo, por lo que no es necesario proporcionar ninguna clave API de Tripo en el flujo de trabajo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `task_id de vistas múltiples` | El identificador de tarea devuelto por Tripo para la solicitud de generación de imágenes multivista. Es un identificador de cadena que puede utilizarse para hacer referencia a la tarea completada. | MULTIVIEW_TASK_ID |
| `frontal` | La vista frontal generada del sujeto. | IMAGE |
| `izquierda` | La vista lateral izquierda generada del sujeto. | IMAGE |
| `atrás` | La vista trasera generada del sujeto. | IMAGE |
| `derecha` | La vista lateral derecha generada del sujeto. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/es.md)

---
**Source fingerprint (SHA-256):** `3beca1feeb88aa080330e6867ffd7076bd45b2c52471d1bfacc71f66452211a5`
