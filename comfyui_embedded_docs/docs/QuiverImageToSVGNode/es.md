# Quiver Imagen a SVG (Heredado)

Este nodo convierte una imagen ráster en un gráfico vectorial escalable (SVG) mediante los modelos de vectorización de Quiver AI. Envía la imagen a una API externa que la procesa y devuelve el resultado vectorizado.

**Nota:** Este nodo está marcado como obsoleto en el código fuente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `imagen` | Imagen de entrada para vectorizar. | IMAGE | Sí | N/A |
| `recorte_automático` | Recorta automáticamente al sujeto dominante (predeterminado: False). | BOOLEAN | Sí | True<br>False |
| `modelo` | Modelo que se usará para la vectorización a SVG. Al seleccionar un modelo se revelan parámetros adicionales específicos de ese modelo: `target_size` (tamaño de redimensionado cuadrado objetivo en píxeles; 0 mantiene el tamaño de la imagen de origen; de lo contrario, 128 a 4096), `temperature`, `top_p` y `presence_penalty`. | DYNAMIC_COMBO | Sí | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales no son deterministas independientemente del valor de la semilla. Este parámetro tiene funcionalidad de "control after generate" (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `reasoning_effort` | Cuánto razonamiento dedica el modelo antes de dibujar. Los niveles más altos mejoran el detalle y consumen más tokens. Solo lo usan los modelos Arrow 2 (predeterminado: "high"). | COMBO | No | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `SVG` | La salida SVG vectorizada. | SVG |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/es.md)

---
---
**Source fingerprint (SHA-256):** `3f5b97794fa4c2e87d954d98f966d4ef0fddd1c3b1054fba552e282d6ac21c83`
