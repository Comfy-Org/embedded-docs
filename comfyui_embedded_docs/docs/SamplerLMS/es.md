> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/es.md)

El nodo SamplerLMS crea un muestreador de Mínimos Cuadrados Medios (LMS) para usar en modelos de difusión. Genera un objeto muestreador que puede utilizarse en el proceso de muestreo, permitiéndote controlar el orden del algoritmo LMS para la estabilidad y precisión numérica.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `orden` | INT | Sí | 1 a 100 | El parámetro de orden para el algoritmo del muestreador LMS, que controla la precisión y estabilidad del método numérico (por defecto: 4) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Un objeto muestreador LMS configurado que puede usarse en el pipeline de muestreo |
