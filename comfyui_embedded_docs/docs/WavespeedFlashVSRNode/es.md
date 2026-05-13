> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/es.md)

El nodo WavespeedFlashVSRNode es un escalador de video rápido y de alta calidad que aumenta la resolución y restaura la claridad de material de video de baja resolución o borroso. Procesa una entrada de video y genera un nuevo video a una resolución superior seleccionada por el usuario.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | N/A | El archivo de video de entrada que se va a escalar. Debe estar en formato contenedor MP4 con una duración entre 5 segundos y 10 minutos. |
| `resolución_objetivo` | STRING | Sí | `"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` | La resolución deseada para el video de salida escalado. |

**Restricciones de entrada:**

* El archivo de `video` de entrada debe estar en formato contenedor MP4.
* La duración del `video` de entrada debe estar entre 5 segundos y 10 minutos (600 segundos).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video escalado a la resolución objetivo seleccionada. |

---
**Source fingerprint (SHA-256):** `9a495889753ac866177921727228846d8ef9516c54ccd9aa425350b87237c397`
