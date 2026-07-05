# ImagenAgregarRuido

El nodo ImageAddNoise añade ruido aleatorio a una imagen de entrada. Utiliza una semilla aleatoria específica para generar patrones de ruido consistentes y permite controlar la intensidad del efecto de ruido. La imagen resultante mantiene las mismas dimensiones que la entrada, pero con una textura visual añadida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada a la que se le añadirá ruido | IMAGE | Sí | - |
| `semilla` | La semilla aleatoria utilizada para generar el ruido (predeterminado: 0) | INT | Sí | 0 a 18446744073709551615 |
| `intensidad` | Controla la intensidad del efecto de ruido (predeterminado: 0.5) | FLOAT | Sí | 0.0 a 1.0 |


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen de salida con el ruido añadido aplicado | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/es.md)

---
**Source fingerprint (SHA-256):** `8abfc64500e5ff8fe7589763a07c15d771e9a5a6a61bae9ec4d819be9bf71810`
