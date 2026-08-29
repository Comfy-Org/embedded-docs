# Renderizar pose corporal 3D

Renderiza datos de pose corporal 3D en una imagen utilizando un estilo seleccionable. El nodo acepta datos de pose del rastreador corporal SAM3D (MHR) o de un rig externo con eje Y vertical (Y-up) como Kimodo, y puede componer el resultado sobre una imagen de fondo opcional (o un lienzo negro cuando no se proporciona ninguno). Los estilos de renderizado disponibles incluyen una malla 3D sombreada, una silueta binaria, esqueletos estilo OpenPose en 2D y 3D, y cápsulas corporales estilo SCAIL.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `render_style` | Modo de renderizado. 'mesh' = malla MHR 3D rasterizada a través de la cámara. 'silhouette' = máscara binaria de la malla. 'openpose_2d' = esqueleto 2D plano. 'openpose_3d' = esqueleto OpenPose como modelo 3D con sombreado plano. 'scail' = cápsulas SCAIL 3D. (predeterminado: "mesh") | DYNAMIC_COMBO | Sí | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | Datos de pose MHR o datos de pose de un rig externo con eje Y vertical (Y-up) (KimodoSample). Todos los estilos de renderizado funcionan con rigs externos que contengan mapas de articulaciones OpenPose en su `_skeleton_override` (KimodoSample lo tiene). | MHR_POSE_DATA or KIMODO_POSE_DATA | Sí | — |
| `fondo` | Fondo por fotograma. Si se omite, se usa un lienzo negro. | IMAGE | No | — |
| `anchura` | Ancho de salida en píxeles. 0 = usar el image_size nativo de los datos de pose. Si solo se establece uno de width/height, el otro se deriva conservando la proporción original. (predeterminado: 0) | INT | No | 0 a 16384, step 8 |
| `altura` | Altura de salida en píxeles. 0 = usar el image_size nativo de los datos de pose. Si solo se establece uno de width/height, el otro se deriva conservando la proporción original. (predeterminado: 0) | INT | No | 0 a 16384, step 8 |
| `camera_info` | Anulación libre de cámara con 6 grados de libertad (6DOF). Cuando está conectada, la pose se reproyecta a través de esta cámara (posición/objetivo/zoom/rotación/FoV) en lugar de la cámara predicha. | LOAD_3D_CAMERA | No | — |

### Entradas de malla

Estos parámetros aparecen cuando `render_style` es "mesh".

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `shader` | Sombreado preestablecido. 'normals' = normal superficial actual en el espacio de cámara (convención de mapa de normales OpenGL Y+: +X→R, +Y→G, +Z→B). 'rainbow' = jet de Y corporal estilo RealisDance; las variantes 'rainbow_face_*' sobrescriben los vértices de la cara con colores por normal/región; 'depth' = gris lineal. (predeterminado: "default") | DYNAMIC_COMBO | No | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Rota el eje del jet de arcoíris alrededor de Z (hacia adelante). Diferencia izquierda/derecha. Solo disponible cuando `shader` es "rainbow", "rainbow_face_normal" o "rainbow_face_semantic". (predeterminado: -35.0) | FLOAT | No | -90.0 a 90.0, step 0.5 |
| `rainbow_tilt_x` | Rota el eje del jet de arcoíris alrededor de X (derecha). Diferencia frente/espalda. Solo disponible cuando `shader` es "rainbow", "rainbow_face_normal" o "rainbow_face_semantic". (predeterminado: 0.0) | FLOAT | No | -90.0 a 90.0, step 0.5 |
| `opacity` | Alfa de la malla sobre la imagen de fondo, o sobre negro cuando no hay ninguna conectada. (predeterminado: 1.0) | FLOAT | No | 0.0 a 1.0, step 0.01 |
| `person_palette_falloff` | Desaturación por persona hacia el blanco: la pista k recibe una mezcla pastel de (1 - falloff^k) (SCAIL 'segunda persona más suave'). 1.0 = desactivado. (predeterminado: 0.6) | FLOAT | No | 0.1 a 1.0, step 0.05 |
| `region` | 'hands_only' filtra las caras mediante el `hand_vert_mask` precalculado (pesos LBS contra los keypoints canónicos de la mano): aísla la malla de la mano para depuración. Si la máscara no está presente, se recurre a la malla completa. (predeterminado: "full_body") | COMBO | No | "full_body"<br>"hands_only" |

### Entradas de silueta

Cuando `render_style` es "silhouette", el nodo renderiza una máscara binaria de la malla 3D. Este modo no tiene parámetros adicionales.

### Entradas de OpenPose 2D

Estos parámetros aparecen cuando `render_style` es "openpose_2d".

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `marker_radius_px` | Radio del punto de los keypoints del cuerpo (px). (predeterminado: 4) | INT | No | 1 a 32, step 1 |
| `stick_width_px` | Semi-ancho de la elipse de la extremidad del cuerpo (px). El valor predeterminado de DWPose es 4. (predeterminado: 4) | INT | No | 1 a 32, step 1 |
| `limb_alpha` | Alfa por extremidad. El valor predeterminado de DWPose es 0.6. (predeterminado: 0.6) | FLOAT | No | 0.0 a 1.0, step 0.05 |
| `face_style` | 'full' = todos los landmarks faciales (sapiens-238 si está presente, o ~30 del fallback del rig). 'eyes_mouth' = subconjunto del fallback del rig (~12 puntos: solo ojos y labios exteriores). 'disabled' = sin puntos faciales. (predeterminado: "disabled") | COMBO | No | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | Dibuja 21+21 keypoints de manos y palos. 'disabled' = sin manos. 'dwpose' = puntos de azul sólido; 'openpose' = puntos de arcoíris. (predeterminado: "disabled") | COMBO | No | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Desaturación por persona: la pista k se mezcla hacia el blanco en 1 - falloff^k. La pista 0 permanece vívida; 1.0 desactiva la desaturación. (predeterminado: 0.6) | FLOAT | No | 0.1 a 1.0, step 0.05 |

### Entradas de OpenPose 3D

Estos parámetros aparecen cuando `render_style` es "openpose_3d".

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `radius_m` | Radio de la cápsula de la extremidad en metros (fino = similar a un palo). (predeterminado: 0.015) | FLOAT | No | 0.004 a 0.1, step 0.001 |
| `include_hands` | Dibuja los 21+21 keypoints de las manos como cápsulas 3D. (predeterminado: True) | BOOLEAN | No | True or False |
| `person_palette_falloff` | Desaturación por persona: la pista k se mezcla hacia el blanco en 1 - falloff^k. La pista 0 permanece vívida; 1.0 desactiva la desaturación. (predeterminado: 0.6) | FLOAT | No | 0.1 a 1.0, step 0.05 |

### Entradas de SCAIL

Estos parámetros aparecen cuando `render_style` es "scail".

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `radius_m` | Radio de la cápsula en metros (referencia SCAIL: ~0.022 m). (predeterminado: 0.022) | FLOAT | No | 0.005 a 0.2, step 0.001 |
| `hand_style` | Compone manos OpenPose 2D sobre el cuerpo de cápsulas 3D (coincide con SCAIL: no hay cápsulas de manos 3D). 'disabled' = sin manos. 'dwpose' = puntos de mano de azul sólido; 'openpose' = puntos de arcoíris. Los palos permanecen de arcoíris por dedo en cualquier caso. (predeterminado: "dwpose") | COMBO | No | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = todos los landmarks faciales (sapiens-238 si está presente, o ~30 del fallback del rig). 'eyes_mouth' = subconjunto del fallback del rig (~12 puntos: solo ojos y labios exteriores). 'disabled' = sin puntos faciales. (predeterminado: "disabled") | COMBO | No | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Desaturación por persona: la pista k se mezcla hacia el blanco en 1 - falloff^k. La pista 0 permanece vívida; 1.0 desactiva la desaturación. (predeterminado: 0.6) | FLOAT | No | 0.1 a 1.0, step 0.05 |

### Notas

- Si tanto `width` como `height` son 0, la salida usa el image_size nativo de los datos de pose. Si solo se establece uno de ellos, el otro se deriva conservando la proporción original. Un `background` conectado se redimensiona para ajustarse a la resolución de renderizado.
- Cuando `camera_info` está conectada, la pose se reproyecta a través de esa cámara en lugar de la predicha.
- En modo malla, `rainbow_tilt_z` y `rainbow_tilt_x` solo están disponibles cuando `shader` está configurado como "rainbow", "rainbow_face_normal" o "rainbow_face_semantic".
- En modo malla, cuando `region` es "hands_only", el filtro de la región de la mano requiere que los datos de pose contengan una máscara de vértices de la mano; si la máscara falta, se renderiza la malla completa en su lugar.
- En modo scail, las manos siempre se dibujan como superposiciones 2D; no hay cápsulas de manos 3D.
- Cuando la resolución de salida difiere de la resolución nativa de los datos de pose, los tamaños de los marcadores y palos de openpose_2d se escalan proporcionalmente.
- Si el fondo tiene menos fotogramas que los datos de pose, el último fotograma de fondo se reutiliza para los fotogramas restantes.
- La salida contiene un fotograma por cada fotograma de pose de entrada. Si los datos de pose no contienen fotogramas, se devuelve una única imagen negra.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `imagen` | Los fotogramas renderizados: los datos de pose dibujados en el estilo de renderizado seleccionado, compuestos sobre el fondo cuando hay uno conectado, o sobre negro en caso contrario. Un fotograma por cada fotograma de pose de entrada, devuelto como una única imagen por lotes (batch). | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/es.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`
