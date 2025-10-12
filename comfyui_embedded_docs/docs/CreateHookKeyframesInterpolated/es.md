> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/es.md)

Crea una secuencia de fotogramas clave de enlace con valores de fuerza interpolados entre un punto de inicio y fin. Este nodo genera múltiples fotogramas clave que transicionan suavemente el parámetro de fuerza a través de un rango porcentual específico del proceso de generación, utilizando varios métodos de interpolación para controlar la curva de transición.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `strength_start` | FLOAT | Sí | 0.0 - 10.0 | El valor de fuerza inicial para la secuencia de interpolación (valor por defecto: 1.0) |
| `strength_end` | FLOAT | Sí | 0.0 - 10.0 | El valor de fuerza final para la secuencia de interpolación (valor por defecto: 1.0) |
| `interpolación` | COMBO | Sí | Múltiples opciones disponibles | El método de interpolación utilizado para transicionar entre los valores de fuerza |
| `start_percent` | FLOAT | Sí | 0.0 - 1.0 | La posición porcentual inicial en el proceso de generación (valor por defecto: 0.0) |
| `end_percent` | FLOAT | Sí | 0.0 - 1.0 | La posición porcentual final en el proceso de generación (valor por defecto: 1.0) |
| `keyframes_count` | INT | Sí | 2 - 100 | El número de fotogramas clave a generar en la secuencia de interpolación (valor por defecto: 5) |
| `print_keyframes` | BOOLEAN | Sí | Verdadero/Falso | Si se debe imprimir la información de los fotogramas clave generados en el registro (valor por defecto: Falso) |
| `prev_hook_kf` | HOOK_KEYFRAMES | No | - | Grupo opcional de fotogramas clave de enlace anteriores al que se puede anexar |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | El grupo de fotogramas clave de enlace generado que contiene la secuencia interpolada |
