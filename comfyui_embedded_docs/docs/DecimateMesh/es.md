# DecimateMesh

DecimateMesh simplifica una malla 3D a un número de caras objetivo mediante una simplificación por métrica de error cuadrático (QEM), ejecutando el cálculo en el dispositivo de cómputo activo. El modo de colocación `"midpoint"` es el preajuste fiel a cumesh que ofrece la mejor calidad y preserva características finas como el cabello, mientras que `"qem"` coloca los vértices en la posición óptima según QEM, con controles opcionales de línea y bordes característicos. La malla de salida permanece soldada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mesh` | La malla 3D a simplificar. | MESH | Sí | - |
| `target_face_count` | Número máximo de caras objetivo. 0 lo desactiva. (por defecto: 200000) | INT | Sí | 0 a 50000000 |
| `placement_mode` | midpoint: fiel a cumesh (recomendado). qem: colocación óptima según QEM. (por defecto: `"midpoint"`) | DYNAMIC_COMBO | Sí | `"midpoint"`<br>`"qem"` |

### Entradas de Midpoint

El modo de colocación `"midpoint"` no expone subparámetros adicionales; utiliza el preajuste de colocación midpoint predeterminado.

### Entradas de QEM

Los siguientes subparámetros aparecen en la interfaz solo cuando `placement_mode` está configurado en `"qem"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `line_quadric_weight` | Peso lineal-cuadrático por borde; conserva crestas/valles pronunciados. 0 = desactivado. (por defecto: 0.0) | FLOAT | No | 0.0 a 100.0 |
| `feature_edge_quadric_weight` | Peso cuadrático adicional en bordes característicos diedros (pliegues). 0 = desactivado. (por defecto: 0.0) | FLOAT | No | 0.0 a 1000.0 |
| `feature_edge_min_dihedral_deg` | Ángulo diedro mínimo (en grados) para considerar un borde como borde característico. (por defecto: 30.0) | FLOAT | No | 0.0 a 180.0 |
| `clamp_v_to_edge` | Proyecta la posición óptima según QEM sobre el segmento de borde colapsado. (por defecto: true) | BOOLEAN | No | `true`<br>`false` |

Nota: La decimación se omite cuando `target_face_count` es 0 o cuando la malla ya tiene menos caras que el objetivo. El nodo muestra un resumen de reducción de caras sobre sí mismo, por ejemplo `faces: 1.23M → 200K (-84%)`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mesh` | La malla simplificada con el número de caras reducido; la conectividad permanece soldada. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/es.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
