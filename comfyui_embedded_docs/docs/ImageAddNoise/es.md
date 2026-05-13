> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/es.md)

El nodo ImageAddNoise añade ruido aleatorio a una imagen de entrada. Utiliza una semilla aleatoria específica para generar patrones de ruido consistentes y permite controlar la intensidad del efecto de ruido. La imagen resultante mantiene las mismas dimensiones que la entrada, pero con una textura visual añadida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada a la que se le añadirá ruido |
| `semilla` | INT | Sí | 0 a 18446744073709551615 | La semilla aleatoria utilizada para generar el ruido (predeterminado: 0) |
| `intensidad` | FLOAT | Sí | 0.0 a 1.0 | Controla la intensidad del efecto de ruido (predeterminado: 0.5) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `imagen` | IMAGE | La imagen de salida con el ruido añadido aplicado |

---
**Source fingerprint (SHA-256):** `8abfc64500e5ff8fe7589763a07c15d771e9a5a6a61bae9ec4d819be9bf71810`
