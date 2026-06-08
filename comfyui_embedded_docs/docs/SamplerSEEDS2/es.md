Este nodo proporciona un muestreador configurable para generar imágenes. Implementa el algoritmo SEEDS-2, que es un solucionador de ecuaciones diferenciales estocásticas (SDE). Al ajustar sus parámetros, puede configurarlo para que se comporte como varios muestreadores específicos, incluyendo `seeds_2`, `exp_heun_2_x0` y `exp_heun_2_x0_sde`.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `solver_type` | Selecciona el algoritmo solucionador subyacente para el muestreador. | COMBO | Sí | `"phi_1"`<br>`"phi_2"` |
| `eta` | Intensidad estocástica (predeterminado: 1.0). | FLOAT | No | 0.0 - 100.0 |
| `s_noise` | Multiplicador de ruido SDE (predeterminado: 1.0). | FLOAT | No | 0.0 - 100.0 |
| `r` | Tamaño de paso relativo para la etapa intermedia (nodo c2) (predeterminado: 0.5). | FLOAT | No | 0.01 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sampler` | Un objeto muestreador configurado que puede pasarse a otros nodos de muestreo. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/es.md)

---
**Source fingerprint (SHA-256):** `13cfc064dab8b77dbdfdc27238130bdf3dc6c1eca47110f4a7f7d6b8c2866b90`
