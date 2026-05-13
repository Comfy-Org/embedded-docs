> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/es.md)

Este nodo crea un activo de imagen personal para el servicio Seedance 2.0 de ByteDance. Carga una imagen de entrada y la registra dentro de un grupo de activos especificado. Si no se proporciona un ID de grupo, iniciará un proceso de verificación de persona real en tu navegador para crear un nuevo grupo antes de agregar el activo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | | La imagen que se registrará como activo personal. |
| `group_id` | STRING | No | | Reutiliza un ID de grupo de activos Seedance existente para omitir la verificación humana repetida para la misma persona. Déjalo vacío para ejecutar la autenticación de persona real en el navegador y crear un nuevo grupo (predeterminado: vacío). |

**Restricciones de la imagen:**
*   El ancho de la imagen debe estar entre 300 y 6000 píxeles.
*   La altura de la imagen debe estar entre 300 y 6000 píxeles.
*   La relación de aspecto de la imagen debe estar entre 0.4:1 y 2.5:1.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `asset_id` | STRING | El identificador único para el activo de imagen recién creado. |
| `group_id` | STRING | El identificador para el grupo de activos. Será el `group_id` proporcionado o uno recién creado. |

---
**Source fingerprint (SHA-256):** `b8b7b4cbbc16a8bb0102982757496ad4e8140bd87155902668c0be0d8b4d3d98`
