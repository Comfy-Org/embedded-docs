# Aplicar Anima LLLite

Este nodo aplica un parche de animación ligero a un modelo de difusión, permitiendo la generación controlada de imagen a imagen con intensidad y temporización ajustables. Integra un parche de modelo preconfigurado con una imagen de entrada y una máscara opcional, modificando las capas de atención y MLP del modelo para influir en el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `modelo` | El modelo de difusión base al que aplicar el parche | MODEL | Sí | |
| `parche de modelo` | El parche de animación preconfigurado a aplicar | MODEL_PATCH | Sí | |
| `imagen` | La imagen de referencia para guiar la generación. Solo se utilizan los primeros 3 canales de color (RGB) | IMAGE | Sí | |
| `intensidad` | La intensidad del efecto del parche (predeterminado: 1.0) | FLOAT | Sí | -10.0 a 10.0 |
| `porcentaje de inicio` | El porcentaje del proceso de eliminación de ruido en el que el parche comienza a hacer efecto (predeterminado: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `porcentaje final` | El porcentaje del proceso de eliminación de ruido en el que el parche deja de hacer efecto (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `máscara` | Una máscara opcional para limitar el efecto del parche a áreas específicas de la imagen | MASK | No | |

**Nota sobre restricciones de parámetros:** Si el `model_patch` tiene 4 canales de entrada y no se proporciona una `mask`, se crea automáticamente una máscara cero que coincide con las dimensiones de la imagen. Si el `model_patch` no tiene 4 canales de entrada, el parámetro `mask` se ignora y se establece en `None`. Este nodo está marcado como experimental en ComfyUI.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `MODEL` | El modelo de difusión parcheado con el parche de animación aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/es.md)

---
**Source fingerprint (SHA-256):** `291dc6a6619faab1c1100110c71c47381addcd80dbaf933dd8025a376bc2bee7`
