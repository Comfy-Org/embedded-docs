# MiniMax Hailuo Video

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

Genera videos a partir de indicaciones de texto utilizando el modelo MiniMax Hailuo-02. Opcionalmente, puedes proporcionar una imagen inicial como primer fotograma para crear un video que continúe a partir de esa imagen.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `texto_del_prompt` | Indicación de texto para guiar la generación del video. | STRING | Sí | - |
| `semilla` | Semilla aleatoria utilizada para crear el ruido (predeterminado: 0). | INT | No | 0 a 18446744073709551615 |
| `imagen_primer_fotograma` | Imagen opcional para usar como primer fotograma y generar un video. | IMAGE | No | - |
| `optimizador_de_prompt` | Optimizar la indicación para mejorar la calidad de generación cuando sea necesario (predeterminado: True). | BOOLEAN | No | - |
| `duración` | Duración del video de salida en segundos (predeterminado: 6). | COMBO | No | `6`<br>`10` |
| `resolución` | Dimensiones de la visualización del video. 1080p es 1920x1080, 768p es 1366x768 (predeterminado: "768P"). | COMBO | No | `"768P"`<br>`"1080P"` |

**Nota:** Al usar el modelo MiniMax-Hailuo-02 con resolución 1080P, la duración está limitada a 6 segundos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `5466b9cda979a30158b818743de0e0cf30eb3e27015d431eb04a370029250a4c`
