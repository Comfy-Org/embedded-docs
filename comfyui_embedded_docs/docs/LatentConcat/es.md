> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/es.md)

El nodo LatentConcat combina dos muestras latentes uniéndolas a lo largo de una dimensión seleccionada. Toma dos entradas latentes y las concatena a lo largo del eje x, y o t, con la opción de controlar qué muestra aparece primero. El nodo ajusta automáticamente el tamaño del lote de la segunda entrada para que coincida con la primera antes de realizar la concatenación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `muestras1` | LATENT | Sí | - | La primera muestra latente a concatenar |
| `muestras2` | LATENT | Sí | - | La segunda muestra latente a concatenar |
| `dimensión` | COMBO | Sí | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` | La dimensión a lo largo de la cual concatenar las muestras latentes. Los valores positivos (x, y, t) colocan samples1 antes de samples2 en el resultado. Los valores negativos (-x, -y, -t) colocan samples2 antes de samples1. La correspondencia de dimensiones es: x = ancho, y = alto, t = tiempo/fotogramas |

**Nota:** La segunda muestra latente (`samples2`) se ajusta automáticamente para que coincida con el tamaño del lote de la primera muestra latente (`samples1`) antes de la concatenación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | Las muestras latentes concatenadas resultantes de combinar las dos muestras de entrada a lo largo de la dimensión especificada |

---
**Source fingerprint (SHA-256):** `46514ef85887279ec577ad88ac46f1c20f428903ee63b076888d7d5df09fde77`
