> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/es.md)

Este nodo detecta automáticamente los modelos ubicados en la carpeta LoRA (incluyendo subcarpetas), siendo la ruta de modelo correspondiente `ComfyUI\models\loras`. Para más información, consulta Instalación de modelos LoRA.

El nodo Cargador de LoRA se utiliza principalmente para cargar modelos LoRA. Puedes pensar en los modelos LoRA como filtros que pueden dar a tus imágenes estilos, contenido y detalles específicos:

- Aplicar estilos artísticos concretos (como pintura con tinta)
- Añadir características de ciertos personajes (como personajes de videojuegos)
- Agregar detalles específicos a la imagen
Todo esto se puede lograr mediante LoRA.

Si necesitas cargar múltiples modelos LoRA, puedes encadenar directamente varios nodos, como se muestra a continuación:

## Entradas

| Parámetro | Tipo de dato | Descripción |
| --- | --- | --- |
| `modelo` | MODEL | Normalmente se utiliza para conectar al modelo base |
| `clip` | CLIP | Normalmente se utiliza para conectar al modelo CLIP |
| `nombre_lora` | COMBO[STRING] | Selecciona el nombre del modelo LoRA a utilizar |
| `fuerza_modelo` | FLOAT | Rango de valores de -100.0 a 100.0, normalmente se usa entre 0~1 para la generación diaria de imágenes. Valores más altos producen efectos de ajuste del modelo más pronunciados |
| `fuerza_clip` | FLOAT | Rango de valores de -100.0 a 100.0, normalmente se usa entre 0~1 para la generación diaria de imágenes. Valores más altos producen efectos de ajuste del modelo más pronunciados |

## Salidas

| Parámetro | Tipo de dato | Descripción |
| --- | --- | --- |
| `modelo` | MODEL | El modelo con los ajustes LoRA aplicados |
| `clip` | CLIP | La instancia CLIP con los ajustes LoRA aplicados |