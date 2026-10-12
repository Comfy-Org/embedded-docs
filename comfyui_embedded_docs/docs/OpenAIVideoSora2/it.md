# OpenAIVideoSora2

Il nodo OpenAIVideoSora2 genera video con i modelli Sora di OpenAI. Accetta un prompt testuale insieme a un'immagine di riferimento singola opzionale, invia la richiesta a OpenAI, attende il completamento della generazione e restituisce il video risultante. Le durate e le risoluzioni supportate dipendono dal modello selezionato.

**AVVISO DI DEPRECAZIONE:** OpenAI smetterà di fornire l'API Sora v2 a settembre 2026. Questo nodo verrà rimosso da ComfyUI in tale data.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello OpenAI Sora da utilizzare per la generazione video (predefinito: "sora-2") | COMBO | Sì | "sora-2"<br>"sora-2-pro" |
| `prompt` | Testo guida; può essere vuoto se è presente un'immagine di input (predefinito: stringa vuota) | STRING | Sì | - |
| `size` | La risoluzione del video generato (predefinito: "1280x720") | COMBO | Sì | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | La durata del video generato in secondi (predefinito: 8) | COMBO | Sì | 4<br>8<br>12 |
| `image` | Immagine di riferimento di input opzionale usata per la generazione video; è supportata una sola immagine | IMAGE | No | - |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seed (predefinito: 0) | INT | No | 0 to 2147483647 |

**Vincoli e limitazioni:**

- Il modello "sora-2" supporta solo le dimensioni "720x1280" e "1280x720"; selezionando "1024x1792" o "1792x1024" con "sora-2" viene generato un errore. Le dimensioni maggiori sono disponibili solo con "sora-2-pro".
- Quando un'immagine è collegata, deve contenere esattamente un'immagine; collegando più di un'immagine viene generato un errore.
- I risultati sono non deterministici indipendentemente dal valore del seed.
- La stima del prezzo visualizzata dipende dal `model`, `size` e `duration` selezionati.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il video generato da OpenAI Sora | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/it.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
