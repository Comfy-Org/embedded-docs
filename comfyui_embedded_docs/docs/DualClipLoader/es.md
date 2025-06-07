El nodo DualCLIPLoader está diseñado para cargar dos modelos CLIP simultáneamente, facilitando operaciones que requieren la integración o comparación de características de ambos modelos.

Imagina que estás en una cocina preparando un plato y tienes dos frascos de especias diferentes: uno con sal y otro con pimienta. Cada especia añade un sabor único a tu plato. Ahora, imagina que tienes una herramienta especial que te permite usar ambos frascos al mismo tiempo para sazonar tu comida. Esto es similar al nodo DualCLIPLoader. Te permite cargar y usar dos modelos CLIP diferentes simultáneamente, para que puedas combinar sus capacidades y estilos únicos y crear arte generado por IA más versátil y refinado.

## Entradas

| Parámetro    | Tipo Comfy   | Descripción |
|--------------|--------------|-------------|
| `clip_name1` | COMBO[STRING] | Especifica el nombre del primer modelo CLIP que se va a cargar. Este parámetro es crucial para identificar y recuperar el modelo correcto de una lista predefinida de modelos CLIP disponibles. |
| `clip_name2` | COMBO[STRING] | Especifica el nombre del segundo modelo CLIP que se va a cargar. Este parámetro permite cargar un segundo modelo CLIP distinto para análisis comparativo o integrador junto con el primer modelo. |
| `type`       | `opción`     | Elige entre "sdxl", "sd3", "flux" para adaptarse a diferentes modelos. |

* El orden de carga no afecta el efecto de salida.

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `clip`    | CLIP      | La salida es un modelo CLIP combinado que integra las características o funcionalidades de los dos modelos CLIP especificados. |
