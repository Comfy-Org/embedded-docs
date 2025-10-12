> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/es.md)

Mejora la guía hacia estructuras detalladas utilizando otro conjunto de CFG negativo con capas omitidas. Esta versión genérica de SkipLayerGuidance puede utilizarse en todos los modelos DiT y está inspirada en Perturbed Attention Guidance. La implementación experimental original fue creada para SD3.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que aplicar la guía de capas omitidas |
| `capas_dobles` | STRING | Sí | - | Números de capa separados por comas para bloques dobles a omitir (por defecto: "7, 8, 9") |
| `capas_simples` | STRING | Sí | - | Números de capa separados por comas para bloques simples a omitir (por defecto: "7, 8, 9") |
| `escala` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de guía (por defecto: 3.0) |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 - 1.0 | Porcentaje inicial para la aplicación de guía (por defecto: 0.01) |
| `porcentaje_final` | FLOAT | Sí | 0.0 - 1.0 | Porcentaje final para la aplicación de guía (por defecto: 0.15) |
| `escala_reescalado` | FLOAT | Sí | 0.0 - 10.0 | Factor de escala de reescalado (por defecto: 0.0) |

**Nota:** Si tanto `double_layers` como `single_layers` están vacíos (no contienen números de capa), el nodo devuelve el modelo original sin aplicar ninguna guía.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con la guía de capas omitidas aplicada |
