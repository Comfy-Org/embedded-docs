> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/es.md)

# Descripción General

Este nodo permite especificar el rendimiento relativo de cada GPU al utilizar múltiples tarjetas gráficas con diferentes velocidades. Crea un grupo de opciones de GPU que puede utilizarse para distribuir el trabajo entre dispositivos, aunque la distribución de carga basada en velocidad aún no está implementada en la versión actual.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `device_index` | INT | Sí | 0 a 64 | Número de índice del dispositivo GPU a configurar (predeterminado: 0) |
| `relative_speed` | FLOAT | Sí | 0.0 a ilimitado | Velocidad relativa de esta GPU en comparación con otras, utilizada para la distribución de carga de trabajo (predeterminado: 1.0, incremento: 0.01) |
| `gpu_options` | GPU_OPTIONS | No | - | Grupo de opciones de GPU existente al que añadir las opciones de este dispositivo. Si no se proporciona, se crea un nuevo grupo |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `GPU_OPTIONS` | GPU_OPTIONS | Grupo de opciones de GPU que contiene la configuración del dispositivo, el cual puede pasarse a otros nodos para operaciones con múltiples GPU |

**Nota:** El parámetro `relative_speed` está definido pero aún no es utilizado por el planificador interno para distribuir el trabajo entre las GPU. En la implementación actual, el trabajo se distribuye de manera uniforme entre todos los dispositivos, independientemente de sus velocidades relativas.

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
