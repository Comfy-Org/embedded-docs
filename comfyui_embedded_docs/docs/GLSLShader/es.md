> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/es.md)

El nodo **Shader GLSL** aplica código de fragment shader GLSL ES personalizado a imágenes de entrada. Permite escribir programas de shader que pueden procesar múltiples imágenes y aceptar parámetros uniformes (flotantes, enteros, booleanos y curvas) para crear efectos visuales complejos. El tamaño de salida puede determinarse por la primera imagen de entrada o configurarse manualmente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `fragment_shader` | STRING | Sí | N/A | Código fuente del fragment shader GLSL (compatible con GLSL ES 3.00 / WebGL 2.0). Valor predeterminado: un shader básico que genera la primera imagen de entrada. |
| `size_mode` | COMBO | Sí | `"from_input"`<br>`"custom"` | Tamaño de salida: 'from_input' usa las dimensiones de la primera imagen de entrada, 'custom' permite un tamaño manual. |
| `width` | INT | No | 1 a 16384 | Ancho de la imagen de salida cuando `size_mode` está configurado en `"custom"`. Valor predeterminado: 512. |
| `height` | INT | No | 1 a 16384 | Alto de la imagen de salida cuando `size_mode` está configurado en `"custom"`. Valor predeterminado: 512. |
| `images` | IMAGE | Sí | 1 a 8 imágenes | Imágenes de entrada que serán procesadas por el shader. Las imágenes están disponibles como `u_image0` a `u_image7` (sampler2D) en el código del shader. |
| `floats` | FLOAT | No | 0 a 8 flotantes | Valores uniformes de punto flotante para el shader. Los flotantes están disponibles como `u_float0` a `u_float7` en el código del shader. Valor predeterminado: 0.0. |
| `ints` | INT | No | 0 a 8 enteros | Valores uniformes enteros para el shader. Los enteros están disponibles como `u_int0` a `u_int7` en el código del shader. Valor predeterminado: 0. |
| `booleanos` | BOOLEAN | No | 0 a 8 booleanos | Valores uniformes booleanos para el shader. Los booleanos están disponibles como `u_bool0` a `u_bool7` (bool) en el código del shader. Valor predeterminado: Falso. |
| `curvas` | CURVE | No | 0 a 8 curvas | Valores uniformes de curva para el shader. Las curvas están disponibles como `u_curve0` a `u_curve7` (sampler2D, LUT 1D) en el código del shader. Se muestrean con `texture(u_curve0, vec2(x, 0.5)).r`. |

**Notas:**

* Los parámetros `width` y `height` solo son obligatorios y visibles cuando `size_mode` está configurado en `"custom"`.
* Se requiere al menos una imagen de entrada.
* El código del shader siempre tiene acceso a un uniforme `u_resolution` (vec2) que contiene las dimensiones de salida.
* Se puede proporcionar un máximo de 8 imágenes de entrada, 8 uniformes flotantes, 8 uniformes enteros, 8 uniformes booleanos y 8 uniformes de curva.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `IMAGE1` | IMAGE | Primera imagen de salida del shader. Disponible mediante `layout(location = 0) out vec4 fragColor0` en el código del shader. |
| `IMAGE2` | IMAGE | Segunda imagen de salida del shader. Disponible mediante `layout(location = 1) out vec4 fragColor1` en el código del shader. |
| `IMAGE3` | IMAGE | Tercera imagen de salida del shader. Disponible mediante `layout(location = 2) out vec4 fragColor2` en el código del shader. |
| `IMAGE3` | IMAGE | Cuarta imagen de salida del shader. Disponible mediante `layout(location = 3) out vec4 fragColor3` en el código del shader. |

---
**Source fingerprint (SHA-256):** `7830977409a5efab205b7c927eb83499a9e1e8299959b34643c9c3f1f586c058`
