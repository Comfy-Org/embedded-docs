# Aplicar ControlNet (ANTIGUO)

El uso de ControlNet requiere el preprocesamiento de las imágenes de entrada. Dado que los nodos iniciales de ComfyUI no incluyen preprocesadores ni modelos ControlNet, instale primero los preprocesadores de ControlNet [descargue los preprocesadores aquí](https://github.com/Fannovel16/comfy_controlnet_preprocessors) y los modelos ControlNet correspondientes.

## Entradas

| Parámetro | Tipo de Dato | Función |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Datos de condicionamiento positivo, provenientes del Codificador de Texto CLIP u otras entradas de condicionamiento |
| `negative` | `CONDITIONING` | Datos de condicionamiento negativo, provenientes del Codificador de Texto CLIP u otras entradas de condicionamiento |
| `control_net` | `CONTROL_NET` | El modelo ControlNet a aplicar, generalmente ingresado desde el Cargador de ControlNet |
| `imagen` | `IMAGE` | Imagen para la aplicación de ControlNet, debe ser procesada por un preprocesador |
| `vae` | `VAE` | Entrada del modelo VAE |
| `fuerza` | `FLOAT` | Controla la fuerza de los ajustes de la red, rango de valores 0~10. Se recomiendan valores entre 0.5~1.5 como razonables. Valores más bajos permiten mayor libertad al modelo; valores más altos imponen restricciones más estrictas. Valores demasiado altos pueden generar imágenes extrañas. Puede probar y ajustar este valor para afinar la influencia de la red de control. |
| `start_percent` | `FLOAT` | Valor 0.000~1.000, determina cuándo comenzar a aplicar ControlNet como porcentaje. Por ejemplo, 0.2 significa que la guía de ControlNet comenzará a influir en la generación de la imagen al 20% del proceso de difusión |
| `end_percent` | `FLOAT` | Valor 0.000~1.000, determina cuándo detener la aplicación de ControlNet como porcentaje. Por ejemplo, 0.8 significa que la guía de ControlNet dejará de influir en la generación de la imagen al 80% del proceso de difusión |

### Salidas

| Parámetro | Tipo de Dato | Función |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Datos de condicionamiento positivo procesados por ControlNet, pueden enviarse al siguiente nodo de ControlNet o al Muestreador K |
| `negative` | `CONDITIONING` | Datos de condicionamiento negativo procesados por ControlNet, pueden enviarse al siguiente nodo de ControlNet o al Muestreador K |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/es.md)
