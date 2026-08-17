# CargarLatente

El nodo `LoadLatent` carga representaciones latentes que se guardaron previamente como archivos `.latent` en el directorio de entrada. Lee los datos del tensor latente del archivo seleccionado y aplica los ajustes de escala necesarios antes de devolver los resultados para su uso en otros nodos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `latent` | Selecciona qué archivo `.latent` cargar entre los archivos disponibles en el directorio de entrada | COMBO | Sí | Todos los archivos `.latent` en el directorio de entrada |

Nota: Para archivos `.latent` que no contienen el marcador `latent_format_version_0`, el tensor latente cargado se multiplica por 1/0.18215 para que su escala coincida con el formato esperado por otros nodos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | Devuelve los datos de representación latente cargados desde el archivo seleccionado | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/es.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
