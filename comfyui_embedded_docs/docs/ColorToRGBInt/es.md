# Color a RGB Int

El nodo **ColorToRGBInt** convierte un color especificado en formato hexadecimal (como `#FF5733`) en un único valor entero RGB. Toma los componentes rojo, verde y azul de la cadena de color y los combina en un solo entero, y devuelve la representación hexadecimal. También se admiten colores con canal alfa (`#RRGGBBAA`), y el valor alfa se devuelve por separado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `color` | Un valor de color en el formato hexadecimal `#RRGGBB` o `#RRGGBBAA`. Debe tener exactamente 7 u 9 caracteres y comenzar con `#`. | COLOR | Sí | `#RRGGBB`<br>`#RRGGBBAA` |

**Nota:** La cadena de entrada `color` debe seguir exactamente el formato `#RRGGBB` o `#RRGGBBAA`. Si la cadena no tiene 7 u 9 caracteres, no comienza con `#`, o contiene caracteres que no son dígitos hexadecimales válidos, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `rgb_int` | El valor entero RGB calculado, derivado de la fórmula: `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | La cadena de color hexadecimal en formato `#RRGGBB`. Si la entrada incluye un canal alfa, se elimina de esta salida. | COLOR |
| `alpha` | El valor alfa (opacidad) como un número de 0.0 a 1.0. Para colores de entrada con canal alfa (`#RRGGBBAA`), es el valor alfa de dos dígitos dividido por 255. Para colores sin canal alfa, es 1.0. | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/es.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
