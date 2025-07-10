El nodo `Promedio de Acondicionamiento` se utiliza para mezclar dos conjuntos diferentes de condiciones (como prompts de texto) según un peso especificado, generando una nueva condición que se sitúa entre ambas. Ajustando el parámetro de peso, puedes controlar de forma flexible la influencia de cada condición en el resultado final. Es especialmente útil para la interpolación de prompts, fusión de estilos y otros casos avanzados.

Como se muestra en la imagen, al ajustar la fuerza de `acondicionamiento_a`, puedes obtener un resultado intermedio entre las dos condiciones.

![example](./asset/example.webp)

**Explicación del ejemplo**
`conditioning_to` — `acondicionamiento_a`
`conditioning_from` — `acondicionamiento_de`
`conditioning_to_strength` — `fuerza_de_acondicionamiento_a`

## Entradas

| Nombre del parámetro             | Tipo de dato     | Descripción |
|----------------------------------|------------------|-------------|
| `acondicionamiento_a`            | CONDITIONING     | Vector de condición objetivo, sirve como base principal para el promedio ponderado. |
| `acondicionamiento_de`           | CONDITIONING     | Vector de condición fuente, que se mezclará con el objetivo según el peso especificado. |
| `fuerza_de_acondicionamiento_a`  | FLOAT            | Peso de la condición objetivo, rango 0.0-1.0, por defecto 1.0, paso 0.01. |

## Salidas

| Nombre del parámetro   | Tipo de dato     | Descripción |
|-----------------------|------------------|-------------|
| `acondicionamiento`   | CONDITIONING     | Devuelve el vector de condición mezclado, reflejando el resultado del promedio ponderado. |

## Casos de uso típicos

- **Interpolación de prompts**: Transición suave entre dos prompts de texto diferentes, generando contenido de estilo o significado intermedio.
- **Fusión de estilos**: Combina diferentes estilos artísticos o condiciones semánticas para crear nuevos efectos.
- **Ajuste de fuerza**: Control preciso de la influencia de una condición en el resultado ajustando el peso.
- **Exploración creativa**: Explora efectos generativos diversos mezclando diferentes prompts.
