# Flotante

El nodo `PrimitiveFloat` crea un valor numérico de punto flotante que se puede utilizar en su flujo de trabajo. Toma una única entrada numérica y genera ese mismo valor, lo que le permite definir y pasar valores flotantes entre diferentes nodos en su pipeline de ComfyUI.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `valor` | El valor numérico de punto flotante a generar (predeterminado: 0.0) | FLOAT | Sí | -sys.maxsize a sys.maxsize (paso: 0.1) |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El valor numérico de punto flotante de entrada | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/es.md)

---
**Source fingerprint (SHA-256):** `a12473ac0efac903249f249770bec92a562b1ef6dede45fc0296e0e397a0754f`
