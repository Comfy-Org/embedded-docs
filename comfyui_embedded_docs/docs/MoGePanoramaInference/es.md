> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/es.md)

## Descripción general

Este nodo realiza la estimación de profundidad en imágenes panorámicas equirrectangulares. Funciona dividiendo el panorama en 12 vistas en perspectiva, ejecutando el modelo de estimación de profundidad MoGe en cada vista y luego fusionando los resultados en un único mapa de profundidad completo para el panorama original.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `moge_model` | MOGE_MODEL | Sí | | El modelo MoGe a utilizar para la inferencia. |
| `image` | IMAGE | Sí | | Imagen panorámica equirrectangular (cualquier relación de aspecto). |
| `resolution_level` | INT | Sí | 0 a 9 | Nivel de detalle por vista. Valores más altos producen mapas de profundidad más detallados (predeterminado: 9). |
| `split_resolution` | INT | Sí | 256 a 1024 | Resolución de cada vista en perspectiva después de dividir el panorama (predeterminado: 512). |
| `merge_resolution` | INT | Sí | 256 a 8192 | Resolución del lado largo del mapa de profundidad equirrectangular final fusionado (predeterminado: 1920). |
| `batch_size` | INT | Sí | 1 a 12 | Número de vistas en perspectiva a procesar en cada lote de inferencia. El número total de vistas es 12 (predeterminado: 4). |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|-------------|-----------|-------------|
| `moge_geometry` | MOGE_GEOMETRY | Un diccionario que contiene la geometría estimada: `points` (nube de puntos 3D), `depth` (mapa de profundidad), `mask` (máscara de área válida) e `image` (la imagen de entrada). |

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
