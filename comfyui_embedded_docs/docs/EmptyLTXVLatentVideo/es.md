# EmptyLTXVLatentVideo

El nodo EmptyLTXVLatentVideo crea un tensor latente vacío para el procesamiento de video. Genera un punto de partida en blanco con el ancho, alto, longitud y tamaño de lote especificados, que puede utilizarse como entrada para flujos de trabajo de generación de video. El nodo produce una representación latente rellenada con ceros cuyas dimensiones espaciales son 32 veces más pequeñas que el ancho y alto configurados, y cuyo número de fotogramas se comprime por un factor de 8.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho del tensor de video latente (por defecto: 768, paso: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `altura` | La altura del tensor de video latente (por defecto: 512, paso: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas del video latente (por defecto: 97, paso: 8) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_del_lote` | El número de videos latentes a generar en un lote (por defecto: 1) | INT | Sí | 1 a 4096 |

Nota: El video latente se comprime en comparación con las dimensiones de entrada: las dimensiones espaciales (ancho y alto) se dividen entre 32, y el número de fotogramas (longitud) se divide entre 8 y se redondea hacia arriba al número entero más próximo. Los valores de paso para ancho, alto y longitud ayudan a mantener estas divisiones exactas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | El tensor latente vacío generado con valores cero en las dimensiones especificadas, junto con un factor de reducción espacial de 32 | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/es.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
