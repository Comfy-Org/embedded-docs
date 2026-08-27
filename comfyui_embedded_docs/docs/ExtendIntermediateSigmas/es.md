# ExtendIntermediateSigmas

El nodo ExtendIntermediateSigmas toma una secuencia existente de valores sigma e inserta valores sigma intermedios adicionales entre ellos. Permite especificar cuántos pasos adicionales añadir, el método de espaciado para la interpolación, y límites opcionales de sigma inicial y final para controlar dónde ocurre la extensión dentro de la secuencia de sigma.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | La secuencia de sigma de entrada para extender con valores intermedios | SIGMAS | Sí | - |
| `pasos` | Controla el número de valores sigma intermedios insertados entre cada par de sigmas existentes. El intervalo entre dos sigmas se divide en `steps` partes, produciendo `steps - 1` valores nuevos por par (predeterminado: 2, que inserta un valor por par) | INT | Sí | 1 a 100 |
| `comenzar_en_sigma` | Límite superior de sigma para la extensión: solo extiende sigmas por debajo de este valor (predeterminado: -1.0, que significa infinito) | FLOAT | Sí | -1.0 a 20000.0 |
| `terminar_en_sigma` | Límite inferior de sigma para la extensión: solo extiende sigmas por encima de este valor (predeterminado: 12.0) | FLOAT | Sí | 0.0 a 20000.0 |
| `espaciado` | El método de interpolación para espaciar los valores sigma intermedios (predeterminado: "linear") | COMBO | Sí | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Nota:** El nodo solo inserta sigmas intermedios entre pares de sigmas existentes donde el sigma actual es menor o igual a `start_at_sigma` y mayor o igual a `end_at_sigma`. Cuando `start_at_sigma` se establece en -1.0, se trata como infinito, lo que significa que solo se aplica el límite inferior `end_at_sigma`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | La secuencia de sigma extendida con valores intermedios adicionales insertados | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/es.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
