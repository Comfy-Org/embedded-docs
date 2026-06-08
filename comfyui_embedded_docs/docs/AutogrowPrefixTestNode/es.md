El nodo AutogrowPrefixTestNode es un nodo lógico diseñado para probar la función de entrada de crecimiento automático. Acepta una cantidad dinámica de entradas flotantes, combina sus valores en una cadena separada por comas y genera esa cadena como salida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `autogrow` | Un grupo de entrada dinámico que puede aceptar entre 1 y 10 valores flotantes. Cada entrada en el grupo es de tipo FLOAT con un valor mínimo de 1 y un valor máximo de 10. | AUTOGROW | Sí | 1 a 10 entradas |

**Nota:** La entrada `autogrow` es una entrada dinámica especial. Puedes agregar múltiples entradas flotantes a este grupo, hasta un máximo de 10. El nodo procesará todos los valores proporcionados. Cada entrada flotante individual está limitada a un rango de 1 a 10.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | Una sola cadena que contiene todos los valores flotantes de entrada, separados por comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/es.md)

---
**Source fingerprint (SHA-256):** `7ae65365f77399a2ad8358b5a1eab3f2caa39331e53dec474cdd7f2751bfff4b`
