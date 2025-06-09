El nodo CheckpointLoader está diseñado para operaciones de carga avanzadas, específicamente para cargar puntos de control de modelos junto con sus configuraciones. Facilita la recuperación de componentes del modelo necesarios para inicializar y ejecutar modelos generativos, incluyendo configuraciones y puntos de control desde directorios especificados.

## Entradas

| Parámetro    | Tipo de Dato | Descripción |
|--------------|--------------|-------------|
| `config_name` | COMBO[STRING] | Especifica el nombre del archivo de configuración a utilizar. Esto es crucial para determinar los parámetros y configuraciones del modelo, afectando el comportamiento y rendimiento del mismo. |
| `ckpt_name`  | COMBO[STRING] | Indica el nombre del archivo de punto de control a cargar. Esto influye directamente en el estado del modelo que se está inicializando, impactando sus pesos y sesgos iniciales. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `model`   | MODEL     | Representa el modelo principal cargado desde el punto de control, listo para operaciones o inferencias adicionales. |
| `clip`    | CLIP      | Proporciona el componente del modelo CLIP, si está disponible y solicitado, cargado desde el punto de control. |
| `vae`     | VAE       | Entrega el componente del modelo VAE, si está disponible y solicitado, cargado desde el punto de control. |
