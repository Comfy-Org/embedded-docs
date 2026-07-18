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

El nodo WanMoveTracksFromCoords crea trayectorias de movimiento a partir de una cadena con formato JSON de coordenadas. Convierte los datos de coordenadas en un formato de tensor que puede ser utilizado por otros nodos de procesamiento de video y, opcionalmente, puede aplicar una máscara para controlar la visibilidad de las trayectorias a lo largo del tiempo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `coordenadas_de_pista` | Una cadena con formato JSON que contiene los datos de coordenadas para las trayectorias. El valor predeterminado es una lista vacía (`"[]"`). | STRING | No | N/A |
| `máscara_de_pista` | Una máscara opcional. Cuando se proporciona, el nodo la utiliza para determinar la visibilidad de cada trayectoria por fotograma. | MASK | No | N/A |

**Nota:** La entrada `track_coords` espera una estructura JSON específica. Debe ser una lista de trayectorias, donde cada trayectoria es una lista de fotogramas, y cada fotograma es un objeto con coordenadas `x` y `y`. El número de fotogramas debe ser consistente en todas las trayectorias.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `longitud_de_pista` | Los datos de trayectoria generados, que contienen las coordenadas de la ruta y la información de visibilidad para cada trayectoria. | TRACKS |
| `longitud_de_pista` | El número total de fotogramas en las trayectorias generadas. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/es.md)

---
**Source fingerprint (SHA-256):** `106b05b3bdb5ede6e31216b9f3c14160630df0eee1f4e8a645c2b6cf9fbecf8c`
