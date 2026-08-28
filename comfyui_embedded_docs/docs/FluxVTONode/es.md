# Flux Prueba virtual de ropa

Este nodo realiza un probador virtual vistiendo a una persona con una imagen de prenda proporcionada. Utiliza la API BFL Flux VTO para generar una imagen realista de la persona usando la prenda especificada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `persona` | Imagen de la persona a vestir. | IMAGE | Sí | - |
| `prenda` | Imagen de la prenda a aplicar. | IMAGE | Sí | - |
| `instrucción` | Instrucción opcional de estilo en lenguaje natural (p. ej., cómo debe ajustarse la prenda). (predeterminado: vacío) | STRING | No | - |
| `semilla` | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) | INT | No | 0 a 18446744073709551615 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `image` | La imagen resultante que muestra a la persona usando la prenda proporcionada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/es.md)

---
**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`
