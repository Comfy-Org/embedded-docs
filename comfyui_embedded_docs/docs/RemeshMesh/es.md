# RemeshMesh

Remesh Mesh reconstruye una malla con una teselación limpia y uniforme muestreando un campo de distancia de banda estrecha alrededor de la superficie original y extrayéndolo mediante Dual Contouring. Esto normaliza topologías desordenadas, no múltiples o auto-intersecantes, y está pensado para ejecutarse antes de Decimate Mesh para alcanzar un recuento exacto de caras. El procesamiento se ejecuta en el dispositivo de cómputo activo y la malla de salida permanece soldada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `malla` | La malla de entrada para remallar. | MESH | Sí | — |
| `resolución` | Resolución de la rejilla de vóxeles (densidad de salida). 256 ~ 100 000 caras, 512 ~ 1M. Para un recuento exacto de caras, continúe con Decimate Mesh. (predeterminado: 512) | INT | Sí | 32 - 2048 |
| `sign_mode` | Modo de distancia con signo utilizado para la extracción de superficie. "udf" es robusto frente a entradas desordenadas o no múltiples; "sdf" produce una superficie única y limpia con recuperación de características nítidas mediante QEF (Función de Error Cuadrático), pero necesita un enrollado (winding) consistente. Seleccionar un modo revela sus subopciones específicas. (predeterminado: "udf") | DYNAMIC_COMBO | Sí | "udf"<br>"sdf" |
| `band` | Ancho de banda estrecha en unidades de vóxel. En modo UDF también desplaza la superficie. (avanzado, predeterminado: 1.0) | FLOAT | Sí | 0.5 - 4.0 |
| `project_back` | Interpolar linealmente los vértices hacia la superficie original (0 = DC puro, 1 = ajustado a la superficie). (avanzado, predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `fix_poles` | Colapsar pares de vértices de valencia 3 (artefacto de unión en T del DC). (avanzado, predeterminado: false) | BOOLEAN | Sí | true / false |
| `smooth_iters` | Iteraciones de suavizado de Taubin (0 = desactivado). 2-3 limpia los artefactos de escalera del DC; valores más altos suavizan en exceso los bordes QEF. (predeterminado: 0) | INT | Sí | 0 - 20 |
| `drop_small_components` | Eliminar componentes por debajo de esta fracción del número de caras del componente más grande. 0 desactiva. (avanzado, predeterminado: 0.01) | FLOAT | Sí | 0.0 - 0.5 |
| `precluster_max_verts` | Limitar el número de vértices de entrada antes de las consultas de campo; las entradas que superen este valor se deciman por agrupamiento (cluster-decimated) primero. Evita OOM (falta de memoria) en mallas enormes. (avanzado, predeterminado: 20 000 000) | INT | Sí | 0 - 100 000 000 |

### Entradas del modo "udf"

Estos parámetros aparecen cuando `sign_mode` está configurado en `"udf"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `qef` | Ubicación de vértices duales mediante QEF (Función de Error Cuadrático) para bordes más nítidos. (predeterminado: false) | BOOLEAN | No | true / false |
| `drop_inverted_components` | Eliminar componentes cerrados con normales hacia adentro (volumen negativo) — la capa interna de la UDF. (predeterminado: false) | BOOLEAN | No | true / false |
| `drop_enclosed_components` | Eliminar componentes dentro del bbox (caja delimitadora) del más grande que no superen un raycast de punto en la malla. Desactivar para piezas anidadas legítimas. (predeterminado: false) | BOOLEAN | No | true / false |

### Entradas del modo "sdf"

Estos parámetros aparecen cuando `sign_mode` está configurado en `"sdf"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `qef` | Ubicación de vértices duales mediante QEF (Función de Error Cuadrático) (recupera características nítidas) frente al centroide de cruce de bordes. (predeterminado: true) | BOOLEAN | No | true / false |
| `manifold` | Contorneado dual múltiple (Manifold Dual Contouring): 1-4 vértices duales por vóxel para casos de múltiples láminas. Más lento. (predeterminado: false) | BOOLEAN | No | true / false |

Nota: La opción `qef` tiene un valor predeterminado diferente según el modo seleccionado: false en el modo "udf", true en el modo "sdf". Cuando `precluster_max_verts` es mayor que 0 y la malla de entrada tiene más vértices que este valor, la malla se decima por agrupamiento hasta ese objetivo antes de las consultas de campo. Después del procesamiento, el nodo muestra el cambio en el número de caras de entrada a salida en el nodo (por ejemplo, "caras: 1.23M → 200K (-84%)").

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `mesh` | La malla remallada con teselación uniforme y topología soldada. Los colores de vértice se conservan si están presentes en la entrada; los UV, normales y tangentes no se transfieren. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/es.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`
