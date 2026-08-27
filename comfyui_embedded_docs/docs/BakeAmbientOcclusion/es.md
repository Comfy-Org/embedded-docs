# BakeAmbientOcclusion

Hornea un mapa de oclusión ambiental de una malla de alta poligonización en el diseño UV de una malla de baja poligonización. La salida es una imagen en escala de grises en la que los texeles blancos están abiertos y los texeles oscuros están en hendiduras; está destinada a la entrada de oclusión del nodo Apply Texture To Mesh. Conecta la malla de baja poligonización con UV desplegados y la malla de alta poligonización de la que se decimó.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `low_poly` | La malla de baja poligonización con UV desplegados en la que se hornea. Debe tener UV; el nodo genera un error si faltan. | MESH | Sí | - |
| `high_poly` | La malla de alta poligonización de la que se decimó la de baja poligonización, utilizada como geometría de origen para la oclusión. | MESH | Sí | - |
| `resolution` | Resolución de textura en píxeles; cada texel recibe un valor de oclusión. Por defecto: 1024. | INT | Sí | 64 to 8192 (step 64) |
| `samples` | Rayos por texel. Más = más suave, más lento. Auméntalo si aparece granulado. Por defecto: 64. | INT | Sí | 4 to 1024 (step 4) |
| `max_distance` | Longitud del rayo, como fracción de la diagonal de la caja delimitadora. Más pequeño = más ajustado, oclusión más local. Por defecto: 0.5. | FLOAT | Sí | 0.01 to 2.0 (step 0.01) |
| `strength` | Escala la oclusión. >1 oscurece, <1 aclara. Por defecto: 1.0. | FLOAT | Sí | 0.0 to 2.0 (step 0.05) |
| `bias` | Elevación del origen del rayo desde la superficie, como fracción de la diagonal de la caja delimitadora. Auméntalo si superficies lisas muestran manchas o agujeros oscuros. Por defecto: 0.01. | FLOAT | Sí | 0.0001 to 0.2 (step 0.0005) |

Nota: `low_poly` debe tener coordenadas UV — este nodo nunca despliega los UV de la malla. Si `high_poly` contiene solo un elemento de lote, se reutiliza para cada elemento de lote de `low_poly`; los elementos de lote de `low_poly` sin caras se omiten y se reemplazan con una imagen completamente blanca, registrándose una advertencia.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `occlusion` | Imagen de oclusión ambiental en escala de grises con valores en [0,1] (blanco = abierto, oscuro = hendiduras), una imagen por elemento de lote de `low_poly`. Destinada a la entrada de oclusión del nodo Apply Texture To Mesh (empaquetada en el mapa ORM / occlusionTexture). | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/es.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
