> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/es.md)

El nodo ExtendIntermediateSigmas toma una secuencia existente de valores sigma e inserta valores sigma intermedios adicionales entre ellos. Permite especificar cuántos pasos extra agregar, el método de espaciado para la interpolación, y límites opcionales de sigma inicial y final para controlar dónde ocurre la extensión dentro de la secuencia sigma.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Sí | - | La secuencia sigma de entrada a extender con valores intermedios |
| `pasos` | INT | Sí | 1-100 | Número de pasos intermedios a insertar entre los sigmas existentes (valor por defecto: 2) |
| `comenzar_en_sigma` | FLOAT | Sí | -1.0 a 20000.0 | Límite superior de sigma para la extensión - solo extiende sigmas por debajo de este valor (valor por defecto: -1.0, que significa infinito) |
| `terminar_en_sigma` | FLOAT | Sí | 0.0 a 20000.0 | Límite inferior de sigma para la extensión - solo extiende sigmas por encima de este valor (valor por defecto: 12.0) |
| `espaciado` | COMBO | Sí | "linear"<br>"cosine"<br>"sine" | El método de interpolación para espaciar los valores sigma intermedios |

**Nota:** El nodo solo inserta sigmas intermedios entre pares sigma existentes donde tanto el sigma actual es menor o igual a `start_at_sigma` como mayor o igual a `end_at_sigma`. Cuando `start_at_sigma` se establece en -1.0, se trata como infinito, lo que significa que solo aplica el límite inferior `end_at_sigma`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | La secuencia sigma extendida con valores intermedios adicionales insertados |
