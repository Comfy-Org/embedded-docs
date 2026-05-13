> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/es.md)

El nodo AudioConcat combina dos entradas de audio uniéndolas. Toma dos entradas de audio y las conecta en el orden que especifiques, ya sea colocando el segundo audio antes o después del primero. El nodo maneja automáticamente diferentes formatos de audio convirtiendo audio mono a estéreo y emparejando las frecuencias de muestreo entre las dos entradas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio1` | AUDIO | Sí | - | La primera entrada de audio que se concatenará |
| `audio2` | AUDIO | Sí | - | La segunda entrada de audio que se concatenará |
| `dirección` | COMBO | Sí | `"after"`<br>`"before"` | Si se añade audio2 después o antes de audio1 (predeterminado: "after") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `AUDIO` | AUDIO | El audio combinado que contiene ambos archivos de audio de entrada unidos |

---
**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`
