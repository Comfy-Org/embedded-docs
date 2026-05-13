> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/es.md)

El nodo LatentBlend combina dos muestras latentes mezclándolas mediante un factor de mezcla especificado. Toma dos entradas latentes y crea una nueva salida donde la primera muestra se pondera por el factor de mezcla y la segunda muestra se pondera por el inverso. Si las muestras de entrada tienen formas diferentes, la segunda muestra se redimensiona automáticamente para coincidir con las dimensiones de la primera.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `samples1` | LATENT | Sí | - | La primera muestra latente a mezclar |
| `samples2` | LATENT | Sí | - | La segunda muestra latente a mezclar |
| `blend_factor` | FLOAT | Sí | 0 a 1 | Controla la proporción de mezcla entre las dos muestras (predeterminado: 0.5) |

**Nota:** Si `samples1` y `samples2` tienen formas diferentes, `samples2` se redimensionará automáticamente para coincidir con las dimensiones de `samples1` mediante interpolación bicúbica con recorte centrado.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `latent` | LATENT | La muestra latente mezclada que combina ambas muestras de entrada |

---
**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`
