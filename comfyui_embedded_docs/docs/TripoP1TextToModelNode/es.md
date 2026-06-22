# Tripo P1: Texto a Modelo

Este nodo genera un modelo 3D a partir de una descripción textual utilizando la API de Tripo P1. Está optimizado para crear mallas de baja poligonización listas para juegos, con topología estable, lo que lo hace adecuado para aplicaciones en tiempo real.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | La descripción textual del modelo 3D que deseas generar. | STRING | Sí | Hasta 1024 caracteres |
| `prompt_negativo` | Una descripción textual de lo que no deseas en el modelo generado. | STRING | No | Hasta 255 caracteres |
| `modo_de_salida` | Controla la calidad del modelo de salida y la configuración de texturas. Este parámetro es un diccionario con las siguientes claves:<br><br>`texture_quality`: STRING, Rango: `"standard"`<br>`pbr`: BOOLEAN, predeterminado: True<br>`texture`: BOOLEAN, predeterminado: True<br>`subdivision`: INT, predeterminado: 0, Rango: 0 a 2<br>`texture_size`: INT, predeterminado: 2048, Rango: 512 a 4096 (debe ser una potencia de 2)<br>`texture_format`: STRING, Rango: `"png"`<br>`texture_clean`: BOOLEAN, predeterminado: False<br>`texture_seamless`: BOOLEAN, predeterminado: False<br><br>Predeterminado: `{"texture_quality": "standard", "pbr": True, "texture": True, "subdivision": 0, "texture_size": 2048, "texture_format": "png", "texture_clean": False, "texture_seamless": False}` | DICT | Sí | Ver descripción |
| `semilla_imagen` | Un valor semilla para la generación de imágenes, utilizado para controlar la aleatoriedad. Predeterminado: 42. | INT | No |  |
| `límite_de_caras` | El número máximo de caras para la malla generada. Un valor de -1 significa sin límite. Predeterminado: -1. | INT | No |  |
| `semilla_modelo` | Un valor semilla para la generación del modelo, utilizado para controlar la aleatoriedad. | INT | No |  |
| `auto_escala` | Si está habilitado, el nodo determinará automáticamente el tamaño óptimo del modelo. Predeterminado: False. | BOOLEAN | No |  |
| `exportar_uv` | Si está habilitado, el modelo incluirá coordenadas UV para el mapeo de texturas. Predeterminado: True. | BOOLEAN | No |  |
| `comprimir_geometría` | Si está habilitado, la geometría se comprimirá para reducir el tamaño del archivo. Predeterminado: False. | BOOLEAN | No |  |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `id_tarea_modelo` | La ruta del archivo al modelo 3D generado (solo para compatibilidad hacia atrás). | STRING |
| `GLB` | El ID de tarea único para la solicitud de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `154e75209d65c823d5681b74cd12fe7b2ed37d7b94bf51cac86f343c68f85722`
