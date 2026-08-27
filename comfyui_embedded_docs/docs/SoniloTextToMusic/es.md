# Sonilo Texto a Música

El nodo Sonilo Text to Music genera música a partir de una descripción de texto utilizando el modelo de IA de Sonilo. Usted proporciona un prompt que describe la música que desea, y el nodo envía una solicitud al servicio de Sonilo para crear un archivo de audio. Puede establecer una duración objetivo para el clip generado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Prompt de texto que describe la música a generar. Debe contener de 1 a 1000 caracteres después de recortar los espacios en blanco. | STRING | Sí | N/A |
| `duration` | Duración objetivo en segundos. Máximo: 6 minutos. Predeterminado: 30. | INT | No | 1 a 360 |
| `seed` | Semilla para reproducibilidad. Actualmente ignorada por el servicio de Sonilo, pero se mantiene para la consistencia del grafo. Predeterminado: 0. | INT | No | 0 a 18446744073709551615 |

**Notas:**
- La entrada `seed` se proporciona para la consistencia del flujo de trabajo, pero actualmente no afecta a la salida del servicio de Sonilo.
- El uso se factura a $0.0025 por segundo de la `duration` solicitada.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `audio` | La música generada como archivo de audio. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/es.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
