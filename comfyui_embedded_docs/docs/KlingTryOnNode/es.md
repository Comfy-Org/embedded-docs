# Kling Virtual Try-On

Viste a una persona con una prenda de ropa usando el probador virtual de Kling. Conecta una foto de una persona y una foto de la prenda, y el nodo devuelve una nueva imagen de esa persona con la prenda puesta.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `person_image` | Foto de una persona, idealmente de frente o en vista de tres cuartos. Las imágenes con un lado de más de 2048 píxeles se reducen de escala primero. | IMAGE | Sí | N/A |
| `garment_image` | La prenda que se va a poner: foto de producto, flat lay, maniquí o foto con modelo. Una foto con modelo puede conservar el resto de ese conjunto. Solo ropa; no se admiten zapatos, bolsos ni accesorios. | IMAGE | Sí | N/A |
| `keep_pose` | Desactívalo para permitir que la pose cambie y ofrezca una mejor presentación del conjunto. Parámetro avanzado (predeterminado: True). | BOOLEAN | Sí | `True`<br>`False` |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Este parámetro tiene la funcionalidad de «control after generate» (predeterminado: 42). | INT | Sí | 0 a 2147483647 |

**Nota:** El resultado tiene el mismo tamaño que `person_image`, limitado a 2048 píxeles en el lado más largo. Ambas entradas se suben a la API de Kling, lo que puede tardar un momento.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La persona usando la prenda de ropa. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/es.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`
