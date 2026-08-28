# BakeTextureFromVoxel

Este nodo hornea texturas PBR sobre una malla 3D utilizando la disposición UV existente de la malla. Muestrea atributos de color y material de un volumen de vóxeles disperso en cada texel y genera una imagen de color base además de mapas de metalidad y rugosidad. No desenvuelve la malla; por lo tanto, se debe conectar aguas arriba un nodo de desenvolvimento UV.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `mesh` | La malla 3D sobre la que se hornean las texturas. Debe tener ya una disposición UV; debe conectarse aguas arriba un nodo de desenvolvimento UV. | MESH | Sí | |
| `voxel_colors` | Volumen de vóxeles disperso que contiene colores por vóxel y atributos PBR opcionales (canales de metalidad y rugosidad). | VOXEL | Sí | |
| `texture_size` | Resolución del atlas UV cuadrado (nombre visible: "resolution", por defecto: 2048). | INT | Sí | 64 a 8192 |
| `reference_mesh` | Malla densa opcional anterior a la decimación; reproyecta cada texel sobre su superficie real antes del muestreo, eliminando el horneado facetado en mallas gruesas. | MESH | No | |

Notas:

- La malla de entrada debe tener UVs. Si no hay UVs, el nodo genera un error. Los UVs deben ser 1:1 con los vértices (un UV por vértice).
- Cuando la malla y las coordenadas de vóxeles contienen una dimensión de lote, cada elemento del lote se hornea por separado. Si un elemento del lote no tiene vóxeles ni caras, se omite y se emite una textura negra para él.
- Cuando se proporciona `reference_mesh` para un lote, se empareja por índice de lote, a menos que contenga una sola malla, en cuyo caso esa malla se usa para todos los elementos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `base_color` | Mapa de textura de color base RGB. Los valores son flotantes en el rango de 0 a 1. | IMAGE |
| `metallic` | Mapa de metalidad en escala de grises (flotante, 0–1). Negro cuando los colores de vóxeles no contienen canal de metalidad. | IMAGE |
| `roughness` | Mapa de rugosidad en escala de grises (flotante, 0–1). Negro cuando los colores de vóxeles no contienen canal de rugosidad. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/es.md)

---
**Source fingerprint (SHA-256):** `419f9e064edaeb9db8d5e052cf57a3b8b77bf7e025e8a0fc9aa0e1919c06b51c`
