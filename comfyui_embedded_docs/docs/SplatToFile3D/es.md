# Crear archivo 3D (desde Splat)

## Descripción General

El nodo SplatToFile3D convierte un splat gaussiano en un objeto File3D que puede utilizarse con los nodos Guardar o Vista Previa 3D. Solo admite un elemento por lote y permite elegir entre diferentes formatos de archivo de salida para los datos 3D exportados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `splat` | Los datos del splat gaussiano que se serializarán en un archivo | SPLAT | Sí | - |
| `formato` | El formato de archivo de salida para el archivo 3D. ply: Splat Gaussiano 3D estándar con armónicos esféricos completos. ksplat: SplatBuffer de mkkellogg (nivel 0, sin comprimir), solo color base. spz: Comprimido con gzip de Niantic (~10x más pequeño), solo color base (predeterminado: "ply") | COMBO | Sí | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `modelo_3d` | Un objeto File3D que contiene los datos del splat gaussiano serializados en el formato seleccionado, listo para guardar o previsualizar | FILE3D |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/es.md)

---
**Source fingerprint (SHA-256):** `c04fe04faa8ce81ad699e67c00d047550b0cadbfd037b687331f76944501a9f6`
