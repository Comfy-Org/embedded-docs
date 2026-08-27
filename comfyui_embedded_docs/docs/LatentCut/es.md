# CorteLatente

El nodo LatentCut extrae una sección específica de las muestras latentes a lo largo de una dimensión elegida. Permite recortar una porción de la representación latente especificando la dimensión (x, y o t), la posición inicial y la cantidad a extraer. El nodo maneja tanto la indexación positiva como la negativa y ajusta automáticamente la cantidad extraída para mantenerse dentro de los límites disponibles.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | Las muestras latentes de entrada de las que extraer | LATENT | Sí | - |
| `dimensión` | La dimensión a lo largo de la cual cortar las muestras latentes. "x" corta a lo largo del último eje (normalmente el ancho), "y" a lo largo del penúltimo eje (normalmente la altura) y "t" a lo largo del tercer último eje (normalmente los fotogramas en latentes de video) | COMBO | Sí | "x"<br>"y"<br>"t" |
| `índice` | La posición inicial para el corte (por defecto: 0). Los valores positivos cuentan desde el inicio, los negativos desde el final. El nodo ajusta automáticamente el índice para mantenerse dentro del rango válido de las muestras latentes | INT | Sí | -16384 a 16384 |
| `cantidad` | El número de elementos a extraer a lo largo de la dimensión especificada (por defecto: 1). El nodo reduce automáticamente este valor si excediera los datos disponibles más allá del índice inicial | INT | Sí | 1 a 16384 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La porción extraída de las muestras latentes | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/es.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
