> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/es.md)

El nodo `ConditioningAverage` se utiliza para combinar dos conjuntos diferentes de condicionamiento (como indicaciones de texto) según un peso especificado, generando un nuevo vector de condicionamiento que se sitúa entre ambos. Al ajustar el parámetro de peso, puedes controlar de forma flexible la influencia de cada condicionamiento en el resultado final. Esto es especialmente adecuado para interpolación de indicaciones, fusión de estilos y otros casos de uso avanzados.

Como se muestra a continuación, al ajustar la intensidad de `conditioning_to`, puedes obtener un resultado intermedio entre los dos condicionamientos.

![ejemplo](./asset/example.webp)

## Entradas

| Parámetro               | Tipo Comfy    | Descripción |
|------------------------|---------------|-------------|
| `conditioning_to`      | `CONDITIONING`| El vector de condicionamiento objetivo, que sirve como base principal para el promedio ponderado. |
| `conditioning_from`    | `CONDITIONING`| El vector de condicionamiento fuente, que se fusionará con el objetivo según un peso determinado. |
| `conditioning_to_strength` | `FLOAT`    | La intensidad del condicionamiento objetivo, rango 0.0-1.0, valor predeterminado 1.0, incremento 0.01. |

## Salidas

| Parámetro        | Tipo Comfy    | Descripción |
|------------------|---------------|-------------|
| `conditioning`   | `CONDITIONING`| El vector de condicionamiento resultante tras la combinación, que refleja el promedio ponderado. |

## Casos de Uso Típicos

- **Interpolación de Indicaciones:** Transición suave entre dos indicaciones de texto diferentes, generando contenido con estilo o semántica intermedia.
- **Fusión de Estilos:** Combinar diferentes estilos artísticos o condiciones semánticas para crear efectos novedosos.
- **Ajuste de Intensidad:** Controlar con precisión la influencia de un condicionamiento particular en el resultado ajustando el peso.
- **Exploración Creativa:** Explorar diversos efectos generativos mezclando diferentes indicaciones.