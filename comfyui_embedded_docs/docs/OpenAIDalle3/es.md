> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/es.md)

Genera imágenes de forma síncrona mediante el endpoint DALL·E 3 de OpenAI. Este nodo toma un texto descriptivo y crea imágenes correspondientes utilizando el modelo DALL·E 3 de OpenAI, permitiéndole especificar la calidad, el estilo y las dimensiones de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Texto descriptivo para DALL·E (valor por defecto: "") |
| `seed` | INT | No | 0 a 2147483647 | aún no implementado en el backend (valor por defecto: 0) |
| `calidad` | COMBO | No | "standard"<br>"hd" | Calidad de la imagen (valor por defecto: "standard") |
| `estilo` | COMBO | No | "natural"<br>"vivid" | Vivid hace que el modelo tienda a generar imágenes hiperrealistas y dramáticas. Natural hace que el modelo produzca imágenes más naturales, menos hiperrealistas. (valor por defecto: "natural") |
| `tamaño` | COMBO | No | "1024x1024"<br>"1024x1792"<br>"1792x1024" | Tamaño de la imagen (valor por defecto: "1024x1024") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La imagen generada por DALL·E 3 |
