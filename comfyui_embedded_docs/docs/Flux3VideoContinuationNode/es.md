# Flux3VideoContinuationNode

Este nodo continúa un videoclip existente con FLUX 3, de modo que el nuevo clip continúa desde los fotogramas finales del video que proporcionas. Sube tu clip de origen, envía el prompt y la configuración al servicio de generación, y devuelve el video de continuación resultante una vez que esté listo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `video` | El clip a continuar. | VIDEO | Sí | Clip de video único |
| `prompt` | Lo que debe mostrar la continuación; el prompt se interpreta y expande antes de la generación. (predeterminado: "") | STRING | Sí | Texto no vacío (mínimo 1 carácter) |
| `aspect_ratio` | Relación de aspecto de salida. 'auto' elige una a partir del prompt y las entradas. (predeterminado: "auto") | STRING | Sí | Múltiples opciones predefinidas (predeterminado: "auto") |
| `duration` | Duración del clip en segundos. 'auto' ajusta la duración al contenido. (predeterminado: "auto") | STRING | Sí | "auto" (predeterminado)<br>Valores numéricos en segundos |
| `resolution` | Resolución de salida. (predeterminado: "720p") | STRING | Sí | Múltiples opciones predefinidas (predeterminado: "720p") |
| `generate_audio` | Generar audio sincronizado (ambiente, habla, efectos). Desactivado produce un video sin pista de audio. (predeterminado: true) | BOOLEAN | Sí | true<br>false |
| `safety_tolerance` | Tolerancia de moderación, 0 es la más estricta. Las solicitudes que envían imágenes o video están limitadas a 2 sin importar lo que establezcas aquí. (parámetro avanzado, predeterminado: 2) | INT | Sí | 0 - 4 (máximo efectivo: 2 para solicitudes de video) |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. (parámetro avanzado, predeterminado: 42) | INT | Sí | 0 - 4294967295 (0xFFFFFFFF) |

### Notas

- `prompt` debe contener al menos un carácter; de lo contrario, la generación falla. Aunque el campo tiene como valor predeterminado una cadena vacía, se requiere un prompt no vacío para ejecutar el nodo.
- `safety_tolerance` acepta cualquier valor de 0 a 4, pero dado que este nodo envía un video a la API, la tolerancia efectiva está limitada a 2 independientemente del valor seleccionado.
- Cuando `duration` se establece en un número, se convierte en un número entero de segundos. El valor especial "auto" permite que el servicio ajuste la duración al contenido.
- Las listas exactas de opciones para `aspect_ratio`, `duration` y `resolution` están definidas internamente por el nodo. Las opciones de resolución incluyen al menos "720p" (el predeterminado) y "1080p", que utiliza una tarifa de precios diferente.
- Los campos de autenticación e identificación del nodo (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) están ocultos y son gestionados automáticamente por la plataforma.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El clip de continuación generado por FLUX 3, que continúa desde el final del video de origen. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/es.md)

---
**Source fingerprint (SHA-256):** `4b3a3df86b870edd696d10d352c7123b9c6c60ce0b57910529fca60615efa9f9`
