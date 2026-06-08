# VAEDecodeTripoSplat

Decodifica una representación latente de TripoSplat en un splat gaussiano 3D. Este nodo toma el latente muestreado de un modelo TripoSplat y lo reconstruye como un conjunto de gaussianos 3D, cuya densidad puede ajustarse modificando la cantidad de gaussianos generados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `muestras` | Las muestras latentes a decodificar | LATENT | Sí | - |
| `vae` | Modelo decodificador VAE de TripoSplat | VAE | Sí | - |
| `número_de_gaussianos` | Número de gaussianos a generar (redondeado a un múltiplo de 32). 262144 coincide con la densidad de puntos del octree; valores más altos sobremuestrean los mismos puntos (más densos, pero sin nuevo detalle) y consumen proporcionalmente más VRAM/tiempo. Valor predeterminado: 262144 | INT | Sí | 32 a 1048576 (paso: 32) |
| `semilla` | Inicializa el muestreador de puntos del octree (RNG global) para decodificaciones deterministas. Valor predeterminado: 0 | INT | Sí | 0 a 18446744073709551615 |

**Nota:** El valor de `num_gaussians` se redondea automáticamente a un múltiplo de la configuración de gaussianos por punto del decodificador VAE. El número real utilizado puede diferir ligeramente del valor ingresado.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `splat` | El splat gaussiano 3D decodificado que contiene posiciones, escalas, rotaciones, opacidades y coeficientes de armónicos esféricos | SPLAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/es.md)

---
**Source fingerprint (SHA-256):** `60fff70ade38bc820eaea9db26b714daf84a111fb3563477f56f4e8ffa96ff5b`
