# Muestrear fotograma de video

El nodo `VideoFrameSample` extrae un número fijo de fotogramas de un video utilizando una de cuatro estrategias. Para las estrategias contiguas "head" y "tail", la salida es una referencia de video diferida (los fotogramas no se decodifican); para las estrategias no contiguas "uniform" y "random", solo se decodifican los fotogramas seleccionados.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `video` | Video de entrada. | VIDEO | Sí | – |
| `num_frames` | Número de fotogramas a muestrear (por defecto: 16). | INT | Sí | 1 – 9999 |
| `estrategia` | Estrategia de muestreo (por defecto: "uniform"). | COMBO | Sí | `"uniform"`<br>`"head"`<br>`"tail"`<br>`"random"` |
| `semilla` | Semilla aleatoria, solo se usa con la estrategia "random" (por defecto: 0). | INT | Sí | 0 – 18446744073709551615 |

- `num_frames` se ajusta automáticamente al número total de fotogramas del video de entrada.
- El parámetro `seed` no tiene efecto a menos que `strategy` esté configurado como `"random"`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | Video muestreado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/es.md)

---
**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`
