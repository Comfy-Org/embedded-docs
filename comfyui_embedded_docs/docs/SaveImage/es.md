
**Función del nodo:** El nodo `Save Image-Guardar Imagen` se utiliza principalmente para guardar imágenes en la carpeta **output** de ComfyUI. Si solo desea previsualizar la imagen durante el proceso intermedio en lugar de guardarla, puede usar el nodo `Preview Image-Previsualizar Imagen`.
Ubicación de guardado predeterminada: `ComfyUI/output/`

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `images` | `IMAGE` | Las imágenes que se guardarán. Este parámetro es crucial ya que contiene directamente los datos de imagen que se procesarán y guardarán en disco. |
| `filename_prefix` | STRING   | El prefijo del nombre de archivo para las imágenes guardadas en la carpeta `ComfyUI/output/`. El valor predeterminado es `ComfyUI`, pero se puede personalizar. |

## Opciones del Menú Contextual

Después de completar la generación de la imagen, al hacer clic derecho en el menú correspondiente, se proporcionan las siguientes opciones y funciones específicas del nodo:

| Nombre de la Opción | Función |
|---------------------|----------|
| `Save Image-Guardar Imagen` | Guardar la imagen localmente |
| `Copy Image-Copiar Imagen` | Copiar la imagen al portapapeles |
| `Open Image-Abrir Imagen` | Abrir la imagen en una nueva pestaña del navegador |

Las imágenes guardadas generalmente están en formato PNG e incluyen todos los datos de generación de imágenes. Si desea utilizar el flujo de trabajo correspondiente para la regeneración, simplemente puede cargar la imagen correspondiente en ComfyUI para cargar el flujo de trabajo.
