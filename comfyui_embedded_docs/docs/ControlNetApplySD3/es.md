> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/es.md)

Este nodo aplica guía ControlNet al acondicionamiento de Stable Diffusion 3. Toma entradas de acondicionamiento positivo y negativo junto con un modelo ControlNet y una imagen, luego aplica la guía de control con parámetros ajustables de fuerza y temporización para influir en el proceso de generación.

**Nota:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | El acondicionamiento positivo al que aplicar la guía ControlNet |
| `negative` | CONDITIONING | Sí | - | El acondicionamiento negativo al que aplicar la guía ControlNet |
| `control_net` | CONTROL_NET | Sí | - | El modelo ControlNet a utilizar para la guía |
| `vae` | VAE | Sí | - | El modelo VAE utilizado en el proceso |
| `image` | IMAGE | Sí | - | La imagen de entrada que ControlNet utilizará como guía |
| `strength` | FLOAT | Sí | 0.0 - 10.0 | La fuerza del efecto ControlNet (valor por defecto: 1.0) |
| `start_percent` | FLOAT | Sí | 0.0 - 1.0 | El punto de inicio en el proceso de generación donde ControlNet comienza a aplicarse (valor por defecto: 0.0) |
| `end_percent` | FLOAT | Sí | 0.0 - 1.0 | El punto final en el proceso de generación donde ControlNet deja de aplicarse (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El acondicionamiento positivo modificado con la guía ControlNet aplicada |
| `negative` | CONDITIONING | El acondicionamiento negativo modificado con la guía ControlNet aplicada |