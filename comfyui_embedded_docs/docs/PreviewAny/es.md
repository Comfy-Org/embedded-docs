# Vista previa de cualquier

El nodo PreviewAny acepta cualquier valor de entrada y lo muestra como texto legible en la interfaz. Está diseñado para inspeccionar y depurar valores en cualquier punto de un flujo de trabajo: las cadenas se muestran tal cual, los números y booleanos se convierten a texto, y otros objetos se formatean como JSON. El texto convertido también se pasa como salida de cadena para que pueda ser utilizado por otros nodos.

## Entradas

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
|-----------|-------------|-----------|----------|-------|
| `source` | El valor a previsualizar como texto. Acepta cualquier tipo de datos. Las cadenas se pasan sin cambios; los números y booleanos se convierten a texto; otros valores se serializan a JSON con indentación. Si la serialización JSON falla, se usa la representación de cadena simple del valor, y si eso también falla, se muestra el texto "source exists, but could not be serialized." | ANY | Sí | Cualquier tipo de datos |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `UI Text Display` | Muestra los datos de entrada convertidos a texto en la interfaz de usuario. El mismo texto también se devuelve como salida de cadena para su posterior procesamiento por otros nodos. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/es.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
