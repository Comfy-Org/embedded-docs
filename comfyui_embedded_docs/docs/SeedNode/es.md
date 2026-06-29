# Semilla

El nodo Semilla genera un valor entero fijo o aleatorio. Se utiliza comúnmente para controlar la reproducibilidad de operaciones aleatorias en otros nodos, proporcionando un punto de partida consistente para la generación de números aleatorios.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `semilla` | El valor de semilla a utilizar. La opción de control posterior a la generación determina si el valor permanece fijo o cambia después de cada generación. | INT | Sí | 0 a 9223372036854775807 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `semilla` | El valor de semilla generado. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/es.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`
