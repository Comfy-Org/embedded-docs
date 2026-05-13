> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/es.md)

El nodo Ampliación de Imagen Magnífica (Precisa V2) realiza una ampliación de imágenes de alta fidelidad con control preciso sobre nitidez, granulado y mejora de detalles. Procesa imágenes a través de una API externa, admitiendo una resolución máxima de salida de hasta 10060×10060 píxeles. El nodo ofrece diferentes estilos de procesamiento y puede reducir automáticamente la escala de la entrada si la salida solicitada supera el tamaño máximo permitido.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se ampliará. Se requiere exactamente una imagen. Las dimensiones mínimas son 160x160 píxeles. La relación de aspecto debe estar entre 1:3 y 3:1. |
| `scale_factor` | STRING | Sí | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` | El multiplicador de ampliación deseado. |
| `flavor` | STRING | Sí | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` | El estilo de procesamiento. "sublime" es para uso general, "photo" está optimizado para fotografías y "photo_denoiser" es para fotos con ruido. |
| `sharpen` | INT | No | 0 a 100 | Controla la intensidad del enfoque de la imagen para aumentar la definición de bordes y la claridad. Valores más altos producen un resultado más nítido. Valor predeterminado: 7. |
| `smart_grain` | INT | No | 0 a 100 | Agrega granulado inteligente o mejora de textura para evitar que la imagen ampliada se vea demasiado suave o artificial. Valor predeterminado: 7. |
| `ultra_detail` | INT | No | 0 a 100 | Controla la cantidad de detalles finos, texturas y microdetalles añadidos durante el proceso de ampliación. Valor predeterminado: 30. |
| `auto_downscale` | BOOLEAN | No | - | Cuando está habilitado, el nodo reducirá automáticamente la escala de la imagen de entrada si las dimensiones de salida calculadas superan la resolución máxima permitida de 10060x10060 píxeles. Esto ayuda a prevenir errores, pero puede afectar la calidad. Valor predeterminado: Falso. |

**Nota:** Si `auto_downscale` está deshabilitado y el tamaño de salida solicitado (dimensiones de entrada × `scale_factor`) supera los 10060x10060 píxeles, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen ampliada resultante. |

---
**Source fingerprint (SHA-256):** `cceff30e9702c6a24ab8102698c59f1afb20ec50e7f279b3c0d50befc9673b24`
