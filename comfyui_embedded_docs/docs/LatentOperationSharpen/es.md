> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/es.md)

El nodo LatentOperationSharpen aplica un efecto de nitidez a representaciones latentes utilizando un kernel gaussiano. Funciona normalizando los datos latentes, aplicando una convolución con un kernel de nitidez personalizado y luego restaurando la luminancia original. Esto realza los detalles y bordes en la representación del espacio latente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `radio_afilado` | INT | No | 1-31 | El radio del kernel de nitidez (predeterminado: 9) |
| `sigma` | FLOAT | No | 0.1-10.0 | La desviación estándar para el kernel gaussiano (predeterminado: 1.0) |
| `alfa` | FLOAT | No | 0.0-5.0 | El factor de intensidad de nitidez (predeterminado: 0.1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `operation` | LATENT_OPERATION | Devuelve una operación de nitidez que se puede aplicar a datos latentes |

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
