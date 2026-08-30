# Suavizar datos de pose corporal SAM3D

Smooth SAM3D Body Pose Data reduce el desplazamiento fotograma a fotograma en secuencias de pose corporal 3D al promediar el movimiento a lo largo del tiempo. Aplica un suavizado completo a los datos de cámara y apariencia, mientras reduce el suavizado en la geometría de la malla cuando el sujeto rota rápidamente, para que los giros rápidos no se aplasten.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mhr_pose_data` | La secuencia de datos de pose MHR que se va a suavizar, que contiene parámetros de modelo, parámetros de forma, parámetros de expresión, disposición de puntos clave MHR70 y datos de malla relacionados. | MHR_POSE_DATA | Sí | — |
| `intensidad` | Fuerza del suavizado. 0 = sin suavizar, 1 = suavizado. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (paso 0.05) |
| `método` | gaussian: media ponderada simétrica, el mejor suavizador de uso general.<br>savgol: ajuste polinomial deslizante, conserva los picos pronunciados. (por defecto: "savgol") | COMBO | Sí | "gaussian"<br>"savgol" |
| `ventana` | Ventana temporal en fotogramas (valores impares). (por defecto: 7) | INT | Sí | 1 a 51 (valores impares, paso 2) |
| `rotation_threshold_degrees` | Desactiva el suavizado para esta tasa de rotación de la raíz (grados/fotograma) con el fin de conservar los giros rápidos. 30° es adecuado para la mayoría de los contenidos; los valores bajos podrían desactivar el suavizado en el desplazamiento común y afectar silenciosamente a la calidad. 0 = desactivar. (por defecto: 30.0) | FLOAT | Sí | 0.0 a 90.0 (paso 1.0) |

Nota: Cuando `strength` es 0.0 o menor, o `window` es 1 o menor, el nodo devuelve los datos de entrada sin cambios. La entrada debe contener al menos 2 fotogramas y datos de puntos clave; de lo contrario, el nodo devuelve los datos de entrada sin cambios. Cuando `rotation_threshold_degrees` es 0.0, la reducción del suavizado basada en la rotación está desactivada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mhr_pose_data` | La secuencia de datos de pose MHR suavizada con un desplazamiento reducido entre fotogramas. | MHR_POSE_DATA |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/es.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`
