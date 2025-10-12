> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/es.md)

El nodo LatentBlend combina dos muestras latentes fusionándolas mediante un factor de mezcla especificado. Toma dos entradas latentes y crea una nueva salida donde la primera muestra se pondera por el factor de mezcla y la segunda muestra se pondera por el inverso. Si las muestras de entrada tienen formas diferentes, la segunda muestra se redimensiona automáticamente para coincidir con las dimensiones de la primera muestra.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `muestras1` | LATENT | Sí | - | La primera muestra latente a mezclar |
| `muestras2` | LATENT | Sí | - | La segunda muestra latente a mezclar |
| `factor_de_mezcla` | FLOAT | Sí | 0 a 1 | Controla la proporción de mezcla entre las dos muestras (valor predeterminado: 0.5) |

**Nota:** Si `samples1` y `samples2` tienen formas diferentes, `samples2` se redimensionará automáticamente para coincidir con las dimensiones de `samples1` usando interpolación bicúbica con recorte central.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latent` | LATENT | La muestra latente mezclada que combina ambas muestras de entrada |