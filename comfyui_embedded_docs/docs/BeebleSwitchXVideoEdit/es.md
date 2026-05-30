> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/es.md)

# Beeble SwitchX Video Edit

Edita un video con Beeble SwitchX. Este nodo puede cambiar cualquier elemento de la escena (fondo, iluminación, vestuario) mientras preserva los píxeles y el movimiento del sujeto original. Proporcione una imagen de referencia y/o un prompt de texto para describir el nuevo aspecto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | N/A | El video de entrada a editar. Máximo 240 fotogramas, máximo ~2.77 megapíxeles por fotograma. |
| `prompt` | STRING | Sí | N/A | Una descripción textual del nuevo aspecto deseado para la escena. |
| `modo_alpha` | COMBO | Sí | `"fill"`<br>`"select"`<br>`"custom"` | El modo de máscara alfa. El modo "fill" no tiene máscara separada y rellena todo el fotograma. El modo "select" utiliza una imagen de fotograma clave única para definir el área a editar. El modo "custom" utiliza un video alfa completo para definir el área a editar fotograma por fotograma. |
| `resolución_máxima` | COMBO | Sí | `"720p"`<br>`"1080p"` | La resolución máxima para el video de salida (predeterminado: "1080p"). |
| `semilla` | INT | Sí | 0 a 2147483647 | Un valor de semilla para reproducibilidad. Usar la misma semilla con las mismas entradas producirá el mismo resultado. |
| `imagen_de_referencia` | IMAGE | No | N/A | Una imagen de referencia opcional que describe el nuevo aspecto deseado para la escena. |

### Detalles del Modo Alfa

El parámetro `alpha_mode` controla qué partes del video se editan:

- **fill**: Se edita todo el fotograma del video. No se produce una máscara alfa separada.
- **select**: Usted proporciona una imagen de fotograma clave única que define el área a editar. El nodo la utilizará para determinar qué partes del video cambiar.
- **custom**: Usted proporciona un video alfa completo que define el área a editar fotograma por fotograma. Esto le brinda un control preciso sobre qué partes de cada fotograma se editan.

Al usar el modo `select`, debe proporcionar la imagen `alpha_keyframe`. Al usar el modo `custom`, debe proporcionar el video `alpha_mask`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `alfa` | VIDEO | El video editado con los cambios de escena aplicados. |
| `alpha` | VIDEO | La máscara alfa utilizada por Beeble. Está vacía para el modo "fill", que no tiene máscara separada. |

---
**Source fingerprint (SHA-256):** `e2d67b037863f024f42c97943ec0d2daf32b547b232a7dfedd6de398f4b7ba28`
