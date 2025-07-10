`CodificarTextoCLIPFlux` es un nodo avanzado de codificación de texto en ComfyUI, diseñado específicamente para la arquitectura Flux. Utiliza un mecanismo de doble codificador (CLIP-L y T5XXL) para procesar tanto palabras clave estructuradas como descripciones detalladas en lenguaje natural, proporcionando al modelo Flux una comprensión textual más precisa y completa para mejorar la calidad de la generación de imágenes a partir de texto.

Este nodo se basa en la colaboración de dos codificadores:

1. La entrada `clip_l` es procesada por el codificador CLIP-L, extrayendo características como estilo y tema, ideal para descripciones concisas.
2. La entrada `t5xxl` es procesada por el codificador T5XXL, especializado en comprender descripciones complejas y detalladas en lenguaje natural.
3. Los resultados de ambos codificadores se fusionan y, junto con el parámetro `orientación`, generan una incrustación condicional unificada (`ACONDICIONAMIENTO`) para los nodos de muestreo Flux, controlando el grado de coincidencia entre el contenido generado y la descripción textual.

## Entradas

| Nombre del parámetro | Tipo de dato | Método de entrada | Valor por defecto | Rango | Función |
|---------------------|--------------|-------------------|-------------------|-------|---------|
| `clip`              | CLIP         | Entrada de nodo   | Ninguno           | -     | Debe ser un modelo CLIP compatible con Flux, que incluya los codificadores CLIP-L y T5XXL |
| `clip_l`            | STRING       | Caja de texto     | Ninguno           | Hasta 77 tokens | Adecuado para descripciones concisas de palabras clave, como estilo o tema |
| `t5xxl`             | STRING       | Caja de texto     | Ninguno           | Prácticamente ilimitado | Adecuado para descripciones detalladas en lenguaje natural, expresando escenas y detalles complejos |
| `orientación`       | FLOAT        | Deslizador        | 3.5               | 0.0 - 100.0 | Controla la influencia de las condiciones textuales en el proceso de generación; valores más altos significan mayor adherencia al texto |

## Salidas

| Nombre de salida    | Tipo de dato    | Función |
|--------------------|-----------------|---------|
| `ACONDICIONAMIENTO`| CONDITIONING    | Contiene la incrustación fusionada de ambos codificadores y el parámetro de orientación, utilizada para la generación condicional de imágenes |

## Ejemplos de uso

### Ejemplos de mensajes

- **Entrada clip_l** (palabras clave):
  - Utiliza combinaciones estructuradas y concisas de palabras clave
  - Ejemplo: `masterpiece, best quality, portrait, oil painting, dramatic lighting`
  - Enfócate en el estilo, la calidad y el tema principal

- **Entrada t5xxl** (descripción en lenguaje natural):
  - Utiliza descripciones completas y fluidas de la escena
  - Ejemplo: `A highly detailed portrait in oil painting style, featuring dramatic chiaroscuro lighting that creates deep shadows and bright highlights, emphasizing the subject's features with renaissance-inspired composition.`
  - Enfócate en los detalles de la escena, relaciones espaciales y efectos de luz

### Notas

1. Asegúrate de usar un modelo CLIP compatible con la arquitectura Flux
2. Se recomienda rellenar tanto `clip_l` como `t5xxl` para aprovechar la ventaja del doble codificador
3. Ten en cuenta el límite de 77 tokens para `clip_l`
4. Ajusta el parámetro `orientación` según los resultados generados
