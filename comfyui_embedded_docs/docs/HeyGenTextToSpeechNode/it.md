# HeyGen Text to Speech

Sintetizza audio vocale dal testo utilizzando il motore TTS Starfish di HeyGen. Questo nodo include le voci più popolari di HeyGen in 17 lingue.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `text` | Testo da sintetizzare (fino a 5000 caratteri). Il parlato generato deve durare almeno 1 secondo. | STRING | Sì | da 1 a 5000 caratteri |
| `voice` | Voce da utilizzare (selezionata tra le voci compatibili con Starfish più popolari di HeyGen). | STRING | Sì | Sono disponibili più opzioni |
| `custom_voice_id` | ID voce HeyGen opzionale. Se impostato, sostituisce la voce selezionata sopra. La voce deve supportare il motore Starfish (predefinito: vuoto). | STRING | No | Qualsiasi ID voce HeyGen valido |
| `speed` | Moltiplicatore della velocità del parlato (predefinito: 1.0). | FLOAT | No | da 0.5 a 2.0 (passo: 0.05) |
| `ssml` | Tratta il testo come markup SSML (per pause, enfasi e controllo della pronuncia) (predefinito: False). | BOOLEAN | No | True / False |
| `seed` | Non inviato a HeyGen; modificalo per forzare una nuova esecuzione (predefinito: 42). | INT | No | da 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `AUDIO` | L'audio vocale sintetizzato generato dal testo di input. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTextToSpeechNode/it.md)

---
**Source fingerprint (SHA-256):** `82300626657db8ab16e96ae96b7dfe3291b77bf75efec35971dc772e5123cce7`
