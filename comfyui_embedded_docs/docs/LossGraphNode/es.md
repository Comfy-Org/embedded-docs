# Graficar Pérdida

El nodo LossGraphNode crea un gráfico de líneas de los valores de pérdida de entrenamiento a lo largo de los pasos de entrenamiento y lo muestra como una imagen de vista previa. Lee los valores de pérdida de un nodo de entrenamiento, los representa en un gráfico con ejes etiquetados y valores mínimo/máximo de pérdida, y devuelve el gráfico como una vista previa de imagen en la interfaz de usuario.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `pérdida` | Mapa de pérdida del nodo de entrenamiento. Debe contener una clave `loss` con una lista de valores numéricos de pérdida. | LOSS_MAP | Sí | - |
| `prefijo_nombre_archivo` | Prefijo para la imagen del gráfico de pérdida guardado. (predeterminado: "loss_graph") | STRING | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `ui.images` | La imagen del gráfico de pérdida generada que se muestra como vista previa. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/es.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
