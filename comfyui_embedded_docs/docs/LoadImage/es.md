Haz clic derecho en el nodo y selecciona **Abrir en Editor de Máscaras** desde el menú para abrir el editor de máscaras de la imagen cargada.

> Tutorial oficial del editor de máscaras: [https://docs.comfy.org/interface/maskeditor](https://docs.comfy.org/interface/maskeditor)

> Las imágenes subidas se guardan por defecto en la carpeta *ComfyUI/input*, y las imágenes se cargan por defecto desde la carpeta **input**.

El nodo Cargar Imagen está diseñado para cargar y preprocesar imágenes desde una ruta especificada. Maneja formatos de imagen con múltiples fotogramas, aplica transformaciones necesarias como la rotación basada en datos EXIF, normaliza los valores de los píxeles y, opcionalmente, genera una máscara para imágenes con un canal alfa.

## Pasos de uso
1. Arrastra y suelta archivos de imagen en la interfaz de ComfyUI, o cópialos manualmente a la carpeta `ComfyUI/input`
2. Añade el nodo Cargar Imagen a tu flujo de trabajo
3. En el menú desplegable `IMAGEN` del nodo, selecciona el archivo de imagen que deseas cargar
4. Conecta las salidas a los nodos posteriores (como VAEEncode, etc.)

## Formatos de archivo soportados
- Formatos comunes: PNG, JPG, JPEG, BMP, TIFF, WEBP
- Soporta imágenes con canal alfa (PNG, TIFF, etc.)
- Soporta secuencias de imágenes de múltiples fotogramas (GIF, TIFF, etc.)

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `IMAGEN`  | COMBO[STRING] | El parámetro `IMAGEN` especifica el identificador de la imagen que se va a cargar y procesar. Es crucial para determinar la ruta al archivo de imagen y posteriormente cargar la imagen para su transformación y normalización. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `IMAGEN`  | IMAGE        | La imagen procesada, con valores de píxeles normalizados y transformaciones aplicadas según sea necesario. Lista para procesamiento o análisis posterior. |
| `MASCARA` | MASK         | (Opcional) Proporciona una máscara para la imagen, útil cuando la imagen incluye un canal alfa para transparencia. |

## Detalles de la salida de máscara
- **Con canal alfa**: Extrae automáticamente la información de transparencia como máscara
- **Modo paleta con transparencia**: Convierte a RGBA y extrae la máscara
- **Sin información de transparencia**: Genera una máscara vacía de 64x64
- Rango de valores de la máscara: 0-1 (0 = transparente, 1 = opaco)

## Actualización de archivos
- El nodo detecta automáticamente los cambios en el contenido del archivo (mediante hash SHA256)
- Al reemplazar un archivo con el mismo nombre, el flujo de trabajo se recargará automáticamente
- No es necesario reiniciar ComfyUI para usar la imagen actualizada
