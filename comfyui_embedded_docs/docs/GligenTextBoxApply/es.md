> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/es.md)

El nodo `GLIGENTextBoxApply` está diseñado para integrar condicionamiento basado en texto en la entrada de un modelo generativo, específicamente aplicando parámetros de cuadro de texto y codificándolos mediante un modelo CLIP. Este proceso enriquece el condicionamiento con información espacial y textual, facilitando una generación más precisa y consciente del contexto.

## Entradas

| Parámetro            | Tipo Comfy         | Descripción |
|----------------------|--------------------|-------------|
| `acondicionamiento_a`     | `CONDITIONING`     | Especifica la entrada de condicionamiento inicial a la que se agregarán los parámetros del cuadro de texto y la información textual codificada. Desempeña un papel crucial en la determinación de la salida final al integrar nuevos datos de condicionamiento. |
| `clip`               | `CLIP`             | El modelo CLIP utilizado para codificar el texto proporcionado en un formato que pueda ser utilizado por el modelo generativo. Es esencial para convertir la información textual en un formato de condicionamiento compatible. |
| `modelo_caja_texto_gligen` | `GLIGEN`         | Representa la configuración específica del modelo GLIGEN que se utilizará para generar el cuadro de texto. Es crucial para garantizar que el cuadro de texto se genere según las especificaciones deseadas. |
| `texto`               | `STRING`           | El contenido de texto que se codificará e integrará en el condicionamiento. Proporciona la información semántica que guía al modelo generativo. |
| `ancho`              | `INT`              | El ancho del cuadro de texto en píxeles. Define la dimensión espacial del cuadro de texto dentro de la imagen generada. |
| `altura`             | `INT`              | La altura del cuadro de texto en píxeles. Al igual que el ancho, define la dimensión espacial del cuadro de texto dentro de la imagen generada. |
| `x`                  | `INT`              | La coordenada x de la esquina superior izquierda del cuadro de texto dentro de la imagen generada. Especifica la posición horizontal del cuadro de texto. |
| `y`                  | `INT`              | La coordenada y de la esquina superior izquierda del cuadro de texto dentro de la imagen generada. Especifica la posición vertical del cuadro de texto. |

## Salidas

| Parámetro            | Tipo Comfy         | Descripción |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | La salida de condicionamiento enriquecida, que incluye los datos de condicionamiento originales junto con los parámetros del cuadro de texto recién agregados y la información textual codificada. Se utiliza para guiar al modelo generativo en la producción de resultados conscientes del contexto. |