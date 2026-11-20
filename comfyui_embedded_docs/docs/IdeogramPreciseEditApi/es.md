# Edición precisa de Ideogram 4.5

Edita una imagen guiándote por un prompt de texto con la edición precisa de Ideogram 4.6 o 4.5: solo cambia lo que el prompt solicita. Una edición de región mantiene la imagen 1 con su tamaño y resolución exactos. Una edición de imagen completa escala la imagen 1 hacia abajo antes de subirla cuando supera el límite del modelo, por lo que el resultado puede ser más pequeño que la entrada: 16.7 MP o 8192 píxeles por lado en 4.6, aproximadamente 4 MP o 4608 píxeles por lado en 4.5. La imagen 1 es la imagen que se va a editar y se pueden conectar hasta 4 imágenes más como referencias. También se puede editar una sola región de la imagen 1 por sí sola, seleccionada mediante una máscara o mediante cajas delimitadoras, lo que devuelve la imagen a tamaño completo.

## Entradas

Seleccionar un `model` determina qué entradas aparecen. Ambos modelos editan una región mediante `context_window`, pero 4.6 toma su máscara de `mask` mientras que 4.5 la toma de `context_window_mask`, y 4.6 tiene `"auto"` como valor predeterminado en lugar de `"none"`.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo que se va a usar. `"ideogram-4.6"` admite fuentes más grandes y regiones más amplias; `"ideogram-4.5"` es el modelo anterior (predeterminado: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sí | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Ranura ampliable: la imagen 1 es la imagen que se va a editar y las imágenes 2 a 5 son referencias opcionales (`image_1` ... `image_5`). Consúltelas en el prompt como @Image1, @Image2, ...; una entrada por lotes cuenta una vez por imagen. Cada imagen debe tener una relación de aspecto entre 1:6 y 6:1, salvo que la imagen 1 no se verifica en cuanto a relación de aspecto mientras se utiliza una ventana de contexto. | IMAGE | Sí | 1 a 5 imágenes |
| `prompt` | Instrucciones de edición. Admite referencias del tipo @Image1 a las imágenes conectadas (predeterminado: cadena vacía). | STRING | Sí | 1 a 10000 caracteres |
| `quality` | Nivel de calidad. Los niveles más altos cuestan más y tardan más (predeterminado: `"medium"`). | COMBO | Sí | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semilla para la generación. En 4.6, las mismas imágenes, el mismo prompt, los mismos ajustes y la misma semilla dan el mismo resultado o uno muy similar; en 4.5, dan el mismo resultado (predeterminado: 42). | INT | Sí | 0 a 2147483647 |

### Entradas de Ideogram 4.6

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Región de la imagen 1 que se va a editar. `"auto"` edita la región alrededor de la máscara y mantiene la imagen 1 a tamaño completo, o la imagen completa cuando no hay una máscara conectada; `"none"` edita la imagen completa; `"custom"` edita la región de `context_window_bboxes` y mantiene la imagen 1 a tamaño completo (predeterminado: `"auto"`). Una `mask` conectada se envía en los tres modos, incluido `"none"`. | COMBO | No | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Región de la imagen 1 que se va a editar, por ejemplo, la salida de Create Bounding Boxes. Obligatorio cuando `context_window` es `"custom"`; no se usa en caso contrario. Varias cajas se combinan en una sola región, que se amplía hasta al menos 256 píxeles por lado y se estira más solo cuando es necesario para mantenerse dentro de la relación de aspecto máxima de 6:1. La región puede tener hasta 8192 píxeles por lado y aproximadamente 16.7 MP (p. ej., 4096x4096); el área se comprueba después de redondear cada lado hacia arriba a un múltiplo de 32, por lo que se rechaza una región de 4097x4095 aunque su área sin redondear esté por debajo de 16.7 MP. | BOUNDING_BOX | No | - |
| `mask` | El blanco marca qué editar; la región de edición se coloca alrededor de este. La máscara debe contener tanto áreas blancas (editar) como negras (conservar). Se envía siempre que esté conectada, en todos los modos de `context_window`, y reduce el límite de imágenes a 4 (consulte las restricciones a continuación). | MASK | No | - |

### Entradas de Ideogram 4.5

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Región de la imagen 1 que se va a editar. `"none"` edita la imagen completa. `"auto"` edita una región alrededor de `context_window_mask` y `"custom"` la región de `context_window_bboxes`; ambos mantienen la imagen 1 a tamaño completo y dejan el resto de la imagen sin cambios (predeterminado: `"none"`). | COMBO | No | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Región de la imagen 1 que se va a editar, por ejemplo, la salida de Create Bounding Boxes. Obligatorio cuando `context_window` es `"custom"`; no se usa en caso contrario. Varias cajas se combinan en una sola región, que se amplía hasta al menos 256 píxeles por lado y se estira más solo cuando es necesario para mantenerse dentro de la relación de aspecto máxima de 6:1, por lo que una caja pequeña, como 32x32, también edita sus píxeles circundantes. La región puede tener hasta 4608 píxeles por lado y aproximadamente 4 MP (p. ej., 2048x2048); se comprueba después de redondear cada lado hacia arriba a un múltiplo de 32. | BOUNDING_BOX | No | - |
| `context_window_mask` | El blanco marca qué editar; la región de edición se coloca alrededor de este. Obligatorio cuando `context_window` es `"auto"`; no se usa en caso contrario. La máscara debe contener tanto áreas blancas (editar) como negras (conservar). | MASK | No | - |

### Restricciones de los parámetros

- **Cantidad de imágenes:** al menos 1 y como máximo 5 imágenes; una entrada por lotes cuenta una vez por imagen. Cuando el nodo usa una máscara, se aceptan como máximo 4 imágenes, es decir, la imagen 1 y 3 referencias. En 4.6, una `mask` conectada se usa en todos los modos; en 4.5, la máscara es `context_window_mask` y se usa solo en `"auto"`, por lo que `"none"` y `"custom"` siguen aceptando 5 imágenes con una máscara conectada.
- **Tamaño de salida:** el nodo no tiene entradas de tamaño, ancho ni alto. Una edición de región devuelve la imagen completa al tamaño de la imagen 1. Una edición de imagen completa devuelve el tamaño de la imagen 1 tal como se subió: en 4.6, una imagen por encima de 16.7 MP o de 8192 píxeles por lado se reduce primero, y en 4.5 ocurre lo mismo por encima de aproximadamente 4 MP o 4608 píxeles por lado.
- **Tamaño de la fuente de la región:** con una ventana de contexto en uso, la imagen 1 puede tener hasta 67,108,864 píxeles en total (aproximadamente 67 MP), por ejemplo, 8192x8192 o 10000x5000; el límite es sobre el área, no sobre un lado.
- **Límites de la región:** una región de `context_window_bboxes` puede tener hasta 8192 píxeles por lado y aproximadamente 16.7 MP en 4.6, y hasta 4608 píxeles por lado y aproximadamente 4 MP en 4.5. Las cajas generan un error solo cuando su región combinada queda fuera de la imagen 1, por lo que una caja a la izquierda de la imagen y otra a la derecha se combinan en una región que abarca la imagen.
- **Etiquetas del prompt:** `@ImageN` se compara sin distinguir mayúsculas y minúsculas y no debe superar el número de imágenes conectadas; el prompt no debe estar compuesto solo por espacios en blanco y debe tener como máximo 10000 caracteres.
- **Límite de carga:** la imagen 1, la máscara y las referencias juntas deben caber en la carga de 50 MB de Ideogram. Una edición de 4.6 y una edición de región de 4.5 vuelven a codificar la imagen 1 como JPEG cuando los archivos no caben y generan un error si aun así no cabe; una edición de imagen completa de 4.5 siempre envía PNG y no tiene ese mecanismo de reserva.
- **Seguridad del contenido:** si el filtro de seguridad de contenido de Ideogram bloquea el resultado, el nodo genera un error en lugar de devolver una imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `IMAGE` | La imagen editada como lote, al tamaño de la imagen 1. Una edición de imagen completa se devuelve más pequeña cuando la fuente supera el presupuesto de carga: 16.7 MP o 8192 píxeles por lado en 4.6, aproximadamente 4 MP o 4608 píxeles por lado en 4.5. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/es.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
