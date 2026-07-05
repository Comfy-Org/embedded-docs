# Escalado Épsilon

Eres un experto en traducción técnica especializado en documentación de nodos ComfyUI del inglés al español.

## Reglas de Traducción

1. **Contenido que NO debe traducirse:**
   - Nombres de parámetros entre comillas invertidas: `image`, `seed`, `model`
   - Tipos de datos en MAYÚSCULAS: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, etc.
   - Valores en columna Range: números, "auto", nombres de opciones
   - Código, rutas de archivos

2. **Contenido que SÍ debe traducirse:**
   - Títulos de secciones: ## Descripción general, ## Entradas, ## Salidas
   - Todo el texto descriptivo y explicativo
   - Descripciones de parámetros

3. **Calidad de traducción:**
   - Usar español estándar y neutral
   - Mantener tono profesional pero accesible
   - Asegurar precisión técnica
   - Usar terminología técnica estándar en español

4. **Formato:**
   - Mantener todo el formato Markdown
   - Preservar estructura de tablas
   - No agregar ninguna nota o enlace al inicio del documento (será agregado automáticamente)

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Este nodo implementa el método de Escalado Épsilon del artículo de investigación "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6). Funciona escalando el ruido predicho durante el proceso de muestreo para ayudar a reducir el sesgo de exposición, lo que puede conducir a una mejora en la calidad de las imágenes generadas. Esta implementación utiliza el "programa uniforme" recomendado por el artículo por su practicidad y efectividad.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al cual se le aplicará el parche de escalado épsilon. | MODEL | Sí | - |
| `factor_escala` | El factor por el cual se escala el ruido predicho. Un valor mayor que 1.0 reduce el ruido, mientras que un valor menor que 1.0 lo aumenta (valor predeterminado: 1.005). | FLOAT | No | 0.5 - 1.5 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | Una versión parcheada del modelo de entrada con la función de escalado épsilon aplicada a su proceso de muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/es.md)

---
**Source fingerprint (SHA-256):** `85c464ce0b2ec2a031a01d9eef5d50fd300be3012499cc061705fb7964110882`
