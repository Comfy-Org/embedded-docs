> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/es.md)

El nodo SamplerDPMPP_3M_SDE crea un sampler DPM++ 3M SDE para usar en el proceso de muestreo. Este sampler utiliza un método de ecuación diferencial estocástica multietapa de tercer orden con parámetros de ruido configurables. El nodo permite elegir si los cálculos de ruido se realizan en la GPU o la CPU.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sí | 0.0 - 100.0 | Controla la estocasticidad del proceso de muestreo (valor por defecto: 1.0) |
| `s_ruido` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (valor por defecto: 1.0) |
| `dispositivo_ruido` | COMBO | Sí | "gpu"<br>"cpu" | Selecciona el dispositivo para los cálculos de ruido, ya sea GPU o CPU |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve un objeto sampler configurado para usar en flujos de trabajo de muestreo |
