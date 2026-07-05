# Orientación de Auto-Atención

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

El nodo de Guía de Autoatención aplica guía a modelos de difusión modificando el mecanismo de atención durante el proceso de muestreo. Captura las puntuaciones de atención de los pasos de eliminación de ruido incondicionales y las utiliza para crear mapas de guía borrosos que influyen en la salida final. Esta técnica ayuda a guiar el proceso de generación aprovechando los propios patrones de atención del modelo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se aplicará la guía de autoatención | MODEL | Sí | - |
| `escala` | La intensidad del efecto de guía de autoatención (predeterminado: 0.5) | FLOAT | No | -2.0 a 5.0 |
| `blur_sigma` | La cantidad de desenfoque aplicada para crear el mapa de guía (predeterminado: 2.0) | FLOAT | No | 0.0 a 10.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo modificado con la guía de autoatención aplicada | MODEL |

**Nota:** Este nodo es actualmente experimental y tiene limitaciones con lotes fragmentados. Solo puede guardar puntuaciones de atención de una llamada UNet y puede no funcionar correctamente con tamaños de lote más grandes.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/es.md)

---
**Source fingerprint (SHA-256):** `5f16ecd8f74bfd71073c6e3a65be08e54e4f5b9c56fe08deb48f35df381e82fa`
