# Flux 3 Texto a Video

Genera un video con audio sincronizado a partir de un prompt de texto usando FLUX 3. El nodo envía tu prompt al servicio de FLUX 3, espera a que la generación termine y devuelve el clip de video completado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Lo que deseas, en lenguaje natural; el prompt se interpreta y expande antes de la generación. Describe el sonido ambiente, la música y el habla por separado para obtener audio en capas. (predeterminado: "") | STRING | Sí | Texto multilínea |
| `aspect_ratio` | Relación de aspecto de salida. 'auto' elige una a partir del prompt y las entradas. (predeterminado: "auto") | COMBO | Sí | Múltiples opciones disponibles, incluyendo `"auto"` |
| `duration` | Duración del clip en segundos. 'auto' ajusta la duración al contenido. (predeterminado: "auto") | COMBO | Sí | Múltiples opciones disponibles, incluyendo `"auto"` |
| `resolution` | Resolución de salida. (predeterminado: "720p") | COMBO | Sí | `"720p"`<br>`"1080p"` |
| `generate_audio` | Generar audio sincronizado (ambiente, habla, efectos). Desactivado produce un video sin pista de audio. (predeterminado: True) | BOOLEAN | Sí | True<br>False |
| `safety_tolerance` | Tolerancia de moderación, 0 es la más estricta. Las solicitudes que envían imágenes o video están limitadas a 2 sin importar lo que configures aquí. (predeterminado: 2) | INT | Sí | 0 a 4 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. (predeterminado: 42) | INT | Sí | 0 a 4294967295 |

Nota: La entrada `seed` incluye controles de Control After Generate en la interfaz. El precio mostrado se basa en `resolution` y `duration`: HD (720p) se cobra a $0.2431 por segundo y FHD (1080p) a $0.4147 por segundo. Cuando se elige una duración fija, se muestra el costo total estimado para el clip; cuando `duration` es "auto", se muestra la tarifa por segundo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El clip de video generado, con audio sincronizado cuando `generate_audio` está habilitado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `9957c78291c320b1a8a6a9c0edeefae5f1ccc21a6b58f0b39069c2df8decd100`
