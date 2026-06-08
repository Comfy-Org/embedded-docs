El nodo LatentOperationSharpen aplica un efecto de nitidez a representaciones latentes utilizando un kernel gaussiano. Funciona normalizando los datos latentes, aplicando una convolución con un kernel de nitidez personalizado y luego restaurando la luminancia original. Esto realza los detalles y bordes en la representación del espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `radio_afilado` | El radio del kernel de nitidez (predeterminado: 9) | INT | No | 1-31 |
| `sigma` | La desviación estándar para el kernel gaussiano (predeterminado: 1.0) | FLOAT | No | 0.1-10.0 |
| `alfa` | El factor de intensidad de nitidez (predeterminado: 0.1) | FLOAT | No | 0.0-5.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `operation` | Devuelve una operación de nitidez que se puede aplicar a datos latentes | LATENT_OPERATION |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/es.md)

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
