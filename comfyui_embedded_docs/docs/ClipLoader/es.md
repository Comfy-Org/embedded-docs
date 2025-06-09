Este nodo se utiliza principalmente para cargar modelos de codificador de texto CLIP de forma independiente.
Los archivos de modelo se pueden detectar en las siguientes rutas:

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> Si guardas un modelo después de haber iniciado ComfyUI, necesitarás actualizar el frontend de ComfyUI para obtener la lista más reciente de rutas de archivos de modelo

Formatos de modelo soportados:

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

Para más detalles sobre la carga de archivos de modelo más recientes, consulta [folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)

## Entradas

| Parámetro     | Tipo de Dato  | Descripción |
|---------------|---------------|-------------|
| `nombre_clip` | COMBO[STRING] | Especifica el nombre del modelo CLIP que se va a cargar. Este nombre se utiliza para localizar el archivo del modelo dentro de una estructura de directorios predefinida. |
| `tipo`        | COMBO[STRING] | Determina el tipo de modelo CLIP a cargar. A medida que ComfyUI admite más modelos, se añadirán nuevos tipos aquí. Consulta la definición de la clase `CLIPLoader` en [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) para más detalles. |
| `dispositivo` | COMBO[STRING] | Elige el dispositivo para cargar el modelo CLIP. `default` ejecutará el modelo en GPU, mientras que seleccionar `CPU` forzará la carga en CPU. |

### Opciones de Dispositivo Explicadas

**Cuándo elegir "default":**

- Tienes suficiente memoria GPU
- Quieres el mejor rendimiento
- Dejas que el sistema optimice automáticamente el uso de memoria

**Cuándo elegir "cpu":**

- Memoria GPU insuficiente
- Necesitas reservar memoria GPU para otros modelos (como UNet)
- Ejecutando en un entorno con poca VRAM
- Necesidades de depuración o propósitos especiales

**Impacto en el Rendimiento**

La ejecución en CPU será mucho más lenta que en GPU, pero puede ahorrar valiosa memoria GPU para otros componentes más importantes del modelo. En entornos con restricciones de memoria, poner el modelo CLIP en CPU es una estrategia de optimización común.

### Combinaciones Soportadas

| Tipo de Modelo | Codificador Correspondiente |
|----------------|----------------------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

A medida que ComfyUI se actualiza, estas combinaciones pueden expandirse. Para más detalles, consulta la definición de la clase `CLIPLoader` en [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `clip`    | CLIP         | El modelo CLIP cargado, listo para su uso en tareas posteriores o procesamiento adicional. |

## Notas Adicionales

Los modelos CLIP juegan un papel fundamental como codificadores de texto en ComfyUI, siendo responsables de convertir los prompts de texto en representaciones numéricas que los modelos de difusión pueden entender. Puedes pensar en ellos como traductores, responsables de traducir tu texto a un lenguaje que los modelos grandes pueden entender. Por supuesto, diferentes modelos tienen sus propios "dialectos", por lo que se necesitan diferentes codificadores CLIP entre diferentes arquitecturas para completar el proceso de codificación de texto.
