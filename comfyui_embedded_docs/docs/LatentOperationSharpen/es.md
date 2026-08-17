# OperaciónAfiladoLatente

El nodo LatentOperationSharpen aplica un efecto de afilado a representaciones latentes mediante un kernel gaussiano. Funciona normalizando los datos latentes, aplicando una convolución con un kernel de afilado personalizado y restaurando la luminancia original. Esto mejora los detalles y los bordes en la representación del espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | El radio del kernel de afilado. El tamaño completo del kernel se calcula como el doble de este valor más uno (predeterminado: 9). | INT | Sí | 1-31 |
| `sigma` | La desviación estándar del kernel gaussiano (predeterminado: 1.0). | FLOAT | Sí | 0.1-10.0 |
| `alpha` | El factor de intensidad de afilado que controla la fuerza del efecto (predeterminado: 0.1). | FLOAT | Sí | 0.0-5.0 |

Todos los parámetros son parámetros avanzados. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `operation` | Una operación de afilado que puede aplicarse a datos latentes. Aplicarla a un latente devuelve una versión afilada con la luminancia original preservada. | LATENT_OPERATION |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/es.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
