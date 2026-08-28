# VaeDecodeShapeTrellis

Este nodo decodifica representaciones latentes de forma Trellis2 en una malla 3D. Utiliza un VAE para convertir datos latentes de forma dispersa en geometría de malla y también genera datos de subdivisión de forma producidos durante la decodificación. El nodo admite entradas latentes tanto individuales como por lotes y ajusta automáticamente la orientación de la malla al sistema de coordenadas esperado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `muestras` | Las muestras latentes a decodificar, incluyendo el tensor de muestra y los datos de coordenadas dispersas. El diccionario latente también puede contener campos opcionales: `coord_counts` para formas por lotes, `coord_resolution` para controlar la resolución de la malla y `model_frame` para la orientación del sistema de coordenadas. | LATENT | Sí | None |
| `vae` | El modelo VAE utilizado para decodificar el latente de forma en una malla. | VAE | Sí | None |

### Notas sobre `samples`

- La entrada `samples` es un diccionario latente que debe contener el tensor `samples` y las coordenadas dispersas `coords`.
- Si `coord_counts` está presente, debe ser un tensor 1D de enteros no negativos, y la suma de todos los recuentos debe ser igual al número total de filas de coordenadas. Cada recuento representa una forma en el lote.
- Si se proporciona `coord_resolution`, la resolución de la malla se calcula como `coord_resolution * 16`. De lo contrario, se utiliza el búfer de resolución integrado del VAE (valor predeterminado: 1024).
- Si `model_frame` está configurado en `"z_up"`, los vértices de la malla decodificada se rotan de un sistema de coordenadas Z-up a la convención Y-up utilizada por glTF. El valor predeterminado es `"y_up"`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `malla` | La malla 3D decodificada, que contiene posiciones de vértices e índices de caras. | MESH |
| `shape_subdivides` | Datos de subdivisión de forma producidos en cada etapa del proceso de decodificación. | SHAPE_SUBDIVIDES |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/es.md)

---
**Source fingerprint (SHA-256):** `50f1b8200bd750671473278aaf94e6b08d6f9a6a72d5d1dc882ea7ab87084681`
