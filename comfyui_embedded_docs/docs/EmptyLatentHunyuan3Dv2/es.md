> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/es.md)

El nodo `EmptyLatentHunyuan3Dv2` crea tensores latentes vacíos formateados específicamente para modelos de generación 3D Hunyuan3Dv2. Genera espacios latentes vacíos con las dimensiones y estructura correctas requeridas por la arquitectura Hunyuan3Dv2, lo que permite iniciar flujos de trabajo de generación 3D desde cero. El nodo produce tensores latentes llenos de ceros que sirven como base para procesos posteriores de generación 3D.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `resolución` | INT | Sí | 1 - 8192 | La dimensión de resolución para el espacio latente (predeterminado: 3072) |
| `tamaño_del_lote` | INT | Sí | 1 - 4096 | El número de imágenes latentes en el lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `LATENT` | LATENT | Devuelve un tensor latente que contiene muestras vacías formateadas para generación 3D Hunyuan3Dv2 |

---
**Source fingerprint (SHA-256):** `f912b226bcec4e2edd52250682d0583ab378b5502173f8e027e0e8fbff1db08f`
