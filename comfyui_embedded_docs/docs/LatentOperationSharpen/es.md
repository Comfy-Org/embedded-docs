> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/es.md)

El nodo LatentOperationSharpen aplica un efecto de realce a las representaciones latentes utilizando un kernel gaussiano. Funciona normalizando los datos latentes, aplicando una convolución con un kernel de realce personalizado y luego restaurando la luminancia original. Esto mejora los detalles y los bordes en la representación del espacio latente.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `radio_afilado` | INT | No | 1-31 | El radio del kernel de realce (por defecto: 9) |
| `sigma` | FLOAT | No | 0.1-10.0 | La desviación estándar para el kernel gaussiano (por defecto: 1.0) |
| `alfa` | FLOAT | No | 0.0-5.0 | El factor de intensidad del realce (por defecto: 0.1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | Devuelve una operación de realce que puede aplicarse a datos latentes |
