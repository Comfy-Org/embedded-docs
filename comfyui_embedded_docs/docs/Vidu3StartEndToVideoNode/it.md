# Vidu3StartEndToVideoNode

Questo nodo genera un video creando una transizione tra un fotogramma iniziale e un fotogramma finale, guidata da un prompt testuale. Utilizza il modello Vidu Q3 per interpolare tra le due immagini e produce un video con la durata e la risoluzione scelte.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare per la generazione del video. Selezionando un'opzione vengono mostrati parametri di configurazione aggiuntivi per `resolution`, `duration` e `audio`. | DYNAMIC_COMBO | Sì | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `first_frame` | L'immagine iniziale della sequenza video. | IMAGE | Sì | - |
| `end_frame` | L'immagine finale della sequenza video. | IMAGE | Sì | - |
| `prompt` | Descrizione del prompt (max 2000 caratteri). | STRING | Sì | Fino a 2000 caratteri |
| `seed` | Valore seed usato per controllare la casualità della generazione. Ha un'opzione di controllo dopo la generazione (predefinito: 1). | INT | Sì | da 0 a 2147483647 |

### Input di viduq3-pro e viduq3-turbo

I seguenti parametri sono condivisi da entrambe le opzioni del modello (`viduq3-pro` e `viduq3-turbo`). Vengono mostrati dopo aver selezionato un modello.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `resolution` | Risoluzione del video in output. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `duration` | Durata del video in output in secondi (predefinito: 5). | INT | Sì | da 1 a 16 |
| `audio` | Se abilitato, produce un video con audio (inclusi dialoghi ed effetti sonori) (predefinito: False). | BOOLEAN | Sì | `True`<br>`False` |

**Nota:** Le immagini `first_frame` e `end_frame` devono avere rapporti d'aspetto simili. Il rapporto d'aspetto delle due immagini deve rimanere compreso tra l'80% e il 125% l'uno rispetto all'altro (vicinanza relativa tra 0,8 e 1,25).

**Nota:** Per `viduq3-turbo`, il prezzo è 0,06 USD al secondo a 720p e 0,08 USD al secondo a 1080p. Per `viduq3-pro`, il prezzo è 0,15 USD al secondo a 720p e 0,16 USD al secondo a 1080p.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
