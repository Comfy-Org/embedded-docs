# HeyGen Voice 1.0 Text to Speech

Riproduce il testo con una voce HeyGen. Il nodo invia il testo e l’ID voce a HeyGen e restituisce il parlato generato come audio. Sono disponibili due modelli: `heygen-voice-1` e il più veloce ed economico `heygen-voice-1-turbo`. Per parlare con una voce clonata da una registrazione, usa HeyGen Voice 1.0 Instant Clone Text to Speech.

Selezionando un `model` vengono mostrati i parametri specifici di quel modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `modello` | Modello da utilizzare. `heygen-voice-1-turbo` è più veloce ed economico. Selezionando un modello vengono mostrati i parametri specifici: `voice_id`, `text`, `language` e `expressiveness_boost`. | DYNAMIC_COMBO | Sì | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | ID di una voce HeyGen, ad esempio dalla libreria voci di HeyGen (predefinito: vuoto). | STRING | Sì | N/D |
| `text` | Testo da pronunciare. Fino a 5000 caratteri; il parlato più lungo di circa 12 minuti fallisce, quindi suddividi i testi molto lunghi in cinese o giapponese (predefinito: vuoto). | STRING | Sì | Da 1 a 5000 caratteri |
| `language` | Lingua del testo. Impostala per lingue strettamente correlate come serbo o malese, che il rilevamento automatico può confondere (predefinito: "auto"). | COMBO | Sì | `"auto"`<br>Diverse preimpostazioni linguistiche |
| `expressiveness_boost` | Valori più alti sono più espressivi; valori più bassi restano più vicini alla voce originale (predefinito: 0.5). | FLOAT | Sì | Da 0.0 a 1.0 (passo 0.05) |

**Nota:** `voice_id` non deve essere vuoto; il nodo si interrompe con un errore quando manca. `text` deve contenere almeno un carattere.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `AUDIO` | Il parlato generato dal testo, pronunciato con la voce selezionata. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/it.md)

---
**Source fingerprint (SHA-256):** `d5bc03344341f2562d4bdca3a8503928a0dbbf7bd2b85df073bd04ab20b4be98`
