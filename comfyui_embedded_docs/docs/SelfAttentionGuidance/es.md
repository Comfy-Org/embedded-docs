> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/es.md)

El nodo Self-Attention Guidance aplica guía a los modelos de difusión modificando el mecanismo de atención durante el proceso de muestreo. Captura las puntuaciones de atención de los pasos de eliminación de ruido incondicionales y las utiliza para crear mapas de guía difusos que influyen en el resultado final. Esta técnica ayuda a guiar el proceso de generación aprovechando los patrones de atención propios del modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión al que aplicar la guía de auto-atención |
| `scale` | FLOAT | No | -2.0 a 5.0 | La intensidad del efecto de guía de auto-atención (valor por defecto: 0.5) |
| `blur_sigma` | FLOAT | No | 0.0 a 10.0 | La cantidad de desenfoque aplicado para crear el mapa de guía (valor por defecto: 2.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con la guía de auto-atención aplicada |

**Nota:** Este nodo es actualmente experimental y tiene limitaciones con lotes divididos. Solo puede guardar puntuaciones de atención de una llamada UNet y puede no funcionar correctamente con tamaños de lote más grandes.