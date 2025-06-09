
El nodo VAESave está diseñado para guardar modelos VAE junto con sus metadatos, incluyendo prompts e información adicional en PNG, en un directorio de salida especificado. Este nodo encapsula la funcionalidad para serializar el estado del modelo y la información asociada en un archivo, facilitando la preservación y el intercambio de modelos entrenados.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `vae`     | VAE       | El modelo VAE que se va a guardar. Este parámetro es crucial ya que representa el modelo cuyo estado se va a serializar y almacenar. |
| `filename_prefix` | STRING   | Un prefijo para el nombre del archivo bajo el cual se guardarán el modelo y sus metadatos. Esto permite un almacenamiento organizado y una fácil recuperación de los modelos. |

## Salidas

El nodo no tiene tipos de salida.
