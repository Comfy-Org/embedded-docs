# Flux Prueba virtual de ropa

Este nodo realiza una prueba virtual de vestimenta al vestir a una persona con una prenda proporcionada. Utiliza la API BFL Flux VTO para generar una imagen realista de la persona usando la prenda especificada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `persona` | Imagen de la persona a vestir. | IMAGE | Sí | - |
| `prenda` | Imagen de la prenda a aplicar. | IMAGE | Sí | - |
| `instrucción` | Instrucción opcional de estilo en lenguaje natural (p. ej., cómo debe ajustarse la prenda). | STRING | No | - |
| `semilla` | La semilla aleatoria utilizada para crear el ruido. | INT | No | 0 a 18446744073709551615 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `image` | La imagen resultante que muestra a la persona usando la prenda proporcionada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/es.md)

---
**Source fingerprint (SHA-256):** `137c4cf91a539605ade93a428567619fea9e6a71459dd92354878fa2f2ea4afa`
