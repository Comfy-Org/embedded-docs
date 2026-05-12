> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/es.md)

# Sampler AR Video

El nodo Sampler AR Video proporciona un método de muestreo especializado para modelos de video autorregresivos, como aquellos que utilizan técnicas de Forzado Causal o Auto-Forzado. Gestiona todos los parámetros relacionados con el bucle autorregresivo (AR) directamente dentro del flujo de trabajo, facilitando la configuración de cómo el modelo genera fotogramas de video paso a paso.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `num_frame_per_block` | INT | Sí | 1 a 64 | Fotogramas por bloque autorregresivo. Un valor de 1 significa que el modelo genera un fotograma a la vez (fotograma por fotograma), mientras que un valor de 3 significa que genera tres fotogramas juntos (por bloques). Esta configuración debe coincidir con el modo de entrenamiento del checkpoint. Valor predeterminado: 1. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `SAMPLER` | SAMPLER | Un objeto muestreador configurado que utiliza la función de muestreo "ar_video" con los parámetros autorregresivos especificados. |