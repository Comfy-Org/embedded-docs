> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/es.md)

El nodo StringConcatenate combina dos cadenas de texto en una sola uniéndolas con un delimitador especificado. Toma dos cadenas de entrada y un carácter o cadena delimitador, luego genera una única cadena donde las dos entradas se conectan con el delimitador colocado entre ellas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `cadena_a` | STRING | Sí | - | La primera cadena de texto a concatenar |
| `cadena_b` | STRING | Sí | - | La segunda cadena de texto a concatenar |
| `delimitador` | STRING | No | - | El carácter o cadena a insertar entre las dos cadenas de entrada (predeterminado: cadena vacía) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | STRING | La cadena combinada con el delimitador insertado entre string_a y string_b |

---
**Source fingerprint (SHA-256):** `8e33665fb14a53f6c3bbfb6a4553ac7effa96d7d16d9ab2a9d4a1249abfc62e4`
