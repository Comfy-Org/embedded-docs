> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/es.md)

El nodo Recorte de Imagen extrae una sección rectangular de una imagen de entrada. Se define la región a conservar especificando las coordenadas de su esquina superior izquierda y su ancho y alto. El nodo devuelve entonces la porción recortada de la imagen original.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | N/A | La imagen de entrada que se va a recortar. |
| `crop_region` | BOUNDINGBOX | Sí | N/A | Define el área rectangular a extraer de la imagen. Se especifica mediante `x` (inicio horizontal), `y` (inicio vertical), `width` (ancho) y `height` (alto). Si la región definida se extiende más allá de los bordes de la imagen, se ajustará automáticamente para que quepa dentro de las dimensiones de la imagen. |

**Nota sobre las Restricciones de la Región:** La región de recorte se restringe automáticamente para permanecer dentro de los límites de la imagen de entrada. Si la coordenada `x` o `y` especificada es mayor que el ancho o alto de la imagen, se establecerá en la posición válida máxima. El ancho y alto resultantes del recorte se ajustarán para que la región no exceda los bordes de la imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La sección recortada de la imagen de entrada original. |