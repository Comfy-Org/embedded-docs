# BakeNormalMapFromMesh

Este nodo hornea un mapa de normales en espacio tangente desde una malla de alta poligonización (high-poly) sobre la disposición UV de una malla de baja poligonización (low-poly), capturando el detalle de superficie que se perdió durante la decimación. Conecta la malla low-poly con UVs desarrolladas y la malla high-poly de la que proviene, y el nodo genera una imagen lista para la entrada `normal_map` de Apply Texture To Mesh.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `low_poly` | La malla low-poly con UVs desarrolladas que recibe el detalle horneado. Debe tener UVs existentes; el nodo nunca desarrolla UVs. | MESH | Sí | — |
| `high_poly` | La malla high-poly cuyo detalle de superficie se hornea en la disposición UV de la low-poly. | MESH | Sí | — |
| `resolution` | Longitud de borde en píxeles del mapa de normales cuadrado de salida (predeterminado: 1024). | INT | Sí | 64 a 8192 (paso 64) |
| `cage_distance` | Banda de búsqueda de superficie, como fracción de la diagonal de la caja delimitadora. Auméntala para parches incorrectos o faltantes bajo una decimación intensa; bájala si capta a través de huecos. Predeterminado: 0.05. | FLOAT | Sí | 0.001 a 0.5 (paso 0.001) |
| `ignore_backfaces` | Omite las superficies high-poly que miran en dirección opuesta al texel, para que las grietas/espacios cerrados no capturen la pared opuesta. Desactívalo solo si el orden de vértices (winding) del high-poly es inconsistente. Predeterminado: true. | BOOLEAN | Sí | true / false |

Nota: `low_poly` debe tener coordenadas UV. Si no tiene, el nodo genera un error porque hornea sobre la disposición UV existente y no desarrolla la malla. Cuando `low_poly` es un lote, cada elemento se hornea en orden; si `high_poly` contiene solo un elemento, ese elemento se reutiliza para cada elemento del lote. Las mallas vacías en el lote se omiten con una advertencia y producen un mapa de normales gris medio plano (0.5).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `normal_map` | El mapa de normales horneado en espacio tangente (convención glTF/OpenGL +Y) como una imagen RGB cuadrada de resolución × resolución con valores en [0,1]. Conéctalo a la entrada `normal_map` de Apply Texture To Mesh. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/es.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
