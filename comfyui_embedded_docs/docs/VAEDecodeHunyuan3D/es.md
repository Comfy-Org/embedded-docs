> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/es.md)

El nodo VAEDecodeHunyuan3D convierte representaciones latentes en datos de vóxeles 3D utilizando un decodificador VAE. Procesa las muestras latentes a través del modelo VAE con configuraciones de fragmentación y resolución ajustables para generar datos volumétricos adecuados para aplicaciones 3D.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sí | - | La representación latente que será decodificada en datos de vóxeles 3D |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para decodificar las muestras latentes |
| `num_chunks` | INT | Sí | 1000-500000 | El número de fragmentos en los que dividir el procesamiento para la gestión de memoria (por defecto: 8000) |
| `octree_resolution` | INT | Sí | 16-512 | La resolución de la estructura de octree utilizada para la generación de vóxeles 3D (por defecto: 256) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `voxels` | VOXEL | Los datos de vóxeles 3D generados a partir de la representación latente decodificada |