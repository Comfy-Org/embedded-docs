> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/es.md)

Extrae todas las líneas de borde de las fotos, como si usaras un bolígrafo para delinear una foto, dibujando los contornos y los límites de los detalles de los objetos.

## Principio de Funcionamiento

Imagina que eres un artista que necesita usar un bolígrafo para delinear una foto. El nodo Canny actúa como un asistente inteligente, ayudándote a decidir dónde dibujar líneas (bordes) y dónde no.

Este proceso es como un trabajo de selección:

- **Umbral alto** es el "estándar de línea que debe dibujarse": solo se dibujarán las líneas de contorno muy obvias y claras, como los contornos faciales de las personas y los marcos de los edificios.
- **Umbral bajo** es el "estándar de línea que definitivamente no debe dibujarse": los bordes demasiado débiles se ignorarán para evitar dibujar ruido y líneas sin significado.
- **Área intermedia**: los bordes entre los dos estándares se dibujarán juntos si se conectan a "líneas que deben dibujarse", pero no se dibujarán si están aislados.

La salida final es una imagen en blanco y negro, donde las partes blancas son las líneas de borde detectadas y las partes negras son las áreas sin bordes.

## Entradas

| Nombre del Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango     | Descripción de la Función |
|----------------------|--------------|-----------------|-------------------|-----------|---------------------------|
| `imagen`              | IMAGE        | Entrada         | -                 | -         | Foto original que necesita extracción de bordes |
| `umbral_bajo`      | FLOAT        | Widget          | 0.4               | 0.01-0.99 | Umbral bajo, determina qué bordes débiles ignorar. Valores más bajos conservan más detalles pero pueden generar ruido |
| `umbral_alto`     | FLOAT        | Widget          | 0.8               | 0.01-0.99 | Umbral alto, determina qué bordes fuertes conservar. Valores más altos solo mantienen las líneas de contorno más obvias |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `imagen`          | IMAGE        | Imagen de bordes en blanco y negro, las líneas blancas son bordes detectados, las áreas negras son partes sin bordes |

## Comparación de Parámetros

![Imagen Original](./asset/input.webp)

![Comparación de Parámetros](./asset/compare.webp)

**Problemas Comunes:**

- Bordes rotos: Intenta bajar el umbral alto
- Demasiado ruido: Sube el umbral bajo
- Faltan detalles importantes: Baja el umbral bajo
- Bordes demasiado toscos: Verifica la calidad y resolución de la imagen de entrada