# Crear Cajas Delimitadoras

Este nodo proporciona una interfaz de lienzo para dibujar cuadros delimitadores alrededor de objetos o regiones de texto en una imagen. Genera las coordenadas de los cuadros delimitadores en el espacio de píxeles, datos de elementos estructurados compatibles con el formato de indicaciones de Ideogram, y una imagen de previsualización que muestra los cuadros dibujados con etiquetas y paletas de colores.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `fondo` | Imagen opcional utilizada como fondo en el lienzo y la previsualización. | IMAGE | No | - |
| `ancho` | Ancho del lienzo y de la cuadrícula de píxeles para los cuadros delimitadores (predeterminado: 1024). | INT | Sí | 64 a 16384 (paso: 16) |
| `alto` | Alto del lienzo y de la cuadrícula de píxeles para los cuadros delimitadores (predeterminado: 1024). | INT | Sí | 64 a 16384 (paso: 16) |
| `estado_del_editor` | Dibuja cuadros delimitadores y configura el tipo, texto, descripción y paleta de colores de cada cuadro. Comienza con el elemento de fondo primero y el de primer plano al final. | BOUNDING_BOXES | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `vista_previa` | Una imagen RGB que muestra el lienzo con todos los cuadros delimitadores renderizados, incluyendo etiquetas, muestras de paletas de colores y texto descriptivo. | IMAGE |
| `cajas_delimitadoras` | Una lista de cuadros delimitadores en coordenadas de píxeles, donde cada cuadro contiene valores de x, y, ancho y alto. | BOUNDING_BOX |
| `elementos` | Un arreglo estructurado de objetos de elementos, cada uno con tipo, coordenadas del cuadro delimitador (normalizadas 0-1000), texto (para tipo texto), descripción y paleta de colores. | ARRAY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/es.md)

---
**Source fingerprint (SHA-256):** `a63939f13edc6c6507590a390dcd6d0a3321febb5831baab1655d9952228612c`
