# EndLoop

End Loop marca el final de un bloque de bucle. Recopila el valor producido por el último nodo en el cuerpo del bucle y devuelve solo la iteración final o todas las iteraciones, según la configuración de `accumulate`, a la vez que también pasa un valor de vuelta a Start Loop para que pueda comenzar la siguiente iteración.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `output_value` | Valor devuelto por End Loop. Devuelve la iteración final o todas las iteraciones según `accumulate`. | ANY | No | Cualquier tipo de valor |
| `next_iteration_value` | Valor enviado desde End Loop de vuelta a Start Loop para la siguiente iteración. | ANY | No | Cualquier tipo de valor |
| `accumulate` | Devuelve `output_value` de cada iteración cuando está habilitado; de lo contrario, devuelve solo la iteración final. | BOOLEAN | No | `true`<br>`false` (predeterminado: `false`) |
| `terminations` | Conecta las salidas que deben ejecutarse en cada iteración. Sus valores no se devuelven. Ranuras ampliables denominadas `termination_1`, `termination_2`, etc. | ANY | No | 0 a 50 ranuras |

Nota: `terminations` es una lista ampliable de ranuras con un mínimo de 0 y un máximo de 50 conexiones. Los valores conectados aquí fuerzan la ejecución en cada iteración, pero no forman parte del resultado devuelto.

Nota: Este nodo es un nodo de lista de entradas, por lo que sus entradas reciben los valores recopilados de cada iteración del bucle.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `outputs` | El `output_value` de la iteración final, o los valores acumulados a lo largo de las iteraciones cuando `accumulate` está habilitado. | ANY (list) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/es.md)

---
**Source fingerprint (SHA-256):** `473ba61d8e6fecdd1205297e2c602e3fd821044aff87d15a3f4b7646748d9999`
