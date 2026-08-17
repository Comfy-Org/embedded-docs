# CLIPMergeSimple

`CLIPMergeSimple` fusiona dos modelos de codificador de texto CLIP en uno solo. Clona el primer modelo CLIP como base y aplica parches de parámetros ponderados tomados del segundo modelo CLIP, de modo que el resultado combina características de ambos. El ajuste `ratio` controla la fuerza con la que contribuye cada modelo; en el valor predeterminado de 1.0, el primer modelo se usa sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|------------|-------|
| `clip1` | El primer modelo CLIP. Se clona y se usa como modelo base para la fusión. | CLIP | Sí | — |
| `clip2` | El segundo modelo CLIP. Sus parches de claves se aplican al modelo base, excepto los parches cuyas claves terminan en `.position_ids` o `.logit_scale`. | CLIP | Sí | — |
| `ratio` | Controla la fuerza relativa de los dos modelos. El modelo base (`clip1`) mantiene una fuerza igual a `ratio`, y los parches de `clip2` se aplican con una fuerza de `1.0 - ratio`. En el valor predeterminado de 1.0, la salida equivale a `clip1`; los valores más bajos mezclan más de `clip2`; en 0.0, los parches de `clip2` se aplican a plena fuerza. | FLOAT | Sí | 0.0 to 1.0 (default: 1.0, step: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `clip` | El modelo CLIP fusionado: un clon de `clip1` con los parches de `clip2` aplicados según `ratio`. | CLIP |

## Explicación del mecanismo de fusión

### Algoritmo de fusión

El nodo utiliza la aplicación ponderada de parches para combinar los dos modelos:

1. **Clonar el modelo base**: clona `clip1` para que sirva como modelo base.
2. **Obtener parches**: recopila todos los parches de claves (valores de parámetros) de `clip2`.
3. **Filtrar claves especiales**: omite las claves que terminan en `.position_ids` y `.logit_scale`, para que esos parámetros permanezcan sin cambios.
4. **Aplicar fusión ponderada**: aplica los parches de `clip2` al modelo base clonado con una fuerza de parche de `1.0 - ratio`, mientras que el modelo base mantiene una fuerza de `ratio`.

### Explicación del parámetro ratio

- **ratio = 1.0**: la fuerza base es 1.0 y la fuerza del parche es 0.0, por lo que la salida es idéntica a `clip1` (predeterminado).
- **ratio = 0.5**: la fuerza base y la fuerza del parche son ambas 0.5, por lo que ambos modelos contribuyen con la misma fuerza.
- **ratio = 0.0**: la fuerza base es 0.0 y la fuerza del parche es 1.0, así que los parches de `clip2` se aplican a plena fuerza.

## Casos de uso

1. **Fusión de estilos de modelo**: combinar características de modelos CLIP entrenados con diferentes datos.
2. **Optimización del rendimiento**: equilibrar fortalezas y debilidades de diferentes modelos.
3. **Investigación experimental**: explorar combinaciones de diferentes codificadores CLIP.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/es.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
