> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/es.md)

El nodo TorchCompileModel aplica compilación de PyTorch a un modelo para optimizar su rendimiento. Crea una copia del modelo de entrada y la envuelve con la funcionalidad de compilación de PyTorch utilizando el backend especificado. Esto puede mejorar la velocidad de ejecución del modelo durante la inferencia.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo que se va a compilar y optimizar |
| `backend` | STRING | Sí | "inductor"<br>"cudagraphs" | El backend de compilación de PyTorch a utilizar para la optimización (predeterminado: "inductor") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `modelo` | MODEL | El modelo compilado con la compilación de PyTorch aplicada |

---
**Source fingerprint (SHA-256):** `923e71b528e6e53468916f74c2a02924bf51738f29e36638312c6da6357fcedb`
