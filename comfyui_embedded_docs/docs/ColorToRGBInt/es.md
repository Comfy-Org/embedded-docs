# Color a RGB Int

El nodo ColorToRGBInt convierte un color especificado en formato hexadecimal en un único valor entero. Toma una cadena de color como `#FF5733` y calcula el entero RGB correspondiente combinando los componentes rojo, verde y azul.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `color` | Un valor de color en el formato hexadecimal `#RRGGBB`. | STRING | Sí | N/A |

**Nota:** La cadena de entrada `color` debe tener exactamente 7 caracteres y comenzar con el símbolo `#`, seguido de seis dígitos hexadecimales (por ejemplo, `#FF0000` para rojo). El nodo generará un error si el formato es incorrecto.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `rgb_int` | El valor entero RGB calculado. Se obtiene mediante la fórmula: `(Rojo * 65536) + (Verde * 256) + Azul`. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/es.md)

---
**Source fingerprint (SHA-256):** `5b8617d6b28caaa5f01dad1c6a302fa321f1bd53a0454451d468e36747e70e8f`
