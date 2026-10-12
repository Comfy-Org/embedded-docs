# ElevenLabsInstantVoiceClone

Il nodo ElevenLabs Instant Voice Clone crea un nuovo modello vocale unico analizzando da 1 a 8 registrazioni audio della voce di una persona. Invia questi campioni all'API ElevenLabs, che li elabora per generare un clone vocale utilizzabile per la sintesi text-to-speech.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio_*` | Registrazioni audio per la clonazione vocale. È necessario fornire da 1 a 8 file audio. | AUDIO | Sì | Da 1 a 8 file |
| `remove_background_noise` | Rimuovi il rumore di fondo dai campioni vocali utilizzando l'isolamento audio. (predefinito: False) | BOOLEAN | No | True / False |

**Nota:** È necessario fornire almeno un file audio e se ne possono fornire fino a otto. Il nodo creerà automaticamente degli slot di input per i file audio aggiunti.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `voice` | L'identificatore univoco per il modello vocale clonato appena creato. Questo output può essere collegato ad altri nodi ElevenLabs text-to-speech. | ELEVENLABS_VOICE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/it.md)

---
**Source fingerprint (SHA-256):** `5b109dfff8cdbc51d9e2684b9508b0998aaa014459b973acf29c204835a8db95`
