El nodo Cargador CLIP está diseñado para cargar modelos CLIP, soportando diferentes tipos como difusión estable y cascada estable. Este nodo abstrae las complejidades de cargar y configurar modelos CLIP para su uso en diversas aplicaciones, proporcionando una forma simplificada de acceder a estos modelos con configuraciones específicas.
## Tipos de entrada

| Parámetro     | Tipo Comfy  | Descripción |
|---------------|-------------|-------------|
| `clip_name`   | `COMBO[STRING]` | Especifica el nombre del modelo CLIP que se va a cargar. Este nombre se utiliza para localizar el archivo del modelo dentro de una estructura de directorios predefinida. |
| `type`        | `COMBO[STRING]` | Determina el tipo de modelo CLIP a cargar, ofreciendo opciones entre 'difusión_estable' y 'cascada_estable'. Esto afecta cómo se inicializa y configura el modelo. |

## Tipos de salida

| Parámetro | Tipo Comfy | Descripción |
|-----------|------------|-------------|
| `clip`    | `CLIP`     | El modelo CLIP cargado, listo para su uso en tareas posteriores o procesamiento adicional. |