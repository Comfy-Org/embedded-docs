> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/es.md)

# Nodo SAM3 Detect

## Descripción General

El nodo SAM3 Detect realiza detección y segmentación de vocabulario abierto utilizando descripciones de texto, cuadros delimitadores o indicaciones de puntos. Puede identificar y segmentar objetos en una imagen basándose en lo que describas en texto, dónde dibujes cuadros o dónde hagas clic en puntos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo SAM3 a utilizar para detección y segmentación |
| `image` | IMAGE | Sí | - | La imagen de entrada a procesar |
| `conditioning` | CONDITIONING | No | - | Condicionamiento de texto desde CLIPTextEncode. Requerido cuando se usan indicaciones de texto para detección |
| `bboxes` | BOUNDING_BOX | No | - | Cuadros delimitadores para segmentar dentro de ellos. Puede ser un solo cuadro (aplicado a todos los fotogramas), una lista de cuadros (aplicada a todos los fotogramas) o una lista de listas (cuadros por fotograma). Cuando se proporciona sin condicionamiento de texto, el nodo segmenta dentro de cada cuadro |
| `positive_coords` | STRING | No | - | Indicaciones de puntos positivos en formato JSON `[{"x": int, "y": int}, ...]` usando coordenadas de píxeles. Son puntos que deseas incluir en la segmentación |
| `negative_coords` | STRING | No | - | Indicaciones de puntos negativos en formato JSON `[{"x": int, "y": int}, ...]` usando coordenadas de píxeles. Son puntos que deseas excluir de la segmentación |
| `threshold` | FLOAT | No | 0.0 a 1.0 | Umbral de confianza para detecciones basadas en texto. Solo se conservan las detecciones con puntuaciones superiores a este valor (predeterminado: 0.5) |
| `refine_iterations` | INT | No | 0 a 5 | Número de pasos de refinamiento del decodificador SAM. Valores más altos pueden mejorar la calidad de las máscaras. Establecer en 0 para usar máscaras del detector sin refinamiento (predeterminado: 2) |
| `individual_masks` | BOOLEAN | No | True/False | Cuando está habilitado, genera máscaras separadas para cada objeto detectado en lugar de combinarlas en una sola máscara (predeterminado: False) |

### Restricciones y Notas de Parámetros

- **Indicaciones de texto**: Para usar detección basada en texto, debes proporcionar la entrada `conditioning`. Cuando se proporciona condicionamiento de texto, el nodo ejecuta detección guiada por texto en la imagen.
- **Indicaciones de cuadros**: Cuando se proporcionan `bboxes` sin condicionamiento de texto, el nodo segmenta el área dentro de cada cuadro delimitador.
- **Indicaciones de puntos**: Cuando se proporcionan `positive_coords` o `negative_coords`, el nodo utiliza segmentación basada en puntos. Los puntos se escalan automáticamente a la resolución interna del modelo.
- **Múltiples tipos de indicaciones**: Puedes combinar diferentes tipos de indicaciones. Por ejemplo, puedes proporcionar tanto condicionamiento de texto como cuadros delimitadores para restringir la detección de texto a áreas específicas.
- **Procesamiento por lotes**: El nodo admite imágenes por lotes. Al procesar múltiples fotogramas, los cuadros delimitadores se pueden proporcionar por fotograma usando un formato de lista de listas.
- **Formato JSON para puntos**: Las coordenadas de los puntos deben proporcionarse como cadenas JSON válidas en el formato `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `masks` | MASK | Máscaras de segmentación. Cuando `individual_masks` es False (predeterminado), devuelve una sola máscara combinada por fotograma. Cuando es True, devuelve máscaras individuales para cada objeto detectado |
| `bboxes` | BOUNDING_BOX | Cuadros delimitadores detectados con coordenadas y puntuaciones de confianza. Cada cuadro incluye valores de `x`, `y`, `width`, `height` y `score` |