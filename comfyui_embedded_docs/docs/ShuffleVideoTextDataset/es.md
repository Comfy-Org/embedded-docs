# Mezclar Pares de Video-Texto

Este nodo mezcla aleatoriamente el orden de los pares de video y texto, manteniendo cada video emparejado con su texto correspondiente. Toma dos listas de igual longitud y aplica la misma permutación aleatoria a ambas, asegurando que los emparejamientos originales se conserven después de la mezcla.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `videos` | Lista de videos a mezclar. | VIDEO | Sí | Lista de elementos de video |
| `texts` | Lista de textos a mezclar. | STRING | Sí | Lista de cadenas de texto |
| `seed` | Semilla aleatoria para controlar el orden de mezcla (por defecto: 0). | INT | Sí | 0 a 18446744073709551615 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `videos` | Videos mezclados en el nuevo orden aleatorio. | VIDEO |
| `texts` | Textos mezclados en el mismo nuevo orden que los videos. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/es.md)

---
**Source fingerprint (SHA-256):** `33b763a6d48ca1036d5267139f90eadb3b2080a02fa57ce5bcae6087a077efa1`
