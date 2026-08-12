# Flux3TextToVideoNode

Genera un video con audio sincronizado a partir de un prompt de texto usando FLUX 3. El nodo envía tu prompt al servicio de FLUX 3, espera a que la generación termine y devuelve el videoclip completo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Lo que quieres, en lenguaje natural; el prompt se interpreta y expande antes de la generación. Describe el sonido ambiental, la música y el habla por separado para un audio en capas. (predeterminado: "") | STRING | Sí | Texto multilínea |
| `aspect_ratio` | Relación de aspecto de salida. 'auto' elige una según el prompt y las entradas. (predeterminado: "auto") | STRING | Sí | Múltiples opciones disponibles, incluyendo `"auto"` |
| `duration` | Duración del clip en segundos. 'auto' ajusta la duración al contenido. (predeterminado: "auto") | STRING | Sí | Múltiples opciones disponibles, incluyendo `"auto"` |
| `resolution` | Resolución de salida. (predeterminado: "720p") | STRING | Sí | `"720p"`<br>`"1080p"` |
| `generate_audio` | Generar audio sincronizado (ambiental, habla, efectos). Desactivado produce un video sin pista de audio. (predeterminado: True) | BOOLEAN | Sí | True<br>False |
| `safety_tolerance` | Tolerancia de moderación, 0 es la más estricta. Las solicitudes que envían imágenes o video tienen un tope de 2 sin importar lo que establezcas aquí. (predeterminado: 2) | INT | Sí | 0 a 4 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. (predeterminado: 42) | INT | Sí | 0 a 4294967295 |

Nota: La entrada `seed` incluye controles de Control After Generate en la interfaz. El precio mostrado se basa en `resolution` y `duration`: HD (720p) se cobra a $0.2431 por segundo y FHD (1080p) a $0.4147 por segundo. Cuando se elige una duración fija, se muestra el costo total estimado para el clip; cuando `duration` es "auto", se muestra la tarifa por segundo.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `video` | El videoclip generado, con audio sincronizado cuando `generate_audio` está habilitado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `35f5e5b1c6dd737afab78f53700997a458781d38149cb64fc60d86a86858b2e6`
