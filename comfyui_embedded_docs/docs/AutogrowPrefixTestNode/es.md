# AutogrowPrefixTestNode

El nodo `AutogrowPrefixTestNode` es un nodo lógico diseñado para probar la función de entrada de crecimiento automático. Acepta un número dinámico de entradas de tipo float, combina sus valores en una cadena separada por comas y devuelve esa cadena como salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `autogrow` | Un grupo de entrada dinámico que acepta valores float. El grupo puede contener entre 1 y 10 entradas float, y el nodo procesa todos los valores proporcionados. | FLOAT | Sí | De 1 a 10 entradas |

**Nota:** La entrada `autogrow` es una entrada dinámica especial que puede expandirse para añadir más entradas float hasta un máximo de 10. El mínimo es 1 entrada. Los valores `min` y `max` en este nodo definen el número permitido de entradas en el grupo, no el rango de valores de cada float individual.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Una sola cadena que contiene todos los valores float de entrada, separados por comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/es.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
