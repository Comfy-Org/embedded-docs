# Graficar Pérdida

El nodo LossGraphNode crea un gráfico visual de los valores de pérdida de entrenamiento a lo largo del tiempo y lo muestra como una imagen de vista previa. Toma datos de pérdida de procesos de entrenamiento y genera un gráfico de líneas que muestra cómo cambia la pérdida a lo largo de los pasos de entrenamiento. El gráfico resultante incluye etiquetas de ejes y los valores mínimos/máximos de pérdida.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `loss` | Mapa de pérdida del nodo de entrenamiento. Debe contener una clave `loss` con una lista de valores de pérdida utilizados para trazar el gráfico. | LOSS_MAP | Sí | - |
| `filename_prefix` | Prefijo para la imagen del gráfico de pérdida guardado. (predeterminado: "loss_graph") | STRING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
| --- | --- | --- |
| `ui.images` | La imagen del gráfico de pérdida generado, mostrada como vista previa. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/es.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
