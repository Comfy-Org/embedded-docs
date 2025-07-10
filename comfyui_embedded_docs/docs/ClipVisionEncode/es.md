El nodo `CLIP Vision Encode` es un nodo de codificación de imágenes en ComfyUI, utilizado para convertir imágenes de entrada en vectores de características visuales mediante el modelo CLIP Vision. Este nodo es un puente importante que conecta la comprensión de imágenes y textos, y se utiliza ampliamente en varios flujos de trabajo de generación y procesamiento de imágenes con IA.

**Funcionalidad del nodo**

- **Extracción de características de imagen**: Convierte imágenes de entrada en vectores de características de alta dimensión
- **Puente multimodal**: Proporciona una base para el procesamiento conjunto de imágenes y textos
- **Generación condicional**: Proporciona condiciones visuales para la generación condicional basada en imágenes

## Entradas

| Nombre del parámetro | Tipo de dato   | Descripción                                                      |
| -------------------- | -------------  | --------------------------------------------------------------- |
| `clip_vision`        | CLIP_VISION    | Modelo CLIP vision, normalmente cargado mediante el nodo CLIPVisionLoader |
| `image`              | IMAGE          | La imagen de entrada a codificar                                 |
| `crop`               | Dropdown       | Método de recorte de imagen, opciones: center (recorte centrado), none (sin recorte) |

## Salidas

| Nombre de salida     | Tipo de dato         | Descripción                |
| -------------------- | ------------------- | -------------------------- |
| SALIDA_CLIP_VISION   | CLIP_VISION_OUTPUT  | Características visuales codificadas    |

Este objeto de salida contiene:

- `last_hidden_state`: El último estado oculto
- `image_embeds`: Vector de incrustación de la imagen
- `penultimate_hidden_states`: El penúltimo estado oculto
- `mm_projected`: Resultado de proyección multimodal (si está disponible)
