# ComfyCloudMageFlowTurboTextToImageNode

Este nodo de Comfy Cloud genera una imagen a partir de un prompt de texto utilizando el flujo de trabajo Mage-Flow Turbo (`mage-flow-turbo/text-to-image`). Ejecuta una versión destilada del modelo Mage-Flow que genera la imagen en 4 pasos con un valor de cfg de 1, lo que requiere aproximadamente una séptima parte del tiempo de GPU de una pasada completa de Mage-Flow, lo que lo convierte en la variante pensada para la iteración rápida.

## Entradas

La clase del nodo en sí no declara widgets de entrada en el código fuente disponible; su esquema de entrada se hereda de la clase base compartida `_ComfyCloudMageFlowNode`, cuya definición no está incluida en el snapshot del código fuente. Según el resumen del nodo y el nombre del flujo de trabajo de texto a imagen, el nodo recibe un prompt de texto que describe la imagen a generar.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | El prompt de texto que describe la imagen a generar. El nombre exacto del parámetro lo establece el esquema base heredado `_ComfyCloudMageFlowNode` y puede diferir de esta etiqueta. | STRING | Sí | Texto libre |

Nota: Pueden existir parámetros de entrada adicionales en la definición del nodo base heredado, que no está disponible en el código fuente proporcionado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `IMAGE` | La imagen generada a partir del prompt de texto. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`
