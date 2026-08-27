# FishAudioVoiceSelector

El nodo Selector de Voz de Fish Audio selecciona una voz de la biblioteca de Fish Audio para la generación de texto a voz. Puede elegir una de las voces preestablecidas integradas o seleccionar "custom" para ingresar cualquier ID de modelo de voz de fish.audio.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `voice` | Elija una voz, o 'custom' para ingresar cualquier ID de modelo de voz de fish.audio. | DYNAMIC_COMBO | Sí | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Las opciones de voz preestablecidas incluyen voces en inglés (en), chino (zh) y japonés (ja) y no requieren entradas adicionales.

### Entradas personalizadas

Estas entradas aparecen cuando `voice` se establece en "custom".

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `voice_id` | ID de modelo de voz de fish.audio, p. ej., el ID en https://fish.audio/m/<id>/. Por defecto: cadena vacía. | STRING | Sí | Cualquier ID de modelo de voz válido de Fish Audio |

Nota: cuando `voice` se establece en "custom", `voice_id` no debe estar vacío después de recortar los espacios en blanco; de lo contrario, el nodo lanza un error "Custom voice ID is empty.". Si se pasa una opción de voz no reconocida, el nodo lanza un error "Unknown voice".

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `voice` | El ID del modelo de voz de Fish Audio seleccionado. Para una voz preestablecida, se devuelve el ID de voz correspondiente de la biblioteca de Fish Audio; para "custom", se devuelve el valor de `voice_id` ingresado. | FISHAUDIO_VOICE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/es.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
