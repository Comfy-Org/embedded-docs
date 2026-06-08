`CLIPMergeSimple` es un nodo avanzado de fusión de modelos utilizado para combinar dos codificadores de texto CLIP según una proporción especificada.

Este nodo se especializa en fusionar dos modelos CLIP basándose en una proporción determinada, combinando eficazmente sus características. Aplica selectivamente parches de un modelo a otro, excluyendo componentes específicos como los ID de posición y la escala logit, para crear un modelo híbrido que combina características de ambos modelos fuente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango |
| --- | --- | --- | --- | --- | --- |
| `clip1` | El primer modelo CLIP que se va a fusionar. Sirve como modelo base para el proceso de fusión. | CLIP | REQUERIDO | - | - |
| `clip2` | El segundo modelo CLIP que se va a fusionar. Sus parches clave, excepto los ID de posición y la escala logit, se aplican al primer modelo según la proporción especificada. | CLIP | REQUERIDO | - | - |
| `ratio` | Determina la proporción de características del segundo modelo que se mezclarán en el primer modelo. Una proporción de 1.0 significa adoptar completamente las características del segundo modelo, mientras que 0.0 conserva únicamente las características del primer modelo. | FLOAT | REQUERIDO | 1.0 | 0.0 - 1.0 (paso: 0.01) |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `clip` | El modelo CLIP fusionado resultante, que incorpora características de ambos modelos de entrada según la proporción especificada. | CLIP |

## Mecanismo de Fusión Explicado

### Algoritmo de Fusión

El nodo utiliza un promedio ponderado para fusionar los dos modelos:

1. **Clonar Modelo Base**: Primero clona `clip1` como modelo base
2. **Obtener Parches**: Obtiene todos los parches clave de `clip2`
3. **Filtrar Claves Especiales**: Omite las claves que terminan en `.position_ids` y `.logit_scale`
4. **Aplicar Fusión Ponderada**: Utiliza la fórmula `(1.0 - ratio) * clip1 + ratio * clip2`

### Parámetro de Proporción Explicado

- **ratio = 0.0**: Utiliza completamente clip1, ignora clip2
- **ratio = 0.5**: Contribución del 50% de cada modelo
- **ratio = 1.0**: Utiliza completamente clip2, ignora clip1

## Casos de Uso

1. **Fusión de Estilos de Modelo**: Combinar características de modelos CLIP entrenados con datos diferentes
2. **Optimización de Rendimiento**: Equilibrar fortalezas y debilidades de diferentes modelos
3. **Investigación Experimental**: Explorar combinaciones de diferentes codificadores CLIP

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/es.md)

---
**Source fingerprint (SHA-256):** `0d3c8388dbe88675ea7fb51161ab41ce898bcf63983b3d2817b16ec5bfa613e5`
