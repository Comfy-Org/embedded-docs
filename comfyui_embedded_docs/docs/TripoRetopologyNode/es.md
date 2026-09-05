# TripoRetopologyNode

Tripo: Retopology toma un modelo 3D high-poly generado por un nodo Tripo anterior y lo reconstruye como una versión low-poly con topología limpia. Envía el modelo al servicio de retopología de Tripo, espera a que la tarea finalice y, a continuación, descarga el modelo finalizado y expone su ID de tarea para que lo utilicen otros nodos Tripo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID de tarea del modelo high-poly de origen. Acepta un ID de tarea de modelo de un nodo de generación de Tripo o un ID de tarea de segmento de Tripo: Segment Model. | STRING | Sí | ID de tarea de Tripo |
| `face_limit` | Número objetivo de caras: 500-20,000 triángulos o 500-10,000 quads. -1 permite que Tripo elija. (por defecto: -1) | INT | Sí | -1 (automático)<br>500 a 20,000 (triángulos)<br>500 a 10,000 (quads) |
| `quad` | Salida de malla quad. Tripo entrega las mallas quad como FBX, por lo que el resultado llega por la salida FBX y la salida GLB permanece vacía. (por defecto: False) | BOOLEAN | Sí | True<br>False (por defecto) |
| `bake` | Hornea las texturas de origen sobre la malla low-poly. (por defecto: True) | BOOLEAN | No | True (por defecto)<br>False |
| `part_names` | Nombres de partes separados por comas procedentes de Tripo: Segment Model. Vacío procesa el modelo completo. (por defecto: "") | STRING | No | Nombres de partes del modelo o vacío |

Nota: cuando `face_limit` se establece en -1, Tripo decide automáticamente el número de caras. Cuando `quad` está habilitado, el límite máximo de caras es de 10,000 quads en lugar de 20,000 triángulos, y el resultado se proporciona como FBX (la salida GLB permanece vacía). Cuando `part_names` está vacío, se procesa el modelo completo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `model_file` | Salida retrocompatible que identifica el archivo del modelo finalizado. Los flujos de trabajo más recientes deberían usar las salidas GLB o FBX en su lugar. | STRING |
| `model task_id` | ID de tarea del resultado de retopología finalizado. Se puede pasar a otros nodos Tripo para hacer referencia a este modelo. | STRING |
| `GLB` | El modelo low-poly retopologizado en formato GLB. Vacío cuando `quad` está habilitado. | GLB FILE |
| `FBX` | El modelo low-poly retopologizado en formato FBX. Solo se completa cuando `quad` está habilitado. | FBX FILE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/es.md)

---
**Source fingerprint (SHA-256):** `dc15f469b160a1d738e8089cf18de4a8262721bc77ebafa45bf194f04c7726b6`
