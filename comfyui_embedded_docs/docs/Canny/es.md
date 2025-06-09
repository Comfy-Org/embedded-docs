Extrae todas las líneas de borde de las fotos, como usar un bolígrafo para contornear una foto, dibujando los contornos y límites de detalles de los objetos.

## Principio de Funcionamiento

Imagina que eres un artista que necesita usar un bolígrafo para contornear una foto. El nodo Canny actúa como un asistente inteligente, ayudándote a decidir dónde dibujar líneas (bordes) y dónde no.

Este proceso es como un trabajo de filtrado:

- **Umbral alto** es el "estándar de línea obligatoria": solo se dibujarán líneas de contorno muy obvias y claras, como contornos faciales de personas y marcos de edificios
- **Umbral bajo** es el "estándar de definitivamente no dibujar línea": los bordes que son demasiado débiles serán ignorados para evitar dibujar ruido y líneas sin sentido
- **Área intermedia**: los bordes entre los dos estándares se dibujarán juntos si se conectan a "líneas obligatorias", pero no se dibujarán si están aislados

La salida final es una imagen en blanco y negro, donde las partes blancas son líneas de borde detectadas y las partes negras son áreas sin bordes.

## Entradas

| Nombre del Parámetro | Tipo de Dato | Método de Entrada | Valor Predeterminado | Rango de Valores | Descripción de Función |
|----------------------|--------------|-------------------|---------------------|------------------|------------------------|
| imagen | IMAGE | Conexión | - | - | Foto original que necesita extracción de bordes |
| umbral_bajo | FLOAT | Entrada Manual | 0.4 | 0.01-0.99 | Umbral bajo, determina qué bordes débiles ignorar. Valores más bajos preservan más detalles pero pueden producir ruido |
| umbral_alto | FLOAT | Entrada Manual | 0.8 | 0.01-0.99 | Umbral alto, determina qué bordes fuertes preservar. Valores más altos solo mantienen las líneas de contorno más obvias |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| imagen | IMAGE | Imagen de bordes en blanco y negro, líneas blancas son bordes detectados, áreas negras son partes sin bordes |

## Comparación de Parámetros

![Imagen Original](./asset/input.webp)

![Comparación de Parámetros](./asset/compare.webp)

**Problemas Comunes:**

- Bordes quebrados: Intenta reducir el umbral alto
- Demasiado ruido: Aumenta el umbral bajo
- Faltan detalles importantes: Reduce el umbral bajo
- Bordes demasiado ásperos: Verifica la calidad y resolución de la imagen de entrada
