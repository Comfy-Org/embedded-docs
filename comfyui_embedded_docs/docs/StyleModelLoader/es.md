Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/style_models`,
y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml.
A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

## Documentación

| Campo                | Descripción                                                                                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre de la clase   | `StyleModelLoader`                                                                                                                                                                                          |
| Categoría            | `loaders`                                                                                                                                                                                                   |
| Nodo de salida       | `False`                                                                                                                                                                                                     |
| Descripción          | El nodo StyleModelLoader está diseñado para cargar un modelo de estilo desde una ruta especificada. Se centra en recuperar e inicializar modelos de estilo que pueden usarse para aplicar estilos artísticos específicos a las imágenes.            |

## Entradas

| Campo               | Descripción                                                                                                                                                                                                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `style_model_name`  | Especifica el nombre del modelo de estilo a cargar. Este nombre se utiliza para localizar el archivo del modelo dentro de una estructura de directorios predefinida, permitiendo la carga dinámica de diferentes modelos de estilo.                  |
| Comfy dtype         | `COMBO[STRING]`                                                                                                                                                                                             |
| Python dtype        | `str`                                                                                                                                                                                                       |

## Salidas

| Campo               | Descripción                                                                                                                                                                                                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `style_model`       | Devuelve el modelo de estilo cargado, listo para su uso en la aplicación de estilos a imágenes. Esto permite la personalización dinámica de los resultados visuales aplicando diferentes estilos artísticos.                                        |
| Comfy dtype         | `STYLE_MODEL`                                                                                                                                                                                               |
| Python dtype        | `StyleModel`                                                                                                                                                                                                |
