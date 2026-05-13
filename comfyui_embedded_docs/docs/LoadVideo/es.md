> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/es.md)

# Nodo de Carga de Video

El nodo de Carga de Video carga archivos de video desde el directorio de entrada y los pone a disposición para su procesamiento en el flujo de trabajo. Lee archivos de video de la carpeta de entrada designada y los genera como datos de video que pueden conectarse a otros nodos de procesamiento de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `archivo` | STRING | Sí | Múltiples opciones disponibles | El archivo de video a cargar desde el directorio de entrada. La lista desplegable se completa dinámicamente con todos los archivos de video encontrados en la carpeta de entrada de ComfyUI. |

**Nota:** Las opciones disponibles para el parámetro `file` se completan dinámicamente a partir de los archivos de video presentes en el directorio de entrada. Solo se muestran los archivos de video con tipos de contenido compatibles. También puedes cargar un nuevo archivo de video directamente a través del selector de archivos del nodo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | Los datos de video cargados que pueden pasarse a otros nodos de procesamiento de video para su posterior manipulación o análisis. |

---
**Source fingerprint (SHA-256):** `e3d18eb43cba34734761b5b147d9fee91fe3ca99db21f9e19a130efc3349cecb`
