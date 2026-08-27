# RemeshMesh

Remesh Mesh reconstruye una malla con una teselación limpia y uniforme muestreando un campo de distancia de banda estrecha alrededor de la superficie original y extrayéndola con Dual Contouring. Esto normaliza topologías desordenadas, no múltiples o auto-intersecantes, y está diseñado para ejecutarse antes de Decimate Mesh para alcanzar un recuento exacto de caras. El procesamiento se ejecuta en el dispositivo de cómputo activo y la malla de salida permanece soldada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mesh` | La malla de entrada a remallar. | MESH | Sí | — |
| `resolution` | Resolución de la cuadrícula de vóxeles (densidad de salida). 256 ~ 100k caras, 512 ~ 1M. Para un recuento exacto de caras, continúe con Decimate Mesh. (por defecto: 512) | INT | Sí | 32 - 2048 |
| `sign_mode` | Modo de distancia con signo utilizado para la extracción de superficies. "udf" es robusto ante entradas desordenadas o no múltiples; "sdf" produce una única superficie limpia con recuperación de características nítidas mediante QEF (Función de Error Cuadrático), pero requiere una orientación consistente. Al seleccionar un modo se muestran sus subopciones específicas. (por defecto: "udf") | DYNAMIC_COMBO | Sí | "udf"<br>"sdf" |
| `band` | Ancho de banda estrecha en unidades de vóxel. En modo UDF también desplaza la superficie. (avanzado, por defecto: 1.0) | FLOAT | Sí | 0.5 - 4.0 |
| `project_back` | Interpola linealmente los vértices hacia la superficie original (0 = DC puro, 1 = ajustado). (avanzado, por defecto: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `fix_poles` | Colapsa pares de vértices de valencia 3 (artefacto de unión en T de DC). (avanzado, por defecto: false) | BOOLEAN | Sí | true / false |
| `smooth_iters` | Iteraciones de suavizado Taubin (0 = desactivado). 2-3 limpia los artefactos de escalera de DC; valores más altos sobresuavizan los bordes QEF. (por defecto: 0) | INT | Sí | 0 - 20 |
| `drop_small_components` | Elimina componentes por debajo de esta fracción del recuento de caras del más grande. 0 desactiva. (avanzado, por defecto: 0.01) | FLOAT | Sí | 0.0 - 0.5 |
| `precluster_max_verts` | Limita el recuento de vértices de entrada antes de las consultas de campo; las entradas por encima de este valor se deciman por clústeres hasta alcanzarlo. Evita OOM (falta de memoria) en mallas enormes. (avanzado, por defecto: 20 000 000) | INT | Sí | 0 - 100 000 000 |

### Entradas del modo "udf"

Estos parámetros aparecen cuando `sign_mode` está configurado en `"udf"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `qef` | Colocación de vértices duales mediante QEF (Función de Error Cuadrático) para bordes más nítidos. (por defecto: false) | BOOLEAN | No | true / false |
| `drop_inverted_components` | Elimina componentes cerrados con normales hacia adentro (volumen negativo) — la capa interna de UDF. (por defecto: false) | BOOLEAN | No | true / false |
| `drop_enclosed_components` | Elimina componentes dentro de la caja delimitadora (bbox) del más grande que fallan un raycast de punto en malla. Desactívelo para piezas anidadas legítimas. (por defecto: false) | BOOLEAN | No | true / false |

### Entradas del modo "sdf"

Estos parámetros aparecen cuando `sign_mode` está configurado en `"sdf"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `qef` | Colocación de vértices duales mediante QEF (Función de Error Cuadrático) (recupera características nítidas) frente al centroide de cruce de bordes. (por defecto: true) | BOOLEAN | No | true / false |
| `manifold` | Dual Contouring múltiple: 1-4 vértices duales por vóxel para casos de múltiples capas. Más lento. (por defecto: false) | BOOLEAN | No | true / false |

Nota: La opción `qef` tiene un valor por defecto diferente según el modo seleccionado: false en modo "udf", true en modo "sdf". Cuando `precluster_max_verts` es mayor que 0 y la malla de entrada tiene más vértices que este valor, la malla se decima por clústeres hasta ese objetivo antes de las consultas de campo. Después del procesamiento, el nodo muestra el cambio de recuento de caras de entrada a salida en el nodo (por ejemplo, "caras: 1.23M → 200K (-84%)").

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mesh` | La malla remallada con teselación uniforme y topología soldada. Los colores de vértice se conservan si están presentes en la entrada; los UV, normales y tangentes no se transfieren. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/es.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`
