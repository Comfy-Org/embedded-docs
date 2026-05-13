> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/es.md)

El nodo ImageFlip invierte imágenes a lo largo de diferentes ejes. Puede invertir imágenes verticalmente a lo largo del eje x u horizontalmente a lo largo del eje y. El nodo utiliza operaciones torch.flip para realizar la inversión según el método seleccionado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a invertir |
| `método_volteo` | STRING | Sí | "x-axis: vertically"<br>"y-axis: horizontally" | La dirección de inversión a aplicar (predeterminado: "x-axis: vertically") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `imagen` | IMAGE | La imagen de salida invertida |

---
**Source fingerprint (SHA-256):** `5cb9949c53653192b1a696179351976c3a87e2e7afc4634624b4d827ad75b527`
