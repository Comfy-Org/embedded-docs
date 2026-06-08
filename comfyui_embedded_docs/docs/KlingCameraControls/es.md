El nodo Controles de Cámara Kling permite configurar varios parámetros de movimiento y rotación de cámara para crear efectos de control de movimiento en la generación de videos. Proporciona controles para posicionamiento, rotación y zoom de la cámara, simulando diferentes movimientos cinematográficos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `camera_control_type` | Especifica el tipo de configuración de control de cámara a utilizar | COMBO | Sí | `"simple"`<br>`"advanced"` |
| `horizontal_movement` | Controla el movimiento de la cámara a lo largo del eje horizontal (eje x). Los valores negativos indican izquierda, los positivos indican derecha (valor predeterminado: 0.0) | FLOAT | No | -10.0 a 10.0 |
| `vertical_movement` | Controla el movimiento de la cámara a lo largo del eje vertical (eje y). Los valores negativos indican hacia abajo, los positivos indican hacia arriba (valor predeterminado: 0.0) | FLOAT | No | -10.0 a 10.0 |
| `pan` | Controla la rotación de la cámara en el plano vertical (eje x). Los valores negativos indican rotación hacia abajo, los positivos indican rotación hacia arriba (valor predeterminado: 0.5) | FLOAT | No | -10.0 a 10.0 |
| `tilt` | Controla la rotación de la cámara en el plano horizontal (eje y). Los valores negativos indican rotación hacia la izquierda, los positivos indican rotación hacia la derecha (valor predeterminado: 0.0) | FLOAT | No | -10.0 a 10.0 |
| `roll` | Controla el grado de inclinación lateral de la cámara (eje z). Los valores negativos indican giro antihorario, los positivos indican giro horario (valor predeterminado: 0.0) | FLOAT | No | -10.0 a 10.0 |
| `zoom` | Controla el cambio en la distancia focal de la cámara. Los valores negativos indican un campo de visión más estrecho, los positivos indican un campo de visión más amplio (valor predeterminado: 0.0) | FLOAT | No | -10.0 a 10.0 |

**Nota:** Al menos uno de los parámetros de control de cámara (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` o `zoom`) debe tener un valor distinto de cero para que la configuración sea válida.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `camera_control` | Devuelve la configuración de control de cámara establecida para su uso en la generación de video | CAMERA_CONTROL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/es.md)

---
**Source fingerprint (SHA-256):** `4e1d826518ae17afd2c0aa22ebf6cce67b3ef33bb1730f0ce5ead5b9431cd548`
