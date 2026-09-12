# Pixal3DMultiViewConditioning

## Resumen

El nodo Pixal3D Multi-View Conditioning es una estructura de órbita fija que genera vistas frontales, laterales, traseras y laterales de un objeto a intervalos de 90 grados. Se utiliza para crear vistas enmarcadas para aplicaciones Pixal3D, donde el objeto abarca aproximadamente 1/1.1 de la imagen en su anchura máxima, manteniendo la misma escala en cada vista.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision con pesos NAF incluidos. | MODEL | Sí | N/A |
| `fov` | FOV horizontal en grados de las vistas enmarcadas. | FLOAT | Sí | 1.0 - 170.0 |
| `frontal` | Vista cuadrada del lado frontal del objeto, con alpha o en un fondo negro. | IMAGE | No | N/A |
| `izquierda` | Vista cuadrada del lado izquierdo del objeto, con alpha o en un fondo negro. | IMAGE | Opcional | N/A |
| `trasera` | Vista cuadrada del lado trasero del objeto, con alpha o en un fondo negro. | IMAGE | Opcional | N/A |
| `derecha` | Vista cuadrada del lado derecho del objeto, con alpha o en un fondo negro. | IMAGE | Opcional | N/A |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `positivo` | La salida de condicionamiento positivo para el nodo Pixal3D Multi-View Conditioning. | CONDITIONING |
| `negativo` | La salida de condicionamiento negativo para el nodo Pixal3D Multi-View Conditioning. | CONDITIONING |

## Notas

- El parámetro `fov` controla el campo de visión horizontal de las vistas enmarcadas. Un valor de 20 grados es típico para renders de estructuras y la mayoría de los generadores de vistas múltiples.
- La primera vista conectada (orden frontal, izquierdo, trasero, derecho) se considera frontal, y la malla se coloca en esta vista.
- Si no se proporciona una vista frontal, se genera un aviso y la malla se coloca con la primera vista conectada como su frontal.
- El nodo asume que las vistas son cuadradas y enmarcadas como la estructura. El objeto debe abarcar aproximadamente 1/1.1 de la imagen en su anchura máxima, y la misma escala debe mantenerse en cada vista.
- El nodo genera dos objetos de condicionamiento, uno para el condicionamiento positivo y otro para el negativo. Estos pueden utilizarse para condicionar modelos Pixal3D u otros nodos que acepten entradas de condicionamiento.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/es.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`
