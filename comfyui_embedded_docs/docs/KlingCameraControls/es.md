> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/es.md)

El nodo Kling Camera Controls permite configurar varios parámetros de movimiento y rotación de cámara para crear efectos de control de movimiento en la generación de video. Proporciona controles para el posicionamiento, rotación y zoom de la cámara para simular diferentes movimientos de cámara.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `camera_control_type` | COMBO | Sí | Múltiples opciones disponibles | Especifica el tipo de configuración de control de cámara a utilizar |
| `horizontal_movement` | FLOAT | No | -10.0 a 10.0 | Controla el movimiento de la cámara a lo largo del eje horizontal (eje x). Negativo indica izquierda, positivo indica derecha (valor por defecto: 0.0) |
| `vertical_movement` | FLOAT | No | -10.0 a 10.0 | Controla el movimiento de la cámara a lo largo del eje vertical (eje y). Negativo indica hacia abajo, positivo indica hacia arriba (valor por defecto: 0.0) |
| `pan` | FLOAT | No | -10.0 a 10.0 | Controla la rotación de la cámara en el plano vertical (eje x). Negativo indica rotación hacia abajo, positivo indica rotación hacia arriba (valor por defecto: 0.5) |
| `tilt` | FLOAT | No | -10.0 a 10.0 | Controla la rotación de la cámara en el plano horizontal (eje y). Negativo indica rotación hacia la izquierda, positivo indica rotación hacia la derecha (valor por defecto: 0.0) |
| `roll` | FLOAT | No | -10.0 a 10.0 | Controla la cantidad de balanceo de la cámara (eje z). Negativo indica en sentido antihorario, positivo indica en sentido horario (valor por defecto: 0.0) |
| `zoom` | FLOAT | No | -10.0 a 10.0 | Controla el cambio en la distancia focal de la cámara. Negativo indica un campo de visión más estrecho, positivo indica un campo de visión más amplio (valor por defecto: 0.0) |

**Nota:** Al menos uno de los parámetros de control de cámara (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll`, o `zoom`) debe tener un valor distinto de cero para que la configuración sea válida.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `camera_control` | CAMERA_CONTROL | Devuelve la configuración de control de cámara configurada para su uso en la generación de video |