El nodo `Guardar CLIP` está diseñado para guardar modelos de codificador de texto CLIP en formato SafeTensors. Este nodo forma parte de flujos de trabajo avanzados de fusión de modelos y se utiliza típicamente en conjunto con nodos como `CLIPMergeSimple` y `CLIPMergeAdd`. Los archivos guardados utilizan el formato SafeTensors para garantizar la seguridad y compatibilidad.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Valor Predeterminado | Descripción |
|-----------|--------------|-----------|---------------------|-------------|
| clip | CLIP | Sí | - | El modelo CLIP que se va a guardar |
| prefijo_nombre_archivo | STRING | Sí | "clip/ComfyUI" | La ruta del prefijo para el archivo guardado |
| prompt | PROMPT | Oculto | - | Información del prompt del flujo de trabajo (para metadatos) |
| extra_pnginfo | EXTRA_PNGINFO | Oculto | - | Información adicional de PNG (para metadatos) |

## Salidas

Este nodo no tiene tipos de salida definidos. Guarda los archivos procesados en la carpeta `ComfyUI/output/`.

### Estrategia de Guardado Múltiple

El nodo guarda diferentes componentes según el tipo de modelo CLIP:

| Tipo de Prefijo | Sufijo del Archivo | Descripción |
|-----------------|-------------------|-------------|
| `clip_l.` | `_clip_l` | Codificador de texto CLIP-L |
| `clip_g.` | `_clip_g` | Codificador de texto CLIP-G |
| Prefijo vacío | Sin sufijo | Otros componentes CLIP |

## Notas de Uso

1. **Ubicación de Archivos**: Todos los archivos se guardan en el directorio `ComfyUI/output/`
2. **Formato de Archivo**: Los modelos se guardan en formato SafeTensors para seguridad
3. **Metadatos**: Incluye información del flujo de trabajo y metadatos PNG si están disponibles
4. **Convención de Nombres**: Utiliza el prefijo especificado más los sufijos apropiados según el tipo de modelo
