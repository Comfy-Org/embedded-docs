# MultiGPU_Options

Este nodo permite especificar el rendimiento relativo de cada GPU al utilizar múltiples tarjetas gráficas con diferentes velocidades. Crea un grupo de opciones de GPU que puede utilizarse para distribuir el trabajo entre dispositivos, aunque la distribución de carga basada en velocidad aún no está implementada en la versión actual.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `device_index` | Número de índice del dispositivo GPU a configurar (predeterminado: 0) | INT | Sí | 0 a 64 |
| `relative_speed` | Velocidad relativa de esta GPU en comparación con otras, utilizada para la distribución de carga de trabajo (predeterminado: 1.0, incremento: 0.01) | FLOAT | Sí | 0.0 a ilimitado |
| `gpu_options` | Grupo de opciones de GPU existente al que añadir las opciones de este dispositivo. Si no se proporciona, se crea un nuevo grupo | GPU_OPTIONS | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `GPU_OPTIONS` | Grupo de opciones de GPU que contiene la configuración del dispositivo, el cual puede pasarse a otros nodos para operaciones con múltiples GPU | GPU_OPTIONS |

**Nota:** El parámetro `relative_speed` está definido pero aún no es utilizado por el planificador interno para distribuir el trabajo entre las GPU. En la implementación actual, el trabajo se distribuye de manera uniforme entre todos los dispositivos, independientemente de sus velocidades relativas.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/es.md)

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
