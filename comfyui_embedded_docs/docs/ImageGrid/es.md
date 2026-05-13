> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/es.md)

El nodo **Cuadrícula de Imágenes** combina múltiples imágenes en una única cuadrícula o collage organizado. Toma una lista de imágenes y las dispone en un número específico de columnas, redimensionando cada imagen para que se ajuste a un tamaño de celda definido y añadiendo relleno opcional entre ellas. El resultado es una única imagen nueva que contiene todas las imágenes de entrada en un diseño de cuadrícula.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `imágenes` | IMAGE | Sí | - | Lista de imágenes que se organizarán en la cuadrícula. El nodo requiere al menos una imagen para funcionar. |
| `columnas` | INT | No | 1 - 20 | Número de columnas en la cuadrícula (valor predeterminado: 4). |
| `ancho_de_celda` | INT | No | 32 - 2048 | Ancho, en píxeles, de cada celda en la cuadrícula (valor predeterminado: 256). |
| `alto_de_celda` | INT | No | 32 - 2048 | Alto, en píxeles, de cada celda en la cuadrícula (valor predeterminado: 256). |
| `espaciado` | INT | No | 0 - 50 | Cantidad de relleno, en píxeles, que se colocará entre las imágenes en la cuadrícula (valor predeterminado: 4). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `image` | IMAGE | La única imagen de salida que contiene todas las imágenes de entrada dispuestas en una cuadrícula. |

---
**Source fingerprint (SHA-256):** `79d0942c79d3966d06fe804f839c1d677764cef90265bd621bf915fe6de0ad46`
