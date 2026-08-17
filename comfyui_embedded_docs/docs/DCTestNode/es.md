# DCTestNode

DCTestNode es un nodo lógico que devuelve diferentes tipos de datos según la selección del usuario en un cuadro combinado dinámico. Actúa como un enrutador condicional, donde la opción elegida determina qué campo de entrada está activo y qué tipo de valor generará el nodo.

## Entradas

El selector `combo` siempre está visible. Los campos de entrada que se muestran debajo dependen de la opción seleccionada.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `combo` | La selección principal que determina qué campo de entrada está activo y qué generará el nodo. | DYNAMIC_COMBO | Sí | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### Entradas de option1

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `string` | Un campo de entrada de texto. Este campo solo está activo y es obligatorio cuando `combo` está establecido en `"option1"`. | STRING | Sí | - |

### Entradas de option2

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `integer` | Un campo de entrada de números enteros. Este campo solo está activo y es obligatorio cuando `combo` está establecido en `"option2"`. | INT | Sí | - |

### Entradas de option3

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | Un campo de entrada de imagen. Este campo solo está activo y es obligatorio cuando `combo` está establecido en `"option3"`. | IMAGE | Sí | - |

### Entradas de option4

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `subcombo` | Una selección secundaria que aparece cuando `combo` está establecido en `"option4"`. Determina qué campos de entrada anidados están activos. | DYNAMIC_COMBO | Sí | `"opt1"`<br>`"opt2"` |

#### Entradas de opt1

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `float_x` | Un campo de entrada de número decimal. Este campo solo está activo y es obligatorio cuando `combo` está establecido en `"option4"` y `subcombo` en `"opt1"`. | FLOAT | Sí | - |
| `float_y` | Un campo de entrada de número decimal. Este campo solo está activo y es obligatorio cuando `combo` está establecido en `"option4"` y `subcombo` en `"opt1"`. | FLOAT | Sí | - |

#### Entradas de opt2

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `mask1` | Un campo de entrada de máscara. Este campo solo está activo cuando `combo` está establecido en `"option4"` y `subcombo` en `"opt2"`. Es opcional. | MASK | No | - |

**Restricciones de parámetros:**

* El parámetro `combo` controla la visibilidad y el requisito de todos los demás campos de entrada. Solo se muestran y son obligatorias las entradas asociadas con la opción `combo` seleccionada (excepto `mask1`, que es opcional).
* Cuando `combo` está establecido en `"option4"`, el parámetro `subcombo` se activa y es obligatorio, y controla un segundo conjunto de entradas anidadas: `"opt1"` muestra `float_x` y `float_y`; `"opt2"` muestra `mask1`.
* Si `combo` se establece en un valor inesperado, el nodo lanza un ValueError.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La salida depende de la opción `combo` seleccionada. Puede ser un STRING (`"option1"`), un INT (`"option2"`), una IMAGE (`"option3"`), o una representación en cadena del diccionario `subcombo` (`"option4"`). | ANYTYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/es.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
