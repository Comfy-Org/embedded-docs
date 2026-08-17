# Decodificar TripoSplat

Decodifica una representación latente de TripoSplat en un splat de gaussianas 3D. Este nodo toma el latente muestreado de un modelo TripoSplat y lo reconstruye como un conjunto de gaussianas 3D, cuya densidad se puede ajustar modificando el número de gaussianas generadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `samples` | Las muestras latentes a decodificar | LATENT | Sí | - |
| `vae` | Decodificador VAE de TripoSplat | VAE | Sí | - |
| `num_gaussians` | Número de gaussianas a generar (redondeado a un múltiplo de 32). 262144 coincide con la densidad de puntos del octree; un valor mayor sobremuestrea los mismos puntos (más denso, pero sin nuevo detalle) y cuesta proporcionalmente más VRAM/tiempo. Valor predeterminado: 262144 | INT | Sí | 32 a 1048576 (paso: 32) |
| `seed` | Fija la semilla del muestreador de puntos del octree (RNG global) para decodificaciones deterministas. Valor predeterminado: 0 | INT | Sí | 0 a 18446744073709551615 |

**Nota:** El valor de `num_gaussians` se redondea automáticamente a un múltiplo de la configuración de gaussianas por punto del decodificador VAE. El número real utilizado puede diferir ligeramente del valor de entrada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `splat` | El splat de gaussianas 3D decodificado que contiene posiciones, escalas, rotaciones, opacidades y coeficientes de armónicos esféricos | SPLAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/es.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
