> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/es.md)

El nodo LossGraphNode crea un gráfico visual de los valores de pérdida de entrenamiento a lo largo del tiempo y lo muestra como una imagen de vista previa. Toma datos de pérdida de procesos de entrenamiento y genera un gráfico de líneas que muestra cómo cambia la pérdida a través de los pasos de entrenamiento. El gráfico resultante incluye etiquetas en los ejes y los valores mínimo y máximo de pérdida.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `pérdida` | LOSS_MAP | Sí | - | Mapa de pérdida proveniente del nodo de entrenamiento. |
| `prefijo_nombre_archivo` | STRING | Sí | - | Prefijo para la imagen del gráfico de pérdida guardada. (valor predeterminado: "loss_graph") |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|-------------|-----------|-------------|
| `ui.images` | IMAGE | La imagen del gráfico de pérdida generado, mostrada como vista previa. |

---
**Source fingerprint (SHA-256):** `9b1c844cb4babafc61102ee7bfd1039c325c6665abff1721d92a6da7d18029f9`
