> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/es.md)

El nodo Magnific Image Relight ajusta la iluminación de una imagen de entrada. Puede aplicar iluminación estilizada basada en un mensaje de texto o transferir las características de iluminación de una imagen de referencia opcional. El nodo ofrece varios controles para ajustar el brillo, el contraste y el ambiente general del resultado final.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | N/A | La imagen a reiluminar. Se requiere exactamente una imagen. Las dimensiones mínimas son 160x160 píxeles. La relación de aspecto debe estar entre 1:3 y 3:1. |
| `prompt` | STRING | No | N/A | Guía descriptiva para la iluminación. Admite notación de énfasis (1-1.4). El valor predeterminado es una cadena vacía. |
| `light_transfer_strength` | INT | Sí | 0 a 100 | Intensidad de la aplicación de transferencia de luz. Valor predeterminado: 100. |
| `style` | COMBO | Sí | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` | Preferencia de resultado estilístico. |
| `interpolate_from_original` | BOOLEAN | Sí | N/A | Restringe la libertad de generación para que coincida más con el original. Valor predeterminado: Falso. |
| `change_background` | BOOLEAN | Sí | N/A | Modifica el fondo según el mensaje o la referencia. Valor predeterminado: Verdadero. |
| `preserve_details` | BOOLEAN | Sí | N/A | Mantiene la textura y los detalles finos del original. Valor predeterminado: Verdadero. |
| `advanced_settings` | DYNAMICCOMBO | Sí | `"disabled"`<br>`"enabled"` | Opciones de ajuste fino para el control avanzado de iluminación. Cuando se establece en `"enabled"`, los parámetros adicionales estarán disponibles. |
| `reference_image` | IMAGE | No | N/A | Imagen de referencia opcional para transferir la iluminación. Si se proporciona, se requiere exactamente una imagen. Las dimensiones mínimas son 160x160 píxeles. La relación de aspecto debe estar entre 1:3 y 3:1. |

**Nota sobre la Configuración Avanzada:** Cuando `advanced_settings` se establece en `"enabled"`, los siguientes parámetros anidados se activan:

* `whites`: Ajusta los tonos más brillantes de la imagen. Rango: 0 a 100. Valor predeterminado: 50.
* `blacks`: Ajusta los tonos más oscuros de la imagen. Rango: 0 a 100. Valor predeterminado: 50.
* `brightness`: Ajuste general del brillo. Rango: 0 a 100. Valor predeterminado: 50.
* `contrast`: Ajuste del contraste. Rango: 0 a 100. Valor predeterminado: 50.
* `saturation`: Ajuste de la saturación del color. Rango: 0 a 100. Valor predeterminado: 50.
* `engine`: Selección del motor de procesamiento. Opciones: `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
* `transfer_light_a`: La intensidad de la transferencia de luz. Opciones: `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
* `transfer_light_b`: También modifica la intensidad de la transferencia de luz. Se puede combinar con el control anterior para obtener efectos variados. Opciones: `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
* `fixed_generation`: Garantiza un resultado coherente con la misma configuración. Valor predeterminado: Verdadero.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen reiluminada. |

---
**Source fingerprint (SHA-256):** `c260b7c88a267a20fdea7f436404fe96ede782bc522ab29da36e94c20f7330cd`
