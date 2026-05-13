> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/es.md)

El nodo Morfología aplica diversas operaciones morfológicas a las imágenes, las cuales son operaciones matemáticas utilizadas para procesar y analizar formas en imágenes. Puede realizar operaciones como erosión, dilatación, apertura, cierre y más, utilizando un tamaño de kernel personalizable para controlar la intensidad del efecto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada a procesar |
| `operation` | STRING | Sí | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | La operación morfológica a aplicar (predeterminado: "erode") |
| `kernel_size` | INT | Sí | 3-999 | El tamaño del kernel del elemento estructurante (predeterminado: 3). Debe ser un número impar. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen procesada después de aplicar la operación morfológica |

---
**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`
