> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/es.md)

Este nodo proporciona un muestreador configurable para generar imágenes. Implementa el algoritmo SEEDS-2, que es un solucionador de ecuaciones diferenciales estocásticas (SDE). Al ajustar sus parámetros, puede configurarlo para que se comporte como varios muestreadores específicos, incluyendo `seeds_2`, `exp_heun_2_x0` y `exp_heun_2_x0_sde`.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `solver_type` | COMBO | Sí | `"phi_1"`<br>`"phi_2"` | Selecciona el algoritmo solucionador subyacente para el muestreador. |
| `eta` | FLOAT | No | 0.0 - 100.0 | Intensidad estocástica (predeterminado: 1.0). |
| `s_noise` | FLOAT | No | 0.0 - 100.0 | Multiplicador de ruido SDE (predeterminado: 1.0). |
| `r` | FLOAT | No | 0.01 - 1.0 | Tamaño de paso relativo para la etapa intermedia (nodo c2) (predeterminado: 0.5). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `sampler` | SAMPLER | Un objeto muestreador configurado que puede pasarse a otros nodos de muestreo. |

---
**Source fingerprint (SHA-256):** `13cfc064dab8b77dbdfdc27238130bdf3dc6c1eca47110f4a7f7d6b8c2866b90`
