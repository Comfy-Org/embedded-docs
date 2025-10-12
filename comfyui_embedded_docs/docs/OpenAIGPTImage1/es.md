> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/es.md)

Genera imágenes de forma síncrona mediante el endpoint GPT Image 1 de OpenAI. Este nodo puede crear nuevas imágenes a partir de prompts de texto o editar imágenes existentes cuando se proporciona una imagen de entrada y una máscara opcional.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt de texto para GPT Image 1 (valor por defecto: "") |
| `seed` | INT | No | 0 a 2147483647 | Semilla aleatoria para la generación (valor por defecto: 0) - aún no implementado en el backend |
| `quality` | COMBO | No | "low"<br>"medium"<br>"high" | Calidad de imagen, afecta el costo y tiempo de generación (valor por defecto: "low") |
| `background` | COMBO | No | "opaque"<br>"transparent" | Retorna la imagen con o sin fondo (valor por defecto: "opaque") |
| `size` | COMBO | No | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024" | Tamaño de imagen (valor por defecto: "auto") |
| `n` | INT | No | 1 a 8 | Cuántas imágenes generar (valor por defecto: 1) |
| `image` | IMAGE | No | - | Imagen de referencia opcional para edición de imagen (valor por defecto: None) |
| `mask` | MASK | No | - | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) (valor por defecto: None) |

**Restricciones de Parámetros:**

- Cuando se proporciona `image`, el nodo cambia al modo de edición de imagen
- `mask` solo puede usarse cuando se proporciona `image`
- Al usar `mask`, solo se admiten imágenes individuales (el tamaño del lote debe ser 1)
- `mask` e `image` deben tener el mismo tamaño

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Imagen(es) generada(s) o editada(s) |
