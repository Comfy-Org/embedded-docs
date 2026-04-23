> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/es.md)

Este nodo crea un recurso de video personal para Seedance 2.0. Sube tu video de entrada y lo registra dentro de un grupo de recursos especificado. Si no proporcionas un ID de grupo, te guiará a través de un proceso de verificación de persona real en tu navegador para crear primero un nuevo grupo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | Video a registrar como recurso personal. |
| `group_id` | STRING | No | - | Reutiliza un ID de grupo de recursos de Seedance existente para omitir la verificación humana repetida para la misma persona. Déjalo vacío para ejecutar la autenticación de persona real en el navegador y crear un nuevo grupo. (valor por defecto: cadena vacía) |

**Restricciones del Video:**
*   **Duración:** Debe estar entre 2 y 15 segundos.
*   **Dimensiones:** El ancho y el alto deben estar cada uno entre 300 y 6000 píxeles.
*   **Relación de Aspecto:** La relación ancho-alto debe estar entre 0.4 y 2.5.
*   **Píxeles Totales:** El número total de píxeles (ancho × alto) debe estar entre 409,600 y 927,408.
*   **Tasa de Cuadros:** Debe estar entre 24 y 60 cuadros por segundo (FPS).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `asset_id` | STRING | El identificador único para el recurso de video recién creado. |
| `group_id` | STRING | El identificador del grupo de recursos que contiene el nuevo video. Este será el `group_id` proporcionado o uno recién creado. |