`CLIPMergeSimple` es un nodo avanzado de fusión de modelos utilizado para combinar dos modelos codificadores de texto CLIP basándose en una proporción especificada.

Este nodo se especializa en fusionar dos modelos CLIP basándose en una proporción especificada, combinando efectivamente sus características. Aplica selectivamente parches de un modelo a otro, excluyendo componentes específicos como los IDs de posición y la escala de logit, para crear un modelo híbrido que combina características de ambos modelos fuente.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `clip1`   | CLIP      | El primer modelo CLIP que se va a fusionar. Sirve como el modelo base para el proceso de fusión. |
| `clip2`   | CLIP      | El segundo modelo CLIP que se va a fusionar. Sus parches clave, excepto los IDs de posición y la escala de logit, se aplican al primer modelo según la proporción especificada. |
| `ratio`   | FLOAT     | Rango `0.0 - 1.0`, determina la proporción de características del segundo modelo que se fusionarán en el primer modelo. Una proporción de 1.0 significa adoptar completamente las características del segundo modelo, mientras que 0.0 retiene solo las características del primer modelo. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `clip`    | CLIP      | El modelo CLIP resultante de la fusión, que incorpora características de ambos modelos de entrada según la proporción especificada. |

## Explicación del Mecanismo de Fusión

### Algoritmo de Fusión

El nodo utiliza un promedio ponderado para fusionar los dos modelos:

1. **Clonar Modelo Base**: Primero clona `clip1` como modelo base
2. **Obtener Parches**: Obtiene todos los parches clave de `clip2`
3. **Filtrar Claves Especiales**: Omite las claves que terminan en `.position_ids` y `.logit_scale`
4. **Aplicar Fusión Ponderada**: Utiliza la fórmula `(1.0 - ratio) * clip1 + ratio * clip2`

### Explicación del Parámetro Ratio

- **ratio = 0.0**: Utiliza completamente clip1, ignora clip2
- **ratio = 0.5**: 50% de contribución de cada modelo
- **ratio = 1.0**: Utiliza completamente clip2, ignora clip1

## Casos de Uso

1. **Fusión de Estilos de Modelos**: Combinar características de modelos CLIP entrenados con diferentes datos
2. **Optimización de Rendimiento**: Equilibrar fortalezas y debilidades de diferentes modelos
3. **Investigación Experimental**: Explorar combinaciones de diferentes codificadores CLIP
