# ManualSigmas

El nodo ManualSigmas te permite definir manualmente una secuencia personalizada de niveles de ruido (sigmas) para el proceso de muestreo. Ingresas una lista de números como cadena, y el nodo los convierte en un tensor que puede ser utilizado por otros nodos de muestreo. Esto es útil para probar o crear programaciones de ruido específicas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | Una cadena que contiene los valores de sigma. El nodo extraerá todos los números de esta cadena. Por ejemplo, "1, 0.5, 0.1" o "1 0.5 0.1". El valor predeterminado es "1, 0.5". | STRING | Sí | Cualquier número separado por comas o espacios |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | El tensor que contiene la secuencia de valores de sigma extraídos de la cadena de entrada. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/es.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`
