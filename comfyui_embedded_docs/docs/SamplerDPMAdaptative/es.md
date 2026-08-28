# SamplerDPMAdaptative

El nodo SamplerDPMAdaptative implementa un muestreador DPM (Modelo Probabilístico de Difusión) adaptativo que ajusta automáticamente los tamaños de paso durante el proceso de muestreo. Utiliza control de error basado en tolerancia para determinar los tamaños de paso óptimos, equilibrando la eficiencia computacional con la precisión del muestreo. Este enfoque adaptativo ayuda a mantener la calidad y potencialmente reduce el número de pasos necesarios.

## Entradas

| Parámetro | Descripción | Tipo de dato | ¿Requerido? | Rango |
| --- | --- | --- | --- | --- |
| `orden` | El orden del método de muestreo (por defecto: 3) | INT | Sí | 2-3 |
| `rtol` | Tolerancia relativa para el control de error (por defecto: 0.05) | FLOAT | Sí | 0.0-100.0 |
| `atol` | Tolerancia absoluta para el control de error (por defecto: 0.0078) | FLOAT | Sí | 0.0-100.0 |
| `h_init` | Tamaño de paso inicial (por defecto: 0.05) | FLOAT | Sí | 0.0-100.0 |
| `pcoeff` | Coeficiente proporcional para el control del tamaño de paso (por defecto: 0.0) | FLOAT | Sí | 0.0-100.0 |
| `icoeff` | Coeficiente integral para el control del tamaño de paso (por defecto: 1.0) | FLOAT | Sí | 0.0-100.0 |
| `dcoeff` | Coeficiente derivativo para el control del tamaño de paso (por defecto: 0.0) | FLOAT | Sí | 0.0-100.0 |
| `aceptar_seguridad` | Factor de seguridad para la aceptación de pasos (por defecto: 0.81) | FLOAT | Sí | 0.0-100.0 |
| `eta` | Parámetro de estocasticidad (por defecto: 0.0) | FLOAT | Sí | 0.0-100.0 |
| `s_ruido` | Factor de escala de ruido (por defecto: 1.0) | FLOAT | Sí | 0.0-100.0 |

Todas las entradas son parámetros avanzados que se utilizan para ajustar finamente el comportamiento del muestreo adaptativo.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `sampler` | Devuelve una instancia de muestreador adaptativo DPM configurada | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/es.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
