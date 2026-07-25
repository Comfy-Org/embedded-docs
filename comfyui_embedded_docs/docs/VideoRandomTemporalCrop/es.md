# Recortar video (temporal aleatorio)

Recorta aleatoriamente un rango continuo de fotogramas de un video de entrada. La longitud del recorte se controla mediante el parámetro `length`, y la posición inicial se elige usando una semilla aleatoria. El nodo opera de manera diferida (lazy), lo que significa que no procesa el video completo hasta que la salida se use en un nodo posterior.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `video` | Video de entrada. | VIDEO | Sí | – |
| `longitud` | Número de fotogramas a conservar. (por defecto: 16) | INT | Sí | min: 1, max: 99999 |
| `semilla` | Semilla aleatoria. (por defecto: 0) | INT | Sí | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `video` | Video recortado (diferido). | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/es.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
