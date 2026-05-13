> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/es.md)

El nodo AudioAdjustVolume modifica el volumen del audio aplicando ajustes de ganancia en decibelios (dB). Toma una entrada de audio y aplica un factor de ganancia basado en el nivel de volumen especificado, donde los valores positivos aumentan el volumen y los negativos lo disminuyen. El nodo devuelve el audio modificado con la misma frecuencia de muestreo que el original.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO | Sí | - | La entrada de audio que se va a procesar |
| `volumen` | INT | Sí | -100 a 100 | Ajuste de volumen en decibelios (dB). 0 = sin cambios, +6 = duplicar, -6 = reducir a la mitad, etc. (valor predeterminado: 1) |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `audio` | AUDIO | El audio procesado con el nivel de volumen ajustado |

---
**Source fingerprint (SHA-256):** `0436765680671551239f7a89b575cdfb22590fbe662bdfe5da01bd1cd5c496ed`
