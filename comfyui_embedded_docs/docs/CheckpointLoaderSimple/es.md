Este es un nodo cargador de modelos que carga archivos de modelos desde ubicaciones específicas y los descompone en tres componentes principales: el modelo principal, el codificador de texto y el codificador/decodificador de imágenes.

Este nodo detecta automáticamente todos los archivos de modelos en la carpeta `ComfyUI/models/checkpoints`, así como rutas adicionales configuradas en tu archivo `extra_model_paths.yaml`.

1. **Compatibilidad del modelo**: Asegúrate de que el modelo seleccionado sea compatible con tu flujo de trabajo. Diferentes tipos de modelos (como SD1.5, SDXL, Flux, etc.) necesitan ser emparejados con los samplers correspondientes y otros nodos
2. **Gestión de archivos**: Coloca los archivos de modelos en la carpeta `ComfyUI/models/checkpoints`, o configura otras rutas a través de extra_model_paths.yaml
3. **Actualización de interfaz**: Si se agregan nuevos archivos de modelos mientras ComfyUI está ejecutándose, necesitas actualizar el navegador (Ctrl+R) para ver los nuevos archivos en la lista desplegable

## Entradas

| Nombre del Parámetro | Tipo de Datos | Método de Entrada | Valor Predeterminado | Rango de Valores | Descripción |
|----------------------|---------------|-------------------|----------------------|------------------|-------------|
| nombre_ckpt | STRING | Selección Desplegable | null | Todos los archivos de modelos en la carpeta checkpoints | Selecciona el nombre del archivo de checkpoint del modelo a cargar, que determina el modelo de IA utilizado para la generación posterior de imágenes |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|------------------|---------------|-------------|
| MODELO | MODEL | El modelo de difusión principal utilizado para la generación de imágenes por eliminación de ruido, el componente central de la creación de imágenes con IA |
| CLIP | CLIP | El modelo utilizado para codificar prompts de texto, convirtiendo descripciones de texto en información que la IA puede entender |
| VAE | VAE | El modelo utilizado para la codificación y decodificación de imágenes, responsable de convertir entre el espacio de píxeles y el espacio latente |
