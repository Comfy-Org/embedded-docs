> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/es.md)

El nodo SamplerDPMPP_SDE crea un sampler DPM++ SDE (Ecuación Diferencial Estocástica) para usar en el proceso de muestreo. Este sampler proporciona un método de muestreo estocástico con parámetros de ruido configurables y selección de dispositivo. Devuelve un objeto sampler que puede utilizarse en el pipeline de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sí | 0.0 - 100.0 | Controla la estocasticidad del proceso de muestreo (valor por defecto: 1.0) |
| `s_ruido` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido añadido durante el muestreo (valor por defecto: 1.0) |
| `r` | FLOAT | Sí | 0.0 - 100.0 | Un parámetro que influye en el comportamiento del muestreo (valor por defecto: 0.5) |
| `dispositivo_ruido` | COMBO | Sí | "gpu"<br>"cpu" | Selecciona el dispositivo donde se realizan los cálculos de ruido |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve un objeto sampler DPM++ SDE configurado para usar en pipelines de muestreo |