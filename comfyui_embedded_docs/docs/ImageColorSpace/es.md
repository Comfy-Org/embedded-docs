# Convertir espacio de color de imagen

El nodo ImageColorSpace convierte imágenes entre los espacios de color sRGB (Rec.709), linear Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3 y HDR ACEScct. LogC3 utiliza la curva EI 800 con primarias Rec.709 y códigos limitados a [0, 1]; ACEScct utiliza primarias AP1 y blanco D60, con adaptación de Bradford a D65. Al convertir a salida SDR, o de HDR PQ a HDR, aplica mapeo tonal a la luminancia excedente en todo el lote y comprime colores fuera de gama; las salidas linear y ACEScct, y las conversiones de linear a HDR, conservan valores extendidos. Las salidas HLG y PQ recortan los canales negativos. Las conversiones se calculan en float32, y cualquier canal alfa se pasa sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `image` | La imagen de entrada que se va a convertir. | IMAGE | Sí | Cualquier imagen válida. |
| `source` | Espacio de color de los píxeles de entrada. Predeterminado: "sRGB". | COMBO | Sí | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |
| `destination` | Espacio de color de los píxeles de salida. Configure el nodo de guardado con este mismo espacio de color. Convierta LogC3 o ACEScct a linear antes de guardar EXR, o a sRGB/HDR/HDR PQ antes de guardar video. Predeterminado: "sRGB". | COMBO | Sí | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen convertida en el espacio de color de destino especificado. | IMAGE |

## Notas

- Linear 1.0 utiliza el mismo blanco de referencia de 203 nits que sRGB; HLG utiliza una pantalla de referencia de 1000 nits.
- Las salidas linear y ACEScct conservan valores extendidos; las conversiones de linear a HDR conservan las altas luces sin mapeo tonal.
- La salida SDR y la conversión de PQ a HLG aplican mapeo tonal a la luminancia excedente en todo el lote (compartiendo un único punto blanco para que la exposición no cambie fotograma a fotograma) y comprimen colores fuera de gama. Las salidas HLG y PQ recortan los canales negativos.
- Las conversiones se calculan en float32 y devuelven el dispositivo y dtype intermedios.
- LogC3 y ACEScct son codificaciones logarítmicas de cámara: conviértalos a linear para guardar EXR, o a sRGB/HDR/HDR PQ antes de guardar video.
- El alfa directo no se transforma en color; solo se convierten los canales RGB.
- Si `source` y `destination` son iguales, no se aplica ninguna transformación de color; la imagen solo se mueve al dispositivo y dtype intermedios.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/es.md)

---
**Source fingerprint (SHA-256):** `fdf8b4f16a1e0c7ff9a86b8cc40f6f796175205e4b1f491b595a74a8456b9b94`
