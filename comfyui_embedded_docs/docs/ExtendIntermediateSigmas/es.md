# ExtendIntermediateSigmas

El nodo ExtendIntermediateSigmas toma una secuencia existente de valores sigma e inserta valores sigma intermedios adicionales entre ellos. Permite especificar cuántos pasos adicionales agregar, el método de espaciado para la interpolación y límites sigma opcionales de inicio y fin para controlar dónde ocurre la extensión dentro de la secuencia sigma.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | La secuencia sigma de entrada a extender con valores intermedios | SIGMAS | Sí | - |
| `pasos` | Número de pasos intermedios a insertar entre sigmas existentes (predeterminado: 2) | INT | Sí | 1 a 100 |
| `comenzar_en_sigma` | Límite sigma superior para la extensión: solo extiende sigmas por debajo de este valor (predeterminado: -1.0, que significa infinito) | FLOAT | Sí | -1.0 a 20000.0 |
| `terminar_en_sigma` | Límite sigma inferior para la extensión: solo extiende sigmas por encima de este valor (predeterminado: 12.0) | FLOAT | Sí | 0.0 a 20000.0 |
| `espaciado` | El método de interpolación para espaciar los valores sigma intermedios (predeterminado: "linear") | COMBO | Sí | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Nota:** El nodo solo inserta sigmas intermedios entre pares de sigmas existentes donde tanto el sigma actual es menor o igual a `start_at_sigma` como mayor o igual a `end_at_sigma`. Cuando `start_at_sigma` se establece en -1.0, se trata como infinito, lo que significa que solo aplica el límite inferior `end_at_sigma`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sigmas` | La secuencia sigma extendida con valores intermedios adicionales insertados | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/es.md)

---
**Source fingerprint (SHA-256):** `f51ed433fc38365334ff8e4072174dc04982a8a00770d07f544320a6863577c4`
