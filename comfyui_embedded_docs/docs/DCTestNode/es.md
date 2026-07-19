# DCTestNode

El DCTestNode es un nodo lógico que devuelve diferentes tipos de datos según la selección del usuario en un cuadro combinado dinámico. Actúa como un enrutador condicional, donde la opción elegida determina qué campo de entrada está activo y qué tipo de valor generará el nodo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `combo` | La selección principal que determina qué campo de entrada está activo y qué generará el nodo. | COMBO | Sí | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |
| `string` | Un campo de entrada de texto. Este campo solo está activo y es obligatorio cuando `combo` está configurado en `"option1"`. | STRING | No | - |
| `integer` | Un campo de entrada de números enteros. Este campo solo está activo y es obligatorio cuando `combo` está configurado en `"option2"`. | INT | No | - |
| `image` | Un campo de entrada de imagen. Este campo solo está activo y es obligatorio cuando `combo` está configurado en `"option3"`. | IMAGE | No | - |
| `subcombo` | Una selección secundaria que aparece cuando `combo` está configurado en `"option4"`. Determina qué campos de entrada anidados están activos. | COMBO | No | `"opt1"`<br>`"opt2"` |
| `float_x` | Una entrada de número decimal. Este campo solo está activo y es obligatorio cuando `combo` está configurado en `"option4"` y `subcombo` está configurado en `"opt1"`. | FLOAT | No | - |
| `float_y` | Una entrada de número decimal. Este campo solo está activo y es obligatorio cuando `combo` está configurado en `"option4"` y `subcombo` está configurado en `"opt1"`. | FLOAT | No | - |
| `mask1` | Un campo de entrada de máscara. Este campo solo está activo cuando `combo` está configurado en `"option4"` y `subcombo` está configurado en `"opt2"`. Es opcional. | MASK | No | - |

**Restricciones de Parámetros:**

* El parámetro `combo` controla la visibilidad y obligatoriedad de todos los demás campos de entrada. Solo se mostrarán y serán obligatorias las entradas asociadas con la opción seleccionada en `combo` (excepto `mask1`, que es opcional).
* Cuando `combo` está configurado en `"option4"`, el parámetro `subcombo` se vuelve obligatorio y controla un segundo conjunto de entradas anidadas (`float_x`/`float_y` o `mask1`).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La salida depende de la opción seleccionada en `combo`. Puede ser un STRING (`"option1"`), un INT (`"option2"`), una IMAGE (`"option3"`) o una representación en cadena del diccionario `subcombo` (`"option4"`). | ANYTYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/es.md)

---
**Source fingerprint (SHA-256):** `98c4ca2100a27594df360935cc1507960480fe75a76ca0df2af75925d399be00`
