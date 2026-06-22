# VAEDecodeHunyuan3D

El nodo VAEDecodeHunyuan3D convierte representaciones latentes en datos de vóxeles 3D mediante un decodificador VAE. Procesa las muestras latentes a través del modelo VAE con configuraciones ajustables de fragmentación y resolución para generar datos volumétricos adecuados para aplicaciones 3D.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | La representación latente que se decodificará en datos de vóxeles 3D | LATENT | Sí | - |
| `vae` | El modelo VAE utilizado para decodificar las muestras latentes | VAE | Sí | - |
| `num_chunks` | Número de fragmentos en los que dividir el procesamiento para la gestión de memoria (predeterminado: 8000) | INT | Sí | 1000-500000 |
| `resolución_octree` | Resolución de la estructura de octree utilizada para la generación de vóxeles 3D (predeterminado: 256) | INT | Sí | 16-512 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `voxels` | Los datos de vóxeles 3D generados a partir de la representación latente decodificada | VOXEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/es.md)

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
