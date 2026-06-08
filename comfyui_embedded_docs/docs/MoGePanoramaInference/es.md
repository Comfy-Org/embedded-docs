## Descripción general

Este nodo realiza la estimación de profundidad en imágenes panorámicas equirrectangulares. Funciona dividiendo el panorama en 12 vistas en perspectiva, ejecutando el modelo de estimación de profundidad MoGe en cada vista y luego fusionando los resultados en un único mapa de profundidad completo para el panorama original.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `moge_model` | El modelo MoGe a utilizar para la inferencia. | MOGE_MODEL | Sí |  |
| `image` | Imagen panorámica equirrectangular (cualquier relación de aspecto). | IMAGE | Sí |  |
| `resolution_level` | Nivel de detalle por vista. Valores más altos producen mapas de profundidad más detallados (predeterminado: 9). | INT | Sí | 0 a 9 |
| `split_resolution` | Resolución de cada vista en perspectiva después de dividir el panorama (predeterminado: 512). | INT | Sí | 256 a 1024 |
| `merge_resolution` | Resolución del lado largo del mapa de profundidad equirrectangular final fusionado (predeterminado: 1920). | INT | Sí | 256 a 8192 |
| `batch_size` | Número de vistas en perspectiva a procesar en cada lote de inferencia. El número total de vistas es 12 (predeterminado: 4). | INT | Sí | 1 a 12 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `moge_geometry` | Un diccionario que contiene la geometría estimada: `points` (nube de puntos 3D), `depth` (mapa de profundidad), `mask` (máscara de área válida) e `image` (la imagen de entrada). | MOGE_GEOMETRY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/es.md)

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
