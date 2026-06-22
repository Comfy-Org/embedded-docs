# Sincronización Labial Kling Video con Texto

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

Nodo Kling de Sincronización Labial de Texto a Video sincroniza los movimientos de la boca en un archivo de video para que coincidan con un texto indicado. Toma un video de entrada y genera un nuevo video donde los movimientos labiales del personaje están alineados con el texto proporcionado. El nodo utiliza síntesis de voz para crear una sincronización del habla de aspecto natural.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | Archivo de video de entrada para la sincronización labial | VIDEO | Sí | - |
| `texto` | Contenido de texto para la generación de video con sincronización labial. Obligatorio cuando el modo es text2video. Longitud máxima de 120 caracteres. | STRING | Sí | - |
| `voz` | Selección de voz para el audio de sincronización labial (por defecto: "Melody") | COMBO | No | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" |
| `velocidad_de_voz` | Velocidad del habla. Rango válido: 0.8~2.0, preciso hasta un decimal. (por defecto: 1) | FLOAT | No | 0.8-2.0 |

**Requisitos del Video:**

- El archivo de video no debe superar los 100MB
- La altura/ancho debe estar entre 720px y 1920px
- La duración debe estar entre 2s y 10s

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `id_video` | Video generado con audio sincronizado con los labios | VIDEO |
| `duración` | Identificador único para el video generado | STRING |
| `duration` | Información de duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `f16200d52ba05acfedebc027dde91e2c91bdbb80086888d947c9f56a4e92856d`
