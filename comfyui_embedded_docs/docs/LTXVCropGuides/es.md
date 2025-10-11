> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/es.md)

El nodo LTXVCropGuides procesa entradas de condicionamiento y latentes para la generación de video mediante la eliminación de información de fotogramas clave y el ajuste de las dimensiones latentes. Recorta la imagen latente y la máscara de ruido para excluir las secciones de fotogramas clave, mientras limpia los índices de fotogramas clave de las entradas de condicionamiento tanto positivas como negativas. Esto prepara los datos para flujos de trabajo de generación de video que no requieren guía de fotogramas clave.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo que contiene información de guía para la generación |
| `negative` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo que contiene información de guía sobre qué evitar en la generación |
| `latent` | LATENT | Sí | - | La representación latente que contiene muestras de imagen y datos de máscara de ruido |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo procesado con los índices de fotogramas clave limpiados |
| `negative` | CONDITIONING | El condicionamiento negativo procesado con los índices de fotogramas clave limpiados |
| `latent` | LATENT | La representación latente recortada con muestras y máscara de ruido ajustadas |