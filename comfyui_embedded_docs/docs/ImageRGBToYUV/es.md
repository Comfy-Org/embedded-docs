> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/es.md)

El nodo ImageRGBToYUV convierte imágenes en color RGB al espacio de color YUV. Toma una imagen RGB como entrada y la separa en tres canales distintos: Y (luminancia), U (proyección azul) y V (proyección roja). Cada canal de salida se devuelve como una imagen en escala de grises separada que representa el componente YUV correspondiente.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen RGB de entrada que se convertirá al espacio de color YUV |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `Y` | IMAGE | El componente de luminancia (brillo) del espacio de color YUV |
| `U` | IMAGE | El componente de proyección azul del espacio de color YUV |
| `V` | IMAGE | El componente de proyección roja del espacio de color YUV |