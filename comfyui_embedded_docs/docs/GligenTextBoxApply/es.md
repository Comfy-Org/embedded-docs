El nodo `GLIGENTextBoxApply` está diseñado para integrar la condicionamiento basada en texto en la entrada de un modelo generativo, específicamente aplicando parámetros de cuadro de texto y codificándolos utilizando un modelo CLIP. Este proceso enriquece la condicionamiento con información espacial y textual, facilitando una generación más precisa y consciente del contexto.

## Entradas

| Parameter            | Comfy dtype        | Description (Descripción) |
|----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Especifica la entrada de condicionamiento inicial a la que se agregarán los parámetros del cuadro de texto y la información de texto codificada. Juega un papel crucial en la determinación de la salida final al integrar nuevos datos de condicionamiento. |
| `clip`               | `CLIP`             | El modelo CLIP utilizado para codificar el texto proporcionado en un formato que puede ser utilizado por el modelo generativo. Es esencial para convertir la información textual en un formato de condicionamiento compatible. |
| `gligen_textbox_model` | `GLIGEN`         | Representa la configuración específica del modelo GLIGEN que se utilizará para generar el cuadro de texto. Es crucial para asegurar que el cuadro de texto se genere de acuerdo con las especificaciones deseadas. |
| `text`               | `STRING`           | El contenido de texto que se codificará e integrará en la condicionamiento. Proporciona la información semántica que guía al modelo generativo. |
| `width`              | `INT`              | El ancho del cuadro de texto en píxeles. Define la dimensión espacial del cuadro de texto dentro de la imagen generada. |
| `height`             | `INT`              | La altura del cuadro de texto en píxeles. Similar al ancho, define la dimensión espacial del cuadro de texto dentro de la imagen generada. |
| `x`                  | `INT`              | La coordenada x de la esquina superior izquierda del cuadro de texto dentro de la imagen generada. Especifica la posición horizontal del cuadro de texto. |
| `y`                  | `INT`              | La coordenada y de la esquina superior izquierda del cuadro de texto dentro de la imagen generada. Especifica la posición vertical del cuadro de texto. |

## Salidas

| Parameter            | Comfy dtype        | Description (Descripción) |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | La salida de condicionamiento enriquecida, que incluye los datos de condicionamiento originales junto con los nuevos parámetros del cuadro de texto y la información de texto codificada. Se utiliza para guiar al modelo generativo en la producción de salidas conscientes del contexto. |
