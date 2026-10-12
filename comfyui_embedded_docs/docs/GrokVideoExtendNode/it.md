# GrokVideoExtendNode

Il nodo Grok Video Extend estende un video esistente con una continuazione fluida basata su un prompt testuale. Fornisci un breve video sorgente e descrivi cosa dovrebbe accadere successivamente; il nodo restituisce una nuova clip video che continua dall'originale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello da utilizzare per l'estensione video. Selezionando l'opzione `"grok-imagine-video"` vengono visualizzate le impostazioni specifiche del modello. | DYNAMIC_COMBO | Sì | `"grok-imagine-video"` |
| `prompt` | Descrizione testuale di ciò che dovrebbe accadere successivamente nel video. | STRING | Sì | N/A |
| `video` | Video sorgente da estendere. Formato MP4, 2-15 secondi. | VIDEO | Sì | MP4, 2-15 secondi, massimo 50MB |
| `seed` | Seme per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seme (predefinito: 0). | INT | Sì | da 0 a 2147483647 |

### Input di grok-imagine-video

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `duration` | Durata dell'estensione in secondi (predefinito: 8). | INT | Sì | da 2 a 10 |

**Vincoli sui parametri:**
*   L'input `video` deve essere un file MP4 di durata compresa tra 2 e 15 secondi e non può superare i 50MB di dimensione.
*   Il `prompt` deve contenere almeno un carattere dopo la rimozione degli spazi bianchi.
*   Il parametro `model` è una combo dinamica. Selezionando l'opzione `"grok-imagine-video"` viene visualizzato il parametro annidato `duration`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | L'estensione video appena generata. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/it.md)

---
**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`
