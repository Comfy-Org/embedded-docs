# Crear archivo 3D (desde Splat)

SplatToFile3D convierte un gaussian splat en un objeto File3D que se puede utilizar con los nodos Save o Preview 3D. Puedes elegir el formato de archivo de salida. El nodo solo admite un elemento por lote; si recibe más de un elemento, utiliza el primero y registra una advertencia.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `splat` | Los datos de gaussian splat que se serializarán en un archivo. Solo se admite un elemento por lote. Si se proporciona más de un elemento, solo se utiliza el primero. | SPLAT | Sí | - |
| `format` | El formato de archivo de salida para el archivo 3D. ply: Gaussian Splat 3D estándar con armónicos esféricos completos. ksplat: SplatBuffer de mkkellogg (nivel 0, sin comprimir), solo color base. spz: comprimido con gzip de Niantic (~10 veces más pequeño), solo color base (predeterminado: "ply") | COMBO | Sí | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `model_3d` | Un objeto File3D que contiene los datos de gaussian splat serializados en el formato seleccionado, listo para guardar o previsualizar. | FILE3D |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/es.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
