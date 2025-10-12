Este nodo detecta automáticamente los modelos ubicados en la carpeta LoRA (incluyendo subcarpetas) con la ruta del modelo correspondiente `ComfyUI\models\loras`.

El nodo Cargador LoRA se utiliza principalmente para cargar modelos LoRA. Puede pensar en los modelos LoRA como filtros que pueden dar a sus imágenes estilos, contenidos y detalles específicos:

- Aplicar estilos artísticos específicos (como pintura a tinta)
- Añadir características de ciertos personajes (como personajes de juegos)
- Añadir detalles específicos a la imagen
Todo esto se puede lograr a través de LoRA.

Si necesita cargar múltiples modelos LoRA, puede encadenar directamente varios nodos, como se muestra a continuación:

## Entradas

| Nombre del Parámetro | Tipo de Datos | Función |
| --- | --- | --- |
| `modelo` | MODEL | Típicamente usado para conectar al modelo base |
| `clip` | CLIP | Típicamente usado para conectar al modelo CLIP |
| `nombre_lora` | COMBO[STRING] | Seleccionar el nombre del modelo LoRA a utilizar |
| `fuerza_modelo` | FLOAT | Rango de valores de -100.0 a 100.0, típicamente usado entre 0~1 para la generación diaria de imágenes. Valores más altos resultan en efectos de ajuste más pronunciados |
| `fuerza_clip` | FLOAT | Rango de valores de -100.0 a 100.0, típicamente usado entre 0~1 para la generación diaria de imágenes. Valores más altos resultan en efectos de ajuste más pronunciados |

## Salidas

| Nombre del Parámetro | Tipo de Datos | Función |
| --- | --- | --- |
| `modelo` | MODEL | El modelo con ajustes LoRA aplicados |
| `clip` | CLIP | La instancia CLIP con ajustes LoRA aplicados |
