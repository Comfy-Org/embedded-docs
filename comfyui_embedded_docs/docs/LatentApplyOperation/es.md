# LatentApplyOperation

El nodo **LatentApplyOperation** aplica una operación especificada a muestras latentes. Toma datos latentes y una operación como entradas, copia las muestras latentes de entrada, aplica la operación al tensor latente y devuelve los datos latentes modificados. Este nodo le permite transformar o manipular representaciones latentes en su flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | Las muestras latentes que serán procesadas por la operación. | LATENT | Sí | - |
| `operation` | La operación a aplicar a las muestras latentes. | LATENT_OPERATION | Sí | - |

**Nota:** Este nodo está marcado como experimental. La operación se aplica al tensor latente almacenado bajo la clave `samples` de la estructura latente. Las muestras latentes de entrada se copian antes de aplicar la operación, por lo que los datos latentes de entrada originales no se modifican.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Las muestras latentes modificadas después de aplicar la operación. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/es.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
