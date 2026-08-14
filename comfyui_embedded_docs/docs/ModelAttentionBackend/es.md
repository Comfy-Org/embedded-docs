# ModelAttentionBackend

Este nodo te permite elegir qué backend de atención utiliza un modelo para sus cálculos de atención. Crea una copia del modelo e intercambia la función de atención que selecciones, lo que puede afectar el rendimiento o el comportamiento. Si el backend elegido no está disponible, automáticamente vuelve a la atención de PyTorch y registra una advertencia.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model` | El modelo al que se le aplicará el backend de atención seleccionado. | MODEL | Sí |  |
| `attention` | El backend de atención a utilizar (predeterminado: "pytorch attention"). Si el backend seleccionado no está disponible, se usa PyTorch attention como respaldo. | STRING | Sí | "pytorch attention"<br>"comfy kitchen attention" |

Nota: La opción "comfy kitchen attention" solo se muestra cuando el módulo de atención int8 de comfy kitchen está disponible en el entorno actual.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `MODEL` | Un clon del modelo de entrada con el backend de atención seleccionado aplicado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/es.md)

---
**Source fingerprint (SHA-256):** `4ba613cc0bf5b3e7f9effa895b98b3a3bd302e5d20e9d7e18d1633906c783244`
