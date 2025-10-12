> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/es.md)

El nodo SamplerDPMAdaptative implementa un muestreador DPM (Modelo Probabilístico de Difusión) adaptativo que ajusta automáticamente los tamaños de paso durante el proceso de muestreo. Utiliza control de errores basado en tolerancia para determinar los tamaños de paso óptimos, equilibrando la eficiencia computacional con la precisión del muestreo. Este enfoque adaptativo ayuda a mantener la calidad mientras potencialmente reduce el número de pasos necesarios.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `orden` | INT | Sí | 2-3 | El orden del método del muestreador (por defecto: 3) |
| `rtol` | FLOAT | Sí | 0.0-100.0 | Tolerancia relativa para el control de errores (por defecto: 0.05) |
| `atol` | FLOAT | Sí | 0.0-100.0 | Tolerancia absoluta para el control de errores (por defecto: 0.0078) |
| `h_init` | FLOAT | Sí | 0.0-100.0 | Tamaño de paso inicial (por defecto: 0.05) |
| `pcoeff` | FLOAT | Sí | 0.0-100.0 | Coeficiente proporcional para el control del tamaño de paso (por defecto: 0.0) |
| `icoeff` | FLOAT | Sí | 0.0-100.0 | Coeficiente integral para el control del tamaño de paso (por defecto: 1.0) |
| `dcoeff` | FLOAT | Sí | 0.0-100.0 | Coeficiente derivativo para el control del tamaño de paso (por defecto: 0.0) |
| `aceptar_seguridad` | FLOAT | Sí | 0.0-100.0 | Factor de seguridad para la aceptación de pasos (por defecto: 0.81) |
| `eta` | FLOAT | Sí | 0.0-100.0 | Parámetro de estocasticidad (por defecto: 0.0) |
| `s_ruido` | FLOAT | Sí | 0.0-100.0 | Factor de escalado de ruido (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve una instancia de muestreador DPM adaptativo configurado |