# Breeze Voice Clone

Crea una voce Breeze da una registrazione di un singolo parlante. La voce viene salvata nel tuo account e restituita come handle della voce, insieme a un'anteprima audio di come suona.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | Registrazione di un singolo parlante, della durata di almeno 3 secondi. Vengono utilizzati solo i primi 60 secondi. | AUDIO | Sì | - |
| `remove_background_noise` | Pulisce la registrazione prima della clonazione. Predefinito: false. | BOOLEAN | No | true<br>false |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `voice` | La nuova voce Breeze, per Breeze Text to Speech. | BREEZE_VOICE |
| `preview` | Anteprima audio della voce clonata. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/it.md)

---
**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`
