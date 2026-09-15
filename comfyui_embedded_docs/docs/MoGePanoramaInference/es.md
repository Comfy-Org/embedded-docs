# Inferencia panorámica MoGe

Este nodo realiza estimación de profundidad en imágenes panorámicas equirrectangulares. Divide el panorama en 12 vistas en perspectiva, ejecuta el modelo de estimación de profundidad MoGe en cada vista y fusiona los resultados por vista de nuevo en un único mapa de profundidad que cubre todo el panorama. Las normales predichas por vista y la escala métrica se ignoran, ya que las escalas por vista no se alinearían a través de las costuras de superposición.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | El modelo MoGe que se usará para la inferencia. | MOGE_MODEL | Sí |  |
| `image` | Panorama equirrectangular (cualquier relación de aspecto). El nodo acepta solo una imagen; pasar un lote de imágenes genera un error. Solo se utilizan los primeros 3 canales de color (RGB). | IMAGE | Sí |  |
| `resolution_level` | Nivel de detalle por vista (0 = más rápido, 9 = más detallado) (predeterminado: 9). | INT | Sí | 0 a 9 |
| `split_resolution` | Resolución de cada división en perspectiva (predeterminado: 512). | INT | Sí | 256 a 1024 |
| `merge_resolution` | Resolución del lado largo del mapa de distancia equirrectangular fusionado (predeterminado: 1920). | INT | Sí | 256 a 8192 |
| `batch_size` | Vistas por lote de inferencia (12 divisiones en total) (predeterminado: 4). | INT | Sí | 1 a 12 |

**Notas:**

- La entrada debe ser una sola imagen. Si `image` contiene más de una imagen en el lote, el nodo genera un error.
- `merge_resolution` se trata como un tamaño máximo del lado largo. Si el panorama es más pequeño que este valor, el mapa fusionado se genera al tamaño original del panorama en lugar de ampliarse. El resultado fusionado se redimensiona de nuevo a la resolución original del panorama antes de devolverse.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `moge_geometry` | Un diccionario que contiene la geometría estimada: `points` (nube de puntos 3D), `depth` (mapa de profundidad), `mask` (máscara de área válida) e `image` (la imagen de entrada). | MOGE_GEOMETRY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/es.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
