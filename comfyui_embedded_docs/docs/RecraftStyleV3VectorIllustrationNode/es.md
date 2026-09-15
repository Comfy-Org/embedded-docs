# RecraftStyleV3VectorIllustrationNode

Este nodo selecciona un estilo para la API de Recraft, específicamente la categoría de estilo de ilustración vectorial. Opcionalmente, puedes elegir un subestilo más específico dentro de esa categoría. El nodo genera un objeto de configuración de estilo que se puede pasar a otros nodos Recraft.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `substyle` | Un estilo más específico dentro de la categoría de ilustración vectorial. Las opciones disponibles son los subestilos definidos para el estilo `vector_illustration` por la API de Recraft. Si no se elige ningún subestilo, se utiliza el estilo base `vector_illustration`. | COMBO | Sí | Múltiples opciones disponibles (lista de subestilos cargada dinámicamente para el estilo `vector_illustration`) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|---------------|
| `recraft_style` | Un objeto de configuración de estilo de Recraft que contiene el estilo de ilustración vectorial seleccionado y el subestilo opcional. Se puede conectar a otros nodos Recraft. | STYLEV3 |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/es.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`
