# BakeAmbientOcclusion

Genera un mapa de oclusión ambiental a partir de una malla de alta poligonización (high-poly) en la disposición UV de una malla de baja poligonización (low-poly). La salida es una imagen en escala de grises en la que los texeles blancos están abiertos y los texeles oscuros están en grietas; está pensada para la entrada de oclusión del nodo Apply Texture To Mesh. Conecta la malla de baja poligonización con UVs desplegados y la malla de alta poligonización de la que fue decimada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `low_poly` | La malla de baja poligonización con UVs desplegados sobre la que se hornea. Debe tener UVs; el nodo genera un error si faltan. | MESH | Sí | - |
| `high_poly` | La malla de alta poligonización de la que se decimó la de baja, utilizada como geometría de origen para la oclusión. | MESH | Sí | - |
| `resolution` | Resolución de textura en píxeles; cada texel recibe un valor de oclusión. Por defecto: 1024. | INT | Sí | 64 a 8192 (paso 64) |
| `samples` | Rayos por texel. Cuantos más, más suave y más lento. Auméntalo si aparece granulado. Por defecto: 64. | INT | Sí | 4 a 1024 (paso 4) |
| `max_distance` | Longitud del rayo, como fracción de la diagonal de la caja delimitadora. Cuanto más pequeño, más ajustada y más local es la oclusión. Por defecto: 0.5. | FLOAT | Sí | 0.01 a 2.0 (paso 0.01) |
| `strength` | Escala la oclusión. >1 oscurece, <1 aclara. Por defecto: 1.0. | FLOAT | Sí | 0.0 a 2.0 (paso 0.05) |
| `bias` | Elevación del origen del rayo respecto a la superficie, como fracción de la diagonal de la caja delimitadora. Auméntalo si incluso las superficies planas muestran manchas o agujeros oscuros. Por defecto: 0.01. | FLOAT | Sí | 0.0001 a 0.2 (paso 0.0005) |

Nota: `low_poly` debe tener coordenadas UV — este nodo nunca despliega la malla. Si `high_poly` contiene solo un elemento de lote, se reutiliza para cada elemento de lote de `low_poly`; los elementos de lote de `low_poly` sin caras se omiten y se reemplazan con una imagen completamente blanca, y se registra una advertencia.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `occlusion` | Imagen de oclusión ambiental en escala de grises con valores en [0,1] (blanco = abierto, oscuro = grietas), una imagen por cada elemento de lote de `low_poly`. Diseñada para la entrada de oclusión del nodo Apply Texture To Mesh (empaquetada en el mapa ORM / occlusionTexture). | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/es.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
