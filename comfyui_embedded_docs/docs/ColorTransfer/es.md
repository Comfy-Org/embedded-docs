> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/es.md)

El nodo ColorTransfer ajusta la paleta de colores de una imagen objetivo para que coincida con los colores de una imagen de referencia. Utiliza diferentes algoritmos matemáticos para analizar y transferir las características de color, como el brillo, el contraste y la distribución de tonos, desde la referencia al objetivo. Esto es útil para crear coherencia visual entre múltiples imágenes o para aplicar un gradado de color específico.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image_target` | IMAGE | Sí | - | Imagen(es) a la(s) que se aplicará la transformación de color. |
| `image_ref` | IMAGE | No | - | Imagen(es) de referencia con la(s) que se igualarán los colores. Si no se proporciona, se omite el procesamiento y se devuelve la imagen objetivo sin cambios. |
| `method` | COMBO | Sí | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` | El algoritmo de transferencia de color a utilizar. |
| `source_stats` | DYNAMICCOMBO | Sí | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` | Determina cómo se calculan las estadísticas de color a partir de la(s) imagen(es) fuente (objetivo). |
| `strength` | FLOAT | Sí | 0.0 a 10.0 | La intensidad del efecto de transferencia de color. Un valor de 1.0 aplica la transformación completa, mientras que 0.0 devuelve la imagen original. Por defecto: 1.0 |

**Detalles de los Parámetros:**
*   **Opciones de `source_stats`:**
    *   **`per_frame`**: Cada fotograma en un lote se iguala individualmente a la `image_ref`.
    *   **`uniform`**: Las estadísticas de color se agrupan en todos los fotogramas fuente para crear una única línea base, que luego se iguala a la `image_ref`.
    *   **`target_frame`**: Utiliza un fotograma elegido del lote objetivo como línea base para calcular la transformación hacia la `image_ref`. Esta transformación se aplica luego uniformemente a todos los fotogramas, lo que preserva las diferencias de color relativas entre ellos. Cuando se selecciona esta opción, se hace disponible un parámetro adicional `target_index`.
*   **`target_index`** (aparece cuando `source_stats` es `"target_frame"`): El índice del fotograma (comenzando desde 0) utilizado como línea base fuente para calcular la transformación. Por defecto: 0. Debe estar entre 0 y 10000.

**Restricciones:**
*   Si no se proporciona `image_ref` o `strength` se establece en 0.0, el nodo devuelve la `image_target` original sin procesar.
*   Cuando `source_stats` está configurado como `"target_frame"`, el `target_index` debe ser un índice válido dentro del lote de `image_target`. Si excede el número de fotogramas, se utiliza el último fotograma.
*   Para el método `histogram` con `source_stats` configurado como `"per_frame"`, si el tamaño del lote de `image_ref` es mayor que 1, cada fotograma objetivo se iguala al fotograma de referencia correspondiente por índice. Si el lote de referencia tiene solo un fotograma, se utiliza para todos los fotogramas objetivo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La(s) imagen(es) resultante(s) después de aplicar la transferencia de color. |