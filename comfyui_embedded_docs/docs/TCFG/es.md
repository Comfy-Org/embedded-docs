> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/es.md)

TCFG (Tangential Damping CFG) implementa una técnica de guía que refina las predicciones incondicionales (negativas) para alinearlas mejor con las predicciones condicionales (positivas). Este método mejora la calidad de la salida aplicando amortiguación tangencial a la guía incondicional, basándose en el documento de investigación referenciado como 2503.18137. El nodo modifica el comportamiento de muestreo del modelo ajustando cómo se procesan las predicciones incondicionales durante el proceso de guía libre de clasificador.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que aplicar la amortiguación tangencial CFG |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `patched_model` | MODEL | El modelo modificado con amortiguación tangencial CFG aplicada |
