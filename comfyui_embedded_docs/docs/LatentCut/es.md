# CorteLatente

El nodo LatentCut extrae una sección específica de muestras latentes a lo largo de una dimensión elegida. Permite recortar una porción de la representación latente especificando la dimensión (x, y o t), la posición inicial y la cantidad a extraer. El nodo maneja tanto indexación positiva como negativa y ajusta automáticamente la cantidad de extracción para mantenerse dentro de los límites disponibles.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | Las muestras latentes de entrada de las que extraer | LATENT | Sí | - |
| `dimensión` | La dimensión a lo largo de la cual cortar las muestras latentes | COMBO | Sí | "x"<br>"y"<br>"t" |
| `índice` | La posición inicial para el corte (predeterminado: 0). Los valores positivos cuentan desde el inicio, los valores negativos cuentan desde el final. El nodo ajusta automáticamente el índice para mantenerse dentro del rango válido de las muestras latentes | INT | Sí | -16384 a 16384 |
| `cantidad` | El número de elementos a extraer a lo largo de la dimensión especificada (predeterminado: 1). El nodo reduce automáticamente este valor si excede los datos disponibles más allá del índice inicial | INT | Sí | 1 a 16384 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La porción extraída de las muestras latentes | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/es.md)

---
**Source fingerprint (SHA-256):** `54f2b0cead9dce2c2cbd241d4e8c50ce85a67d3e1a40e7002056b83acbf0cf2d`
