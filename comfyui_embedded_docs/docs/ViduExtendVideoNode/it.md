# ViduExtendVideoNode

Il nodo Vidu Video Extension genera frame aggiuntivi per estendere la durata di un video esistente. Utilizza un modello AI specificato per creare una continuazione basata sul video di origine e su un prompt testuale opzionale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare per l'estensione video. Selezionando un modello vengono mostrate le relative impostazioni specifiche di durata e risoluzione. | DYNAMIC_COMBO | Sì | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `video` | Il video di origine da estendere. | VIDEO | Sì | - |
| `prompt` | Un prompt testuale opzionale per il video esteso (massimo 2000 caratteri; predefinito: vuoto). | STRING | Sì | - |
| `seed` | Un valore di seed per controllare la casualità della generazione (predefinito: 1). | INT | Sì | 0 to 2147483647 |
| `end_frame` | Un'immagine opzionale da utilizzare come frame finale di destinazione per l'estensione. | IMAGE | No | - |

### Input di viduq2-pro e viduq2-turbo

Queste impostazioni sono condivise da entrambi i modelli.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `duration` | Durata del video esteso in secondi (predefinito: 4). Questa impostazione compare dopo aver selezionato un modello. | INT | Sì | 1 to 7 |
| `resolution` | Risoluzione del video in output. Questa impostazione compare dopo aver selezionato un modello. | COMBO | Sì | `"720p"`<br>`"1080p"` |

**Nota:** Il `video` di origine deve avere una durata compresa tra 4 e 55 secondi. Se viene fornito `end_frame`, il suo rapporto d'aspetto deve essere compreso tra 1:4 e 4:1, e la sua larghezza e altezza devono essere ciascuna di almeno 128 pixel.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video appena generato contenente il filmato esteso. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
