# OperaciónAfiladoLatente

El nodo LatentOperationSharpen crea una operación de nitidez para representaciones latentes utilizando un kernel gaussiano. Normaliza los datos latentes, aplica un kernel de nitidez personalizado mediante convolución y luego restaura la luminancia original. Esto realza los detalles y bordes en la representación del espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `radio_afilado` | El radio del kernel de nitidez, que controla el tamaño del área utilizada para el afilado (valor predeterminado: 9) | INT | Sí | 1-31 |
| `sigma` | La desviación estándar del kernel gaussiano utilizado para construir el kernel de nitidez (valor predeterminado: 1.0) | FLOAT | Sí | 0.1-10.0 |
| `alfa` | El factor de intensidad de nitidez; valores más altos producen un efecto de nitidez más fuerte (valor predeterminado: 0.1) | FLOAT | Sí | 0.0-5.0 |

Los tres parámetros son parámetros avanzados y tienen valores predeterminados, por lo que el nodo se puede utilizar sin cambiarlos. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `operation` | Devuelve una operación de nitidez que se puede aplicar a datos latentes | LATENT_OPERATION |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/es.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
