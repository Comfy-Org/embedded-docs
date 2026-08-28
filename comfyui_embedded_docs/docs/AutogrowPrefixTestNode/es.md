# AutogrowPrefixTestNode

El AutogrowPrefixTestNode es un nodo lógico que prueba la función de entrada de autogrow. Acepta un número dinámico de entradas flotantes, convierte cada valor en texto, los combina en una cadena separada por comas y genera esa cadena.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `autogrow` | Un grupo de entrada dinámico que acepta entre 1 y 10 valores flotantes. Cada valor es un número de punto flotante, y las entradas generadas se nombran con el prefijo `float`. | AUTOGROW | Sí | 1 a 10 entradas |

**Nota:** La entrada `autogrow` es una entrada dinámica especial. Puede agregar múltiples entradas flotantes a este grupo, desde un mínimo de 1 hasta un máximo de 10. El nodo procesa todos los valores proporcionados e incluye cada entrada conectada en la cadena de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Una única cadena que contiene todos los valores flotantes de entrada, separados por comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/es.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
