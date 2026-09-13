# Remallar malla (DC de banda estrecha)

Remesh Mesh reconstruye una malla con un teselado limpio y uniforme muestreando un campo de distancia de banda estrecha alrededor de la superficie original y extrayéndolo con Dual Contouring. Esto normaliza topologías desordenadas, no manifold o auto-intersectantes, y está pensado para ejecutarse antes de Decimate Mesh para alcanzar un recuento exacto de caras. El procesamiento se ejecuta en el dispositivo de cómputo activo y la malla de salida permanece soldada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `malla` | La malla de entrada que se va a remallar. | MESH | Sí | — |
| `resolución` | Resolución de la cuadrícula de vóxeles (densidad de salida). 256 ~ 100k caras, 512 ~ 1M. Para un recuento exacto de caras, continúe con Decimate Mesh. (predeterminado: 512) | INT | Sí | 32 - 2048 |
| `sign_mode` | Modo de extracción de superficie. "udf" es robusto ante entradas desordenadas/no manifold; "sdf" produce una superficie única limpia con recuperación de características nítidas mediante QEF (función de error cuadrático), pero necesita un bobinado consistente. Al seleccionar un modo, se muestran sus subopciones específicas. (predeterminado: "udf") | DYNAMIC_COMBO | Sí | "udf"<br>"sdf" |
| `band` | Ancho de la banda estrecha en unidades de vóxel. En modo UDF, también desplaza la superficie. (avanzado, predeterminado: 1.0) | FLOAT | Sí | 0.5 - 4.0 |
| `project_back` | Interpola linealmente los vértices hacia la superficie original (0 = DC puro, 1 = ajustado). (avanzado, predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `fix_poles` | Colapsa pares de vértices de valencia 3 (artefacto de unión en T de DC). (avanzado, predeterminado: false) | BOOLEAN | Sí | true / false |
| `smooth_iters` | Iteraciones de suavizado de Taubin (0 = desactivado). 2-3 limpia artefactos escalonados de DC; valores más altos suavizan en exceso los bordes QEF. (predeterminado: 0) | INT | Sí | 0 - 20 |
| `drop_small_components` | Elimina componentes por debajo de esta fracción del recuento de caras del componente más grande. 0 lo desactiva. (avanzado, predeterminado: 0.01) | FLOAT | Sí | 0.0 - 0.5 |
| `precluster_max_verts` | Limita el recuento de vértices de entrada antes de las consultas del campo; las entradas que superen este valor se reducen primero mediante decimación por clústeres hasta ese valor. Evita OOM en mallas enormes. (avanzado, predeterminado: 20,000,000) | INT | Sí | 0 - 100,000,000 |

### Entradas del modo "udf"

Estos parámetros aparecen cuando `sign_mode` se establece en `"udf"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `qef` | Colocación de vértices duales mediante QEF (función de error cuadrático) para bordes más nítidos. (avanzado, predeterminado: false) | BOOLEAN | No | true / false |
| `drop_inverted_components` | Elimina componentes cerrados con normal hacia dentro (volumen negativo): la capa interna del UDF. (avanzado, predeterminado: false) | BOOLEAN | No | true / false |
| `drop_enclosed_components` | Elimina componentes dentro de la bbox del más grande que fallen un raycast de punto en malla. Desactívelo para partes anidadas legítimas. (avanzado, predeterminado: false) | BOOLEAN | No | true / false |

### Entradas del modo "sdf"

Estos parámetros aparecen cuando `sign_mode` se establece en `"sdf"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `qef` | Colocación de vértices duales mediante QEF (función de error cuadrático) (recupera características nítidas) frente al centroide de cruce de bordes. (predeterminado: true) | BOOLEAN | No | true / false |
| `manifold` | Dual Contouring manifold: 1-4 vértices duales por vóxel para casos de varias hojas. Más lento. (predeterminado: false) | BOOLEAN | No | true / false |

Nota: La opción `qef` tiene un valor predeterminado diferente según el modo seleccionado: false en el modo "udf", true en el modo "sdf". Cuando `precluster_max_verts` es mayor que 0 y la malla de entrada tiene más vértices que este valor, la malla se decima por clústeres hasta ese objetivo antes de las consultas del campo. Después del procesamiento, el nodo muestra el cambio en el recuento de caras de entrada a salida en el propio nodo (por ejemplo, "faces: 1.23M → 200K (-84%)").

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-----------|-----------|
| `mesh` | La malla remallada con teselado uniforme y topología soldada. Los colores de vértice se conservan cuando están presentes en la entrada; las UV, normales y tangentes no se transfieren. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/es.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
