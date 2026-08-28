# Flux 3 Continuación de Video

Este nodo continúa un videoclip existente con FLUX 3: el nuevo clip continúa desde los fotogramas finales del video que proporcionas. Sube tu videoclip de origen, envía el prompt y la configuración al servicio de generación y devuelve el video de continuación resultante una vez que esté listo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `video` | El clip a continuar. | VIDEO | Sí | Un solo videoclip |
| `prompt` | Lo que debe mostrar la continuación; el prompt se interpreta y expande antes de la generación. (por defecto: "") | STRING | Sí | Texto no vacío (mínimo 1 carácter) |
| `aspect_ratio` | Relación de aspecto de salida. 'auto' elige una según el prompt y las entradas. (por defecto: "auto") | COMBO | Sí | "auto" (por defecto)<br>Múltiples opciones predefinidas |
| `duration` | Duración del clip en segundos. 'auto' ajusta la duración al contenido. (por defecto: "auto") | COMBO | Sí | "auto" (por defecto)<br>Valores numéricos en segundos |
| `resolution` | Resolución de salida. (por defecto: "720p") | COMBO | Sí | "720p" (por defecto)<br>"1080p"<br>Otras opciones predefinidas |
| `generate_audio` | Generar audio sincronizado (ambiente, habla, efectos). Desactivado produce un video sin pista de audio. (por defecto: true) | BOOLEAN | Sí | true<br>false |
| `safety_tolerance` | Tolerancia de moderación, 0 es la más estricta. Las solicitudes que envían imágenes o video están limitadas a 2, sea cual sea el valor que establezcas aquí. (parámetro avanzado, por defecto: 2) | INT | Sí | 0 - 4 (máximo efectivo: 2 para solicitudes de video) |
| `seed` | Semilla para determinar si el nodo debe re-ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. (parámetro avanzado, por defecto: 42) | INT | Sí | 0 - 4294967295 (0xFFFFFFFF) |

### Notas

- `prompt` debe contener al menos un carácter, de lo contrario la generación falla. Aunque el campo tiene como valor predeterminado una cadena vacía, se requiere un prompt no vacío para ejecutar el nodo.
- `safety_tolerance` acepta cualquier valor de 0 a 4, pero dado que este nodo envía un video a la API, la tolerancia efectiva está limitada a 2 independientemente del valor seleccionado.
- Cuando `duration` se establece en un número, se convierte a un número entero de segundos. El valor especial "auto" permite que el servicio ajuste la duración al contenido.
- Las listas de opciones exactas para `aspect_ratio`, `duration` y `resolution` están definidas internamente por el nodo. Las opciones de resolución incluyen al menos "720p" (la predeterminada) y "1080p". El precio se calcula según la `resolution` y la `duration` seleccionadas; "1080p" se factura a $0.7579 por segundo, mientras que otras resoluciones se facturan a $0.5863 por segundo.
- Los campos de autenticación e identificación del nodo (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) están ocultos y son gestionados automáticamente por la plataforma.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El clip de continuación generado por FLUX 3, que continúa desde el final del video de origen. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/es.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
