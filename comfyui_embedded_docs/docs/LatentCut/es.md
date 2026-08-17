# CorteLatente

El nodo LatentCut extrae una sección específica de las muestras latentes a lo largo de una dimensión elegida. Permite recortar una parte de la representación latente especificando la dimensión (x, y o t), la posición inicial y la cantidad a extraer. El nodo maneja tanto la indexación positiva como negativa y ajusta automáticamente la cantidad de extracción para mantenerse dentro de los límites disponibles.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | Las muestras latentes de entrada de las que extraer | LATENT | Sí | - |
| `dim` | La dimensión a lo largo de la cual cortar las muestras latentes | COMBO | Sí | "x"<br>"y"<br>"t" |
| `index` | La posición inicial para el corte (predeterminado: 0). Los valores positivos cuentan desde el inicio, los negativos desde el final. El nodo limita automáticamente el índice para mantenerse dentro del rango válido de las muestras latentes | INT | Sí | -16384 a 16384 |
| `amount` | El número de elementos a extraer a lo largo de la dimensión especificada (predeterminado: 1). El nodo reduce automáticamente este valor si excediera los datos disponibles más allá del índice inicial | INT | Sí | 1 a 16384 |

Nota: `x` corta a lo largo de la última dimensión del tensor latente, `y` a lo largo de la penúltima dimensión y `t` a lo largo de la antepenúltima dimensión. Cuando `index` es positivo, se limita a la última posición válida de la dimensión elegida; cuando es negativo, se limita para que no apunte antes del inicio de los datos. `amount` se reduce siempre que el corte solicitado se extienda más allá de los datos disponibles.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | La porción extraída de las muestras latentes | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/es.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
