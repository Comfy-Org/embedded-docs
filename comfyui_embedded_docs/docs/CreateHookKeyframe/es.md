> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/es.md)

El nodo Crear Fotograma Clave de Hook permite definir puntos específicos en un proceso de generación donde cambia el comportamiento del hook. Crea fotogramas clave que modifican la intensidad de los hooks en porcentajes particulares del progreso de generación, y estos fotogramas clave pueden encadenarse para crear patrones de programación complejos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `multiplicador_fuerza` | FLOAT | Sí | -20.0 a 20.0 | Multiplicador de la intensidad del hook en este fotograma clave (predeterminado: 1.0) |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 a 1.0 | El punto porcentual en el proceso de generación donde este fotograma clave surte efecto (predeterminado: 0.0) |
| `prev_hook_kf` | HOOK_KEYFRAMES | No | - | Grupo opcional de fotogramas clave de hook anterior al que agregar este fotograma clave |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Un grupo de fotogramas clave de hook que incluye el fotograma clave recién creado |

---
**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`
