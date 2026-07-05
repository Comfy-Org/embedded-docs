# LTXVAddGuide

El nodo LTXVAddGuide agrega guía de condicionamiento de video a secuencias latentes mediante la codificación de imágenes o videos de entrada y su incorporación como fotogramas clave en los datos de condicionamiento. Procesa la entrada a través de un codificador VAE y coloca estratégicamente los latentes resultantes en posiciones de fotograma especificadas, actualizando tanto el condicionamiento positivo como el negativo con información de fotogramas clave. El nodo maneja restricciones de alineación de fotogramas y permite controlar la intensidad de la influencia del condicionamiento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo que se modificará con guía de fotogramas clave | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo que se modificará con guía de fotogramas clave | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar los fotogramas de imagen/video de entrada | VAE | Sí | - |
| `latente` | Secuencia latente de entrada que recibirá los fotogramas de condicionamiento | LATENT | Sí | - |
| `imagen` | Imagen o video para condicionar el video latente. Debe tener 8*n + 1 fotogramas. Si el video no tiene 8*n + 1 fotogramas, se recortará al número de fotogramas válido más cercano. | IMAGE | Sí | - |
| `indice_fotograma` | Índice de fotograma para iniciar el condicionamiento. Para imágenes de un solo fotograma o videos de 1 a 8 fotogramas, cualquier valor de `indice_fotograma` es aceptable. Para videos de 9 o más fotogramas, `indice_fotograma` debe ser divisible por 8; de lo contrario, se redondeará hacia abajo al múltiplo de 8 más cercano. Los valores negativos se cuentan desde el final del video. (predeterminado: 0) | INT | No | -9999 a 9999 |
| `fuerza` | Intensidad de la influencia del condicionamiento, donde 1.0 aplica condicionamiento completo y 0.0 no aplica condicionamiento (predeterminado: 1.0) | FLOAT | No | 0.0 a 1.0 |

**Nota:** La imagen/video de entrada debe tener un número de fotogramas que siga el patrón 8*n + 1 (por ejemplo, 1, 9, 17, 25 fotogramas). Si la entrada supera este patrón, se recortará automáticamente al número de fotogramas válido más cercano.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Condicionamiento positivo actualizado con información de guía de fotogramas clave | CONDITIONING |
| `latente` | Condicionamiento negativo actualizado con información de guía de fotogramas clave | CONDITIONING |
| `latente` | Secuencia latente con fotogramas de condicionamiento incorporados y máscara de ruido actualizada | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/es.md)

---
**Source fingerprint (SHA-256):** `e7f4e6ed25cddd4b50b98341c63fc9915afc4956317ac7a5a9121fdc53c03a2d`
