> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/es.md)

El nodo AudioConcat combina dos entradas de audio uniéndolas. Toma dos entradas de audio y las conecta en el orden que especifiques, colocando el segundo audio antes o después del primero. El nodo maneja automáticamente diferentes formatos de audio convirtiendo audio mono a estéreo e igualando las tasas de muestreo entre las dos entradas.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | requerido | - | - | La primera entrada de audio a concatenar |
| `audio2` | AUDIO | requerido | - | - | La segunda entrada de audio a concatenar |
| `direction` | COMBO | requerido | after | ['after', 'before'] | Si agregar audio2 después o antes de audio1 |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | El audio combinado que contiene ambos archivos de audio de entrada unidos |