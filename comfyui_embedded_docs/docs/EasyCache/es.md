# EasyCache

El nodo EasyCache añade un sistema de caché nativo a un modelo de difusión que acelera el muestreo reutilizando los resultados de pasos previamente calculados en lugar de volver a calcular cada paso. Se activa solo entre un punto de inicio y un punto de fin configurables del proceso de muestreo, y omite pasos cuando el cambio estimado en la salida se mantiene por debajo de un umbral definido por el usuario. Es un nodo experimental destinado a usos avanzados de depuración.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le añade EasyCache. | MODEL | Sí | - |
| `umbral_de_reutilización` | El umbral para reutilizar pasos almacenados en caché (por defecto: 0.2). | FLOAT | Sí | 0.0 - 3.0 |
| `porcentaje_inicial` | El paso de muestreo relativo para comenzar a usar EasyCache (por defecto: 0.15). | FLOAT | Sí | 0.0 - 1.0 |
| `porcentaje_final` | El paso de muestreo relativo para finalizar el uso de EasyCache (por defecto: 0.95). | FLOAT | Sí | 0.0 - 1.0 |
| `detallado` | Si se debe registrar información detallada (por defecto: False). | BOOLEAN | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo con la funcionalidad EasyCache añadida. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/es.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
