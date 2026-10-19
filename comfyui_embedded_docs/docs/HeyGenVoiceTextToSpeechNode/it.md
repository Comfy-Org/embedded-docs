# HeyGen Voice 1.0 Text to Speech

Riproduce il testo con una voce clonata tramite HeyGen Voice 1.0 Instant Clone. Il nodo invia il testo e l'ID voce a HeyGen e restituisce il parlato generato come audio. Sono disponibili due modelli: `heygen-voice-1` e il più veloce `heygen-voice-1-turbo`, che costa la metà.

Selezionando un `model` vengono mostrati i parametri specifici di quel modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. `heygen-voice-1-turbo` è più veloce e costa la metà. Selezionando un modello vengono mostrati i parametri specifici: `voice_id`, `text`, `language` e `expressiveness_boost`. | DYNAMIC_COMBO | Sì | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | Voce da HeyGen Voice 1.0 Instant Clone (predefinito: vuoto). | STRING | Sì | N/D |
| `text` | Testo da pronunciare. Fino a 5000 caratteri; il parlato più lungo di circa 12 minuti fallisce, quindi suddividi i testi molto lunghi in cinese o giapponese (predefinito: vuoto). | STRING | Sì | Da 1 a 5000 caratteri |
| `language` | Lingua del testo. Impostala per lingue strettamente correlate come serbo o malese, che il rilevamento automatico può confondere (predefinito: "auto"). | COMBO | Sì | `"auto"`<br>Diverse preimpostazioni linguistiche |
| `expressiveness_boost` | Valori più alti sono più espressivi; valori più bassi restano più vicini alla voce originale (predefinito: 0.5). | FLOAT | Sì | Da 0.0 a 1.0 (passo 0.05) |

**Nota:** `voice_id` deve essere una voce creata tramite HeyGen Voice 1.0 Instant Clone; il nodo si interrompe con un errore quando è vuoto. `text` deve contenere almeno un carattere.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `AUDIO` | Il parlato generato dal testo, pronunciato con la voce clonata. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/it.md)

---
**Source fingerprint (SHA-256):** `61e345563db04a4dfc61e8862a328d5062aa2a77af57c2209ca4ca3862930be8`
