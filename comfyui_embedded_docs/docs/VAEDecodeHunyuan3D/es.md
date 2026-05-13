> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/es.md)

El nodo VAEDecodeHunyuan3D convierte representaciones latentes en datos de vóxeles 3D mediante un decodificador VAE. Procesa las muestras latentes a través del modelo VAE con configuraciones ajustables de fragmentación y resolución para generar datos volumétricos adecuados para aplicaciones 3D.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `muestras` | LATENT | Sí | - | La representación latente que se decodificará en datos de vóxeles 3D |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para decodificar las muestras latentes |
| `num_chunks` | INT | Sí | 1000-500000 | Número de fragmentos en los que dividir el procesamiento para la gestión de memoria (predeterminado: 8000) |
| `resolución_octree` | INT | Sí | 16-512 | Resolución de la estructura de octree utilizada para la generación de vóxeles 3D (predeterminado: 256) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `voxels` | VOXEL | Los datos de vóxeles 3D generados a partir de la representación latente decodificada |

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
