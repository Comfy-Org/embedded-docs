# ExtendIntermediateSigmas

El nodo `ExtendIntermediateSigmas` toma una secuencia existente de valores sigma e inserta valores sigma intermedios adicionales entre ellos. Permite especificar cuántos pasos adicionales añadir, el método de espaciado para la interpolación y límites de sigma inicial y final opcionales para controlar dónde se produce la extensión dentro de la secuencia de sigma.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | La secuencia de sigma de entrada para extender con valores intermedios | SIGMAS | Sí | - |
| `steps` | Número de pasos intermedios para insertar entre los sigma existentes; con N pasos, se insertan N-1 valores sigma intermedios entre cada par elegible (predeterminado: 2) | INT | Sí | 1 to 100 |
| `start_at_sigma` | Límite de sigma superior para la extensión: solo extiende los sigma por debajo de este valor (predeterminado: -1.0, que significa infinito) | FLOAT | Sí | -1.0 to 20000.0 |
| `end_at_sigma` | Límite de sigma inferior para la extensión: solo extiende los sigma por encima de este valor (predeterminado: 12.0) | FLOAT | Sí | 0.0 to 20000.0 |
| `spacing` | El método de interpolación para espaciar los valores sigma intermedios: "linear" los distribuye uniformemente, "cosine" y "sine" aplican un espaciado curvo (predeterminado: "linear") | COMBO | Sí | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Nota:** El nodo solo inserta sigma intermedios entre pares de sigma existentes donde el sigma actual sea menor o igual que `start_at_sigma` y mayor o igual que `end_at_sigma` a la vez. Cuando `start_at_sigma` se establece en -1.0, se trata como infinito, lo que significa que solo se aplica el límite inferior `end_at_sigma`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sigmas` | La secuencia de sigma extendida con valores intermedios adicionales insertados | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/es.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
