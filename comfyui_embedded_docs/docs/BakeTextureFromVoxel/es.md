# BakeTextureFromVoxel

Este nodo hornea texturas PBR sobre una malla 3D utilizando la disposición UV existente de la malla. Muestrea el color y los atributos de material de un volumen de vóxeles disperso en cada texel y genera una imagen de color base además de mapas de metalicidad y rugosidad. No desarrolla la malla, por lo que debe conectarse un nodo de desenvolvimento UV aguas arriba.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `mesh` | La malla 3D sobre la que hornear texturas. Debe tener ya una disposición de UV; debe conectarse un nodo de desenvolvimento UV aguas arriba. | MESH | Sí | |
| `voxel_colors` | Volumen de vóxeles disperso que contiene colores por vóxel y atributos PBR opcionales (canales de metalicidad y rugosidad). | VOXEL | Sí | |
| `texture_size` | Resolución del atlas UV cuadrado (nombre mostrado: "resolution", predeterminado: 2048). | INT | Sí | 64 to 8192 |
| `reference_mesh` | Malla densa opcional anterior a la decimación; reproyecta cada texel sobre su superficie real antes de muestrear, eliminando el horneado facetado en mallas gruesas. | MESH | No | |

Notas:

- La malla de entrada debe tener UV. Si no hay UV, el nodo genera un error. Los UV deben ser 1:1 con los vértices (un UV por vértice).
- Cuando la malla y las coordenadas de vóxeles contienen una dimensión de lote, cada elemento del lote se hornea por separado. Si un elemento del lote no tiene vóxeles ni caras, se omite y se emite una textura negra para él.
- Cuando se proporciona `reference_mesh` para un lote, se empareja por índice de lote a menos que contenga solo una malla, en cuyo caso esa malla se usa para todos los elementos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `base_color` | Mapa de textura de color base RGB. Los valores son flotantes en el rango 0–1. | IMAGE |
| `metallic` | Mapa de metalicidad en escala de grises (float, 0–1). Negro cuando los colores de vóxel no contienen canal de metalicidad. | IMAGE |
| `roughness` | Mapa de rugosidad en escala de grises (float, 0–1). Negro cuando los colores de vóxel no contienen canal de rugosidad. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/es.md)

---
**Source fingerprint (SHA-256):** `419f9e064edaeb9db8d5e052cf57a3b8b77bf7e025e8a0fc9aa0e1919c06b51c`
