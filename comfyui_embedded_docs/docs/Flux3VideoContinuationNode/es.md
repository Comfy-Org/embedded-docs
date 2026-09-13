# Flux 3 Continuación de Video

Este nodo continúa un clip de vídeo existente con FLUX 3: el nuevo clip prosigue a partir de los fotogramas finales del vídeo que proporciones. Carga tu clip de origen, envía el prompt y la configuración al servicio de generación, y devuelve el vídeo de continuación resultante una vez que está listo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `video` | El clip que se va a continuar. | VIDEO | Sí | Un solo clip de vídeo |
| `prompt` | Lo que debe mostrar la continuación; el prompt se interpreta y se expande antes de la generación. (predeterminado: "") | STRING | Sí | Texto no vacío (mínimo 1 carácter) |
| `aspect_ratio` | Relación de aspecto de salida. "auto" elige una a partir del prompt y las entradas. (predeterminado: "auto") | COMBO | Sí | "auto" (predeterminado)<br>Múltiples opciones predefinidas |
| `duration` | Duración del clip en segundos. "auto" ajusta la duración al contenido. (predeterminado: "auto") | COMBO | Sí | "auto" (predeterminado)<br>Valores numéricos en segundos |
| `resolution` | Resolución de salida. (predeterminado: "720p") | COMBO | Sí | "720p" (predeterminado)<br>"1080p"<br>Otras opciones predefinidas |
| `generate_audio` | Genera audio sincronizado (sonido ambiente, habla, efectos). Desactivado produce un vídeo sin pista de audio. (predeterminado: true) | BOOLEAN | Sí | true<br>false |
| `safety_tolerance` | Tolerancia de moderación; 0 es la más estricta. Las solicitudes que envían imágenes o vídeo tienen un límite de 2, independientemente de lo que configures aquí. (parámetro avanzado, predeterminado: 2) | INT | Sí | 0 - 4 (máximo efectivo: 2 para solicitudes de vídeo) |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. (predeterminado: 42) | INT | Sí | 0 - 4294967295 (0xFFFFFFFF) |

### Notas

- `prompt` debe contener al menos un carácter; de lo contrario, la generación falla. Aunque el campo tiene como valor predeterminado una cadena vacía, se requiere un prompt no vacío para ejecutar el nodo.
- `safety_tolerance` acepta cualquier valor de 0 a 4, pero como este nodo envía un vídeo a la API, la tolerancia efectiva se limita a 2 independientemente del valor seleccionado.
- Cuando `duration` se establece en un número, se convierte a un número entero de segundos. El valor especial "auto" permite que el servicio ajuste la duración al contenido.
- Las listas exactas de opciones para `aspect_ratio`, `duration` y `resolution` están definidas internamente por el nodo. Las opciones de resolución incluyen al menos "720p" (la predeterminada) y "1080p". El precio se calcula a partir de la `resolution` y la `duration` seleccionadas; "1080p" se factura a $0.7579 por segundo, mientras que las demás resoluciones se facturan a $0.5863 por segundo.
- `seed` solo controla si el nodo se vuelve a ejecutar; no se envía al servicio de generación.
- Los campos de autenticación e identificación del nodo (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) están ocultos y la plataforma los gestiona automáticamente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El clip de continuación generado por FLUX 3, que prosigue desde el final del vídeo de origen. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/es.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
