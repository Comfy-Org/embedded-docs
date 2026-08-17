# Inferencia panorámica MoGe

Este nodo realiza estimación de profundidad en imágenes de panorama equirectangular. Funciona dividiendo el panorama en 12 vistas en perspectiva, ejecutando el modelo de estimación de profundidad MoGe en cada vista y luego fusionando los resultados para obtener un único mapa de profundidad completo del panorama original.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `moge_model` | El modelo MoGe a utilizar para la inferencia. | MOGE_MODEL | Sí |  |
| `image` | Panorama equirectangular (cualquier relación de aspecto). Acepta solo una imagen. | IMAGE | Sí |  |
| `resolution_level` | Detalle por vista (0 = más rápido, 9 = más detallado). Predeterminado: 9. | INT | Sí | 0 a 9 |
| `split_resolution` | Resolución de cada división en perspectiva. Predeterminado: 512. | INT | Sí | 256 a 1024 |
| `merge_resolution` | Resolución del lado largo del mapa de distancia equirectangular fusionado. Predeterminado: 1920. | INT | Sí | 256 a 8192 |
| `batch_size` | Vistas por lote de inferencia (12 divisiones en total). Predeterminado: 4. | INT | Sí | 1 a 12 |

Nota: Este nodo acepta solo una imagen. Pasar un lote de imágenes genera un error. El panorama siempre se divide en 12 vistas en perspectiva; `batch_size` solo controla cuántas de esas vistas se procesan por lote de inferencia.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `moge_geometry` | Un diccionario que contiene la geometría estimada: `points` (nube de puntos 3D), `depth` (mapa de profundidad), `mask` (máscara de área válida) e `image` (la imagen de entrada). | MOGE_GEOMETRY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/es.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
