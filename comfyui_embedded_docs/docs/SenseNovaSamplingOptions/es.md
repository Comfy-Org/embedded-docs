# SenseNovaSamplingOptions

SenseNova Sampling Options establece el desplazamiento de flujo de SenseNova en un modelo. Clona el modelo de entrada, adjunta una configuración de muestreo de modelo SenseNova utilizando el valor de desplazamiento de flujo elegido y devuelve el modelo parcheado para su uso durante el muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo al que se le aplica la configuración de muestreo con desplazamiento de flujo de SenseNova. | MODEL | Sí | - |
| `shift` | El valor de desplazamiento de flujo que se establecerá en el muestreo del modelo SenseNova (valor predeterminado: 3.0; paso de interfaz: 0.01). | FLOAT | Sí | Sin mínimo ni máximo definido |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `MODEL` | Un clon del modelo de entrada con el desplazamiento de flujo de SenseNova aplicado a su configuración de muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/es.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
