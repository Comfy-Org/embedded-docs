# LtxApi25AudioToVideo

Questo nodo genera un video che segue una traccia audio utilizzando il modello LTX 2.5. L'audio determina la durata del video (tra 2 e 20 secondi) e, facoltativamente, puoi fornire un'immagine da usare come primo fotogramma. Il video viene generato tramite il servizio API LTX 2.5.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | Traccia audio che guida il video. La sua durata (2-20 secondi) imposta la durata del video. | AUDIO | Sì | 2-20 secondi |
| `model` | La versione del modello LTX 2.5 da usare. Selezionando un modello viene anche mostrata la sotto-opzione `resolution` per quel modello. | COMBO | Sì | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `resolution` | La risoluzione di output del video generato. Questa sotto-opzione è mostrata sotto il `model` selezionato (predefinito: "1920x1080"). Entrambi i modelli offrono le stesse opzioni di risoluzione. | COMBO | Sì | "1920x1080"<br>"1080x1920" |
| `prompt` | Una descrizione testuale che guida il contenuto del video generato (predefinito: ""). Deve contenere almeno 1 carattere e al massimo 10000 caratteri. | STRING | Sì | 1-10000 caratteri |
| `seed` | Un numero che controlla la casualità della generazione. Lo stesso seed produce lo stesso risultato (predefinito: 42). | INT | Sì | Qualsiasi numero intero |
| `image` | Primo fotogramma opzionale da usare per il video. È supportata una sola immagine. | IMAGE | No | Immagine singola |

Note sui vincoli:
- La durata dell'audio deve essere compresa tra 2 e 20 secondi; il nodo genera un errore se è al di fuori di questo intervallo.
- Il prompt è obbligatorio e non può essere vuoto; deve essere compreso tra 1 e 10000 caratteri.
- Quando viene fornito `image`, è accettata una sola immagine di input.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video generato guidato dalla traccia audio fornita. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/it.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
