> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/es.md)

## Descripción General

El nodo Krea 2 Style Reference permite agregar una imagen de referencia para influir en el estilo de una generación de imágenes Krea 2. Puedes encadenar múltiples referencias de estilo (hasta 10 en total) y alimentar el resultado combinado en un nodo Krea 2 Image. Cada imagen que proporciones se carga en el almacenamiento de ComfyAPI y se pasa como una URL.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | - | Imagen de referencia cuyo estilo influye en la generación. |
| `fuerza` | FLOAT | Sí | -2.0 a 2.0 (paso: 0.05) | Intensidad de la referencia; los valores negativos invierten la influencia del estilo (valor predeterminado: 1.0). |
| `style_reference` | STYLE_REF | No | - | Cadena opcional de referencias de estilo entrantes; este nodo agrega una más. |

**Nota sobre restricciones:** Puedes encadenar un máximo de 10 referencias de estilo en total. Si intentas agregar una 11.ª referencia, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `style_reference` | STYLE_REF | Una lista de entradas de referencia de estilo, cada una contiene una URL y un valor de intensidad. Alimenta esta salida en un nodo Krea 2 Image. |

---
**Source fingerprint (SHA-256):** `7f87568a1cd5038571f3188cfb1d71e15533ea19eee01d7826fe574a1a4dc88d`
