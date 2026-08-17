# VAEDecodeHunyuan3D

El nodo VAEDecodeHunyuan3D convierte representaciones latentes en datos de vóxeles 3D mediante un decodificador VAE. Procesa las muestras latentes a través del modelo VAE con ajustes configurables de fragmentación y resolución para generar datos volumétricos adecuados para aplicaciones 3D.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | La representación latente que se decodificará en datos de vóxeles 3D | LATENT | Sí | - |
| `vae` | El modelo VAE utilizado para decodificar las muestras latentes | VAE | Sí | - |
| `num_chunks` | El número de fragmentos en los que se divide el procesamiento para la gestión de memoria (predeterminado: 8000) | INT | Sí | 1000-500000 |
| `octree_resolution` | La resolución de la estructura de octree utilizada para la generación de vóxeles 3D (predeterminado: 256) | INT | Sí | 16-512 |

Nota: `num_chunks` y `octree_resolution` son parámetros avanzados.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `voxels` | Los datos de vóxeles 3D generados a partir de la representación latente decodificada | VOXEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/es.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
