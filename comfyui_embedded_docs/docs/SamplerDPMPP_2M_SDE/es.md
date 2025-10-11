> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/es.md)

El nodo SamplerDPMPP_2M_SDE crea un muestreador DPM++ 2M SDE para modelos de difusión. Este muestreador utiliza solucionadores de ecuaciones diferenciales de segundo orden con ecuaciones diferenciales estocásticas para generar muestras. Ofrece diferentes tipos de solucionadores y opciones de manejo de ruido para controlar el proceso de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | STRING | Sí | `"midpoint"`<br>`"heun"` | El tipo de solucionador de ecuaciones diferenciales a utilizar para el proceso de muestreo |
| `eta` | FLOAT | Sí | 0.0 - 100.0 | Controla la estocasticidad del proceso de muestreo (valor por defecto: 1.0) |
| `s_noise` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (valor por defecto: 1.0) |
| `noise_device` | STRING | Sí | `"gpu"`<br>`"cpu"` | El dispositivo donde se realizan los cálculos de ruido |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Un objeto muestreador configurado listo para usar en el pipeline de muestreo |