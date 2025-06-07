Esta documentación es para el nodo original `Apply ControlNet(Advanced)`. El nodo más antiguo `Apply ControlNet` ha sido renombrado a `Apply ControlNet(Old)`. Aunque aún puedes ver el nodo `Apply ControlNet(Old)` en muchas carpetas de flujo de trabajo que descargues de comfyui.org por razones de compatibilidad, ya no puedes encontrar el nodo `Apply ControlNet(Old)` a través de búsqueda o lista de nodos. Por favor, usa el nodo `Apply ControlNet` en su lugar.

Este nodo aplica un ControlNet a una imagen y acondicionamiento dados, ajustando los atributos de la imagen según los parámetros de la red de control y una fuerza especificada, como Depth, OpenPose, Canny, HED, etc.

El uso de controlNet requiere preprocesamiento de imágenes de entrada. Como los nodos iniciales de ComfyUI no vienen con preprocesadores y modelos controlNet, primero instale los preprocesadores ContrlNet [descargue los preprocesadores aquí](https://github.com/Fannovel16/comfy_controlnet_preprocessors) y los modelos controlNet correspondientes.

## Entradas

| Parámetro | Tipo de datos | Función |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Datos de acondicionamiento positivo, del `Codificador de texto CLIP u otras entradas de acondicionamiento |
| `negative` | `CONDITIONING` | Datos de acondicionamiento negativo, del `Codificador de texto CLIP` u otras entradas de acondicionamiento |
| `control_net` | `CONTROL_NET` | El modelo controlNet a aplicar, típicamente entrada desde el `Cargador de ControlNet` |
| `image` | `IMAGE` | Imagen para aplicación de controlNet, necesita ser procesada por el preprocesador |
| `vae` | `VAE` | Entrada del modelo Vae |
| `strength` | `FLOAT` | Controla la fuerza de los ajustes de la red, rango de valores 0~10. Los valores recomendados entre 0.5~1.5 son razonables. Valores más bajos permiten más libertad al modelo, valores más altos imponen restricciones más estrictas. Valores demasiado altos pueden resultar en imágenes extrañas. |
| `start_percent` | `FLOAT` | Valor 0.000~1.000, determina cuándo comenzar a aplicar controlNet como porcentaje, por ejemplo, 0.2 significa que la guía de ControlNet comenzará a influir en la generación de imágenes al 20% del proceso de difusión |
| `end_percent` | `FLOAT` | Valor 0.000~1.000, determina cuándo dejar de aplicar controlNet como porcentaje, por ejemplo, 0.8 significa que la guía de ControlNet dejará de influir en la generación de imágenes al 80% del proceso de difusión |

## Salidas

| Parámetro | Tipo de datos | Función |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Datos de acondicionamiento positivo procesados por ControlNet, pueden enviarse a los siguientes nodos ControlNet o K Sampler |
| `negative` | `CONDITIONING` | Datos de acondicionamiento negativo procesados por ControlNet, pueden enviarse a los siguientes nodos ControlNet o K Sampler |

Si desea usar **modelos de estilo T2IAdaptor**, utilice el nodo `Apply Style Model` en su lugar
