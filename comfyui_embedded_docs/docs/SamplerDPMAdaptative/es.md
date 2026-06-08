El nodo SamplerDPMAdaptative implementa un muestreador DPM (Modelo Probabilístico de Difusión) adaptativo que ajusta automáticamente los tamaños de paso durante el proceso de muestreo. Utiliza control de error basado en tolerancia para determinar tamaños de paso óptimos, equilibrando la eficiencia computacional con la precisión del muestreo. Este enfoque adaptativo ayuda a mantener la calidad mientras potencialmente reduce la cantidad de pasos necesarios.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `orden` | El orden del método de muestreo (predeterminado: 3) | INT | Sí | 2-3 |
| `rtol` | Tolerancia relativa para el control de error (predeterminado: 0.05) | FLOAT | Sí | 0.0-100.0 |
| `atol` | Tolerancia absoluta para el control de error (predeterminado: 0.0078) | FLOAT | Sí | 0.0-100.0 |
| `h_init` | Tamaño de paso inicial (predeterminado: 0.05) | FLOAT | Sí | 0.0-100.0 |
| `pcoeff` | Coeficiente proporcional para el control del tamaño de paso (predeterminado: 0.0) | FLOAT | Sí | 0.0-100.0 |
| `icoeff` | Coeficiente integral para el control del tamaño de paso (predeterminado: 1.0) | FLOAT | Sí | 0.0-100.0 |
| `dcoeff` | Coeficiente derivativo para el control del tamaño de paso (predeterminado: 0.0) | FLOAT | Sí | 0.0-100.0 |
| `aceptar_seguridad` | Factor de seguridad para la aceptación de pasos (predeterminado: 0.81) | FLOAT | Sí | 0.0-100.0 |
| `eta` | Parámetro de estocasticidad (predeterminado: 0.0) | FLOAT | Sí | 0.0-100.0 |
| `s_ruido` | Factor de escalado de ruido (predeterminado: 1.0) | FLOAT | Sí | 0.0-100.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | Devuelve una instancia configurada del muestreador DPM adaptativo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/es.md)

---
**Source fingerprint (SHA-256):** `2815ba8c3325d3d099de685edc99e9ff8e90736c1f4bd0188165969179cb99fa`
