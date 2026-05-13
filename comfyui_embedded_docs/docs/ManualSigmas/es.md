> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/es.md)

El nodo ManualSigmas te permite definir manualmente una secuencia personalizada de niveles de ruido (sigmas) para el proceso de muestreo. Ingresas una lista de números como cadena de texto, y el nodo los convierte en un tensor que puede ser utilizado por otros nodos de muestreo. Esto es útil para realizar pruebas o crear programaciones de ruido específicas.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `sigmas` | STRING | Sí | Cualquier número separado por comas o espacios | Una cadena de texto que contiene los valores sigma. El nodo extraerá todos los números de esta cadena. Por ejemplo, "1, 0.5, 0.1" o "1 0.5 0.1". El valor predeterminado es "1, 0.5". |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `sigmas` | SIGMAS | El tensor que contiene la secuencia de valores sigma extraídos de la cadena de texto de entrada. |

---
**Source fingerprint (SHA-256):** `b815633dfea8f529f487f46b2d0464fa8c1045df8c4d4ef586bd36ad6f4a28db`
