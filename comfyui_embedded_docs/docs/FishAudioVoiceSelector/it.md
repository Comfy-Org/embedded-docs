# Selettore voce Fish Audio

Il nodo Fish Audio Voice Selector seleziona una voce dalla libreria Fish Audio per la generazione di sintesi vocale. Puoi scegliere una delle voci preimpostate integrate, oppure selezionare `custom` per inserire qualsiasi ID di modello vocale da fish.audio.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `voice` | Scegli una voce, oppure `custom` per inserire qualsiasi ID di modello vocale fish.audio. | DYNAMIC_COMBO | Sì | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Le opzioni di voce preimpostate coprono voci inglesi (en), cinesi (zh) e giapponesi (ja) e non richiedono input aggiuntivi.

### Input personalizzati

Questi input compaiono quando `voice` è impostato su `custom`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | ID del modello vocale da fish.audio, ad es. l'ID in https://fish.audio/m/<id>/. Predefinito: stringa vuota. | STRING | Sì | Qualsiasi ID valido di un modello vocale Fish Audio |

Nota: quando `voice` è impostato su `custom`, `voice_id` non deve essere vuoto dopo la rimozione degli spazi bianchi; in caso contrario il nodo genera un errore "Custom voice ID is empty.". Se viene passata un'opzione vocale non riconosciuta, il nodo genera un errore "Unknown voice".

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `voice` | L'ID del modello vocale Fish Audio selezionato. Per una voce preimpostata, viene restituito il corrispondente ID voce dalla libreria Fish Audio; per `custom`, viene restituito il valore `voice_id` inserito. | FISHAUDIO_VOICE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/it.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
