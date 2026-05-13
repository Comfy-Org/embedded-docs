> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/es.md)

El nodo ImageRotate rota una imagen de entrada según ángulos especificados. Admite cuatro opciones de rotación: sin rotación, 90 grados en sentido horario, 180 grados y 270 grados en sentido horario. La rotación se realiza mediante operaciones eficientes con tensores que mantienen la integridad de los datos de la imagen.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a rotar |
| `rotación` | STRING | Sí | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" | El ángulo de rotación que se aplicará a la imagen (predeterminado: "none") |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `imagen` | IMAGE | La imagen de salida rotada |

---
**Source fingerprint (SHA-256):** `068946b31ebe87b2524a1e628b5bc0a3da7367d7252fa7afafe96bcbb174747d`
