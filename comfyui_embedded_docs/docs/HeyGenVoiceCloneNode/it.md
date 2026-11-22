# HeyGen Voice 1.0 Instant Clone

Clona una voce da una registrazione di un singolo parlante con il motore Voice 1.0 di HeyGen. Il nodo carica la registrazione, crea un clone vocale istantaneo, attende che HeyGen completi l'elaborazione e restituisce `voice_id`. Collegalo a HeyGen Voice 1.0 Text to Speech oppure a `custom_voice_id` in HeyGen Avatar Video e HeyGen Talking Photo. La creazione del clone è gratuita; ti viene addebitato il parlato generato con la voce.

**Nota:** Questo nodo è contrassegnato come deprecato nel codice sorgente. Usa HeyGen Voice 1.0 Instant Clone Text to Speech per clonare una voce e pronunciare testo in un unico nodo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | Registrazione di un singolo parlante. Usa almeno 10 secondi di parlato chiaro; vengono utilizzati solo i primi 3 minuti. | AUDIO | Sì | N/A |
| `language` | Lingua parlata nella registrazione (predefinito: "auto"). | COMBO | Sì | `"auto"`<br>Numerosi preset di lingua |
| `similarity` | Quanto fedelmente la voce segue la registrazione (predefinito: "max"). | COMBO | Sì | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Rimuove il rumore di fondo dalla registrazione prima della clonazione (predefinito: True). | BOOLEAN | Sì | True<br>False |
| `seed` | Modifica il seed per clonare nuovamente la registrazione; ogni clone è una voce leggermente diversa (predefinito: 42). | INT | Sì | da 0 a 2147483647 |

**Nota:** La voce viene creata come "ComfyUI Voice" nel tuo account HeyGen e il nodo stampa `voice_id` nell'interfaccia utente, così puoi copiarlo per riutilizzarlo. Lascia `language` su "auto" a meno che il parlante non parli una lingua facilmente confondibile con una lingua strettamente correlata. L'input `seed` include un controllo fisso Control After Generate nell'interfaccia utente, quindi modificalo manualmente quando vuoi un altro clone.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `voice_id` | L'ID della voce clonata, da riutilizzare nel nodo HeyGen Voice 1.0 Text to Speech o come `custom_voice_id`. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/it.md)

---
**Source fingerprint (SHA-256):** `a44924942311ca520e8d77d89119cb56c1b8030124ce608ae89efd72a0e2ad28`
