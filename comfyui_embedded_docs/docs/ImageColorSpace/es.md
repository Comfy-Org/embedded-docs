# Convertir espacio de color de imagen

El nodo ImageColorSpace convierte imágenes entre los espacios de color sRGB (Rec.709), Rec.709 lineal, HDR (Rec.2020 HLG) y HDR PQ (Rec.2020 PQ). Cuando convierte a salida SDR, o de HDR PQ a HDR, aplica tone mapping a la luminancia excedente en todo el lote y comprime los colores fuera de gamut; la salida linear y las conversiones de linear a HDR preservan valores extendidos sin aplicar tone mapping. Las conversiones se calculan en float32 y cualquier canal alfa se pasa sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `image` | La imagen de entrada que se va a convertir. | IMAGE | Sí | Cualquier imagen válida. |
| `source` | Espacio de color de los píxeles de entrada. Predeterminado: "sRGB". | COMBO | Sí | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |
| `destination` | Espacio de color de los píxeles de salida. Configure el nodo de guardado con este mismo espacio de color. Predeterminado: "sRGB". | COMBO | Sí | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen convertida en el espacio de color de destino especificado. | IMAGE |

## Notas

- Linear 1.0 usa el mismo blanco de referencia de 203 nits que sRGB; HLG usa una pantalla de referencia de 1000 nits.
- La salida linear y las conversiones de linear a HDR preservan valores extendidos sin aplicar tone mapping.
- La salida SDR y la conversión de PQ a HLG aplican tone mapping a la luminancia excedente en todo el lote (compartiendo un mismo punto blanco para que la exposición no cambie fotograma a fotograma) y comprimen los colores fuera de gamut.
- Las conversiones se calculan en float32 y devuelven el dispositivo y dtype intermedios.
- El alfa directo (straight alpha) no se transforma en color; solo se convierten los canales RGB.
- Si `source` y `destination` son iguales, no se aplica ninguna transformación de color; la imagen solo se mueve al dispositivo y dtype intermedios.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/es.md)

---
**Source fingerprint (SHA-256):** `04ae447a9f9805341e31755ad0fa56746ac0371fa2cb9bda95df3879c9dbead7`
