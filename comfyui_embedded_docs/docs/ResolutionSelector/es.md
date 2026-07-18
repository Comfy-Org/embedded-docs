El nodo Selector de Resolución calcula el ancho y alto en píxeles de una imagen basándose en una relación de aspecto seleccionada y una resolución total objetivo en megapíxeles. Es útil para generar dimensiones consistentes para otros nodos, como el nodo de Imagen Latente Vacía. Las dimensiones de salida siempre se redondean al múltiplo de 8 más cercano.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `relación_de_aspecto` | La relación de aspecto para las dimensiones de salida (predeterminado: `"SQUARE"`). | COMBO | Sí | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` |
| `megapíxeles` | Total de megapíxeles objetivo. 1.0 MP ≈ 1024×1024 para una relación de aspecto cuadrada (predeterminado: 1.0). | FLOAT | Sí | 0.1 - 16.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `ancho` | El ancho calculado en píxeles, que es un múltiplo de 8. | INT |
| `alto` | La altura calculada en píxeles, que es un múltiplo de 8. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/es.md)

---
**Source fingerprint (SHA-256):** `221d38fa72c9989e06b706d33fd3e0dc4caa0f741dd2931864c58a6bd7f52613`
