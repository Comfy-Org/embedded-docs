> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/es.md)

El nodo GLSL Shader aplica código personalizado de fragment shader GLSL ES a imágenes de entrada. Permite escribir programas de shader que pueden procesar múltiples imágenes y aceptar parámetros uniformes (flotantes y enteros) para crear efectos visuales complejos. El tamaño de salida puede determinarse por la primera imagen de entrada o establecerse manualmente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | Sí | N/A | Código fuente del fragment shader GLSL (compatible con GLSL ES 3.00 / WebGL 2.0). Por defecto: Un shader básico que devuelve la primera imagen de entrada. |
| `size_mode` | COMBO | Sí | `"from_input"`<br>`"custom"` | Tamaño de salida: 'from_input' usa las dimensiones de la primera imagen de entrada, 'custom' permite un tamaño manual. |
| `width` | INT | No | 1 a 16384 | El ancho de la imagen de salida cuando `size_mode` está configurado como `"custom"`. Por defecto: 512. |
| `height` | INT | No | 1 a 16384 | La altura de la imagen de salida cuando `size_mode` está configurado como `"custom"`. Por defecto: 512. |
| `images` | IMAGE | Sí | 1 a 8 imágenes | Imágenes de entrada para ser procesadas por el shader. Las imágenes están disponibles como `u_image0` a `u_image7` (sampler2D) en el código del shader. |
| `floats` | FLOAT | No | 0 a 8 flotantes | Valores uniformes de punto flotante para el shader. Los flotantes están disponibles como `u_float0` a `u_float7` en el código del shader. Por defecto: 0.0. |
| `ints` | INT | No | 0 a 8 enteros | Valores uniformes enteros para el shader. Los enteros están disponibles como `u_int0` a `u_int7` en el código del shader. Por defecto: 0. |

**Notas:**
*   Los parámetros `width` y `height` solo son obligatorios y visibles cuando `size_mode` está configurado como `"custom"`.
*   Se requiere al menos una imagen de entrada.
*   El código del shader siempre tiene acceso a un uniforme `u_resolution` (vec2) que contiene las dimensiones de salida.
*   Se puede proporcionar un máximo de 8 imágenes de entrada, 8 uniformes flotantes y 8 uniformes enteros.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | La primera imagen de salida del shader. Disponible mediante `layout(location = 0) out vec4 fragColor0` en el código del shader. |
| `IMAGE1` | IMAGE | La segunda imagen de salida del shader. Disponible mediante `layout(location = 1) out vec4 fragColor1` en el código del shader. |
| `IMAGE2` | IMAGE | La tercera imagen de salida del shader. Disponible mediante `layout(location = 2) out vec4 fragColor2` en el código del shader. |
| `IMAGE3` | IMAGE | La cuarta imagen de salida del shader. Disponible mediante `layout(location = 3) out vec4 fragColor3` en el código del shader. |