# HeyGen Voice 1.0 Instant Clone Text to Speech

Clona una voce da una registrazione di un singolo parlante e pronuncia del testo con essa tramite HeyGen Voice 1.0. Il nodo carica la registrazione, sintetizza il parlato e lo restituisce come audio, così un singolo nodo passa da un campione vocale a un parlato finito.

Selezionando un `model` vengono rivelati i parametri specifici: `audio`, `text`, `language`, `expressiveness_boost`, `recording_language`, `similarity`, `remove_background_noise` e `seed`.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da usare. `heygen-voice-1-turbo` è più veloce e costa meno (predefinito: `"heygen-voice-1"`). | DYNAMIC_COMBO | Sì | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `audio` | Registrazione di un singolo parlante da clonare. Usa almeno 10 secondi di parlato chiaro; vengono usati solo i primi 3 minuti. | AUDIO | Sì | - |
| `text` | Testo da pronunciare, fino a 5000 caratteri. Un parlato più lungo di circa 12 minuti non va a buon fine, quindi suddividi testi molto lunghi in cinese o giapponese (predefinito: vuoto). | STRING | Sì | 1 a 5000 caratteri |
| `language` | Lingua del testo. Impostala per lingue strettamente correlate come serbo o malese, che il rilevamento automatico può confondere (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>Più preset di lingua |
| `expressiveness_boost` | Valori più alti sono più espressivi; valori più bassi restano più vicini alla voce originale (predefinito: 0.5). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.05) |
| `recording_language` | Lingua parlata nella registrazione, che limita la clonazione a quella lingua (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>Più preset di lingua |
| `similarity` | Quanto fedelmente la voce segue la registrazione (predefinito: `"max"`). | COMBO | Sì | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Rimuove il rumore di fondo nella registrazione prima della clonazione (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |
| `seed` | Il seed controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 42). | INT | Sì | 0 a 2147483647 |

`text` deve contenere almeno un carattere e `audio` è obbligatorio: una registrazione con più parlanti, o una troppo rumorosa per essere clonata, produce una voce scadente. Imposta `recording_language` quando la lingua del campione non è ovvia.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `AUDIO` | Il testo pronunciato con la voce clonata. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneTextToSpeechNode/it.md)

---
**Source fingerprint (SHA-256):** `ea18e2abce687e106ed0b37eb7afd723fbe72a3b4d58124a143c00b66d2fe7c9`
