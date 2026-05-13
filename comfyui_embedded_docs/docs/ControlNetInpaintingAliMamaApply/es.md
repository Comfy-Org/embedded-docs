> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/es.md)

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

El nodo ControlNetInpaintingAliMamaApply aplica el condicionamiento de ControlNet para tareas de inpainting combinando el condicionamiento positivo y negativo con una imagen de control y una máscara. Procesa la imagen de entrada y la máscara para crear un condicionamiento modificado que guía el proceso de generación, permitiendo un control preciso sobre qué áreas de la imagen serán inpintadas. El nodo admite ajuste de intensidad y controles de temporización para afinar la influencia de ControlNet durante diferentes etapas del proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | El condicionamiento positivo que guía la generación hacia el contenido deseado |
| `negative` | CONDITIONING | Sí | - | El condicionamiento negativo que aleja la generación del contenido no deseado |
| `control_net` | CONTROL_NET | Sí | - | El modelo ControlNet que proporciona control adicional sobre la generación |
| `vae` | VAE | Sí | - | El VAE (Autoencoder Variacional) utilizado para codificar y decodificar imágenes |
| `image` | IMAGE | Sí | - | La imagen de entrada que sirve como guía de control para el ControlNet |
| `mask` | MASK | Sí | - | La máscara que define qué áreas de la imagen deben ser inpintadas |
| `strength` | FLOAT | Sí | 0.0 a 10.0 | La intensidad del efecto de ControlNet (predeterminado: 1.0) |
| `start_percent` | FLOAT | Sí | 0.0 a 1.0 | El punto de inicio (como porcentaje) de cuándo comienza la influencia de ControlNet durante la generación (predeterminado: 0.0) |
| `end_percent` | FLOAT | Sí | 0.0 a 1.0 | El punto final (como porcentaje) de cuándo se detiene la influencia de ControlNet durante la generación (predeterminado: 1.0) |

**Nota:** Cuando el ControlNet tiene `concat_mask` habilitado, la máscara se invierte y se aplica a la imagen antes del procesamiento, y la máscara se incluye en los datos de concatenación adicional enviados al ControlNet.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado con ControlNet aplicado para inpainting |
| `negative` | CONDITIONING | El condicionamiento negativo modificado con ControlNet aplicado para inpainting |

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
