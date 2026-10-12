# ByteDance da immagine a video

Il nodo ByteDance Image to Video genera video utilizzando i modelli ByteDance tramite un'API basata su un'immagine di input e un prompt testuale. Prende un fotogramma immagine iniziale e crea una sequenza video che segue la descrizione fornita. Il nodo offre varie opzioni di personalizzazione per risoluzione video, rapporto d'aspetto, durata e altri parametri di generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello ByteDance da utilizzare per la generazione video (predefinito: `"seedance-1-0-pro-fast-251015"`). | COMBO | Sì | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Il prompt testuale utilizzato per generare il video. Deve contenere almeno 1 carattere dopo aver rimosso gli spazi bianchi. | STRING | Sì | - |
| `image` | Primo fotogramma da utilizzare per il video. Deve essere compreso tra 300x300 e 6000x6000 pixel, con un rapporto d'aspetto compreso tra 0,4 e 2,5. | IMAGE | Sì | - |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Il rapporto d'aspetto del video di output. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | La durata del video di output in secondi (predefinito: 5). Per il modello `seedance-1-5-pro-251215`, la durata minima supportata è di 4 secondi. | INT | Sì | 3 - 12 |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). | INT | No | 0 - 2147483647 |
| `camera_fixed` | Specifica se fissare la fotocamera. La piattaforma aggiunge un'istruzione per fissare la fotocamera al prompt, ma non garantisce l'effetto effettivo (predefinito: False). | BOOLEAN | No | `False`<br>`True` |
| `watermark` | Indica se aggiungere una filigrana "AI generated" al video (predefinito: False). | BOOLEAN | No | `False`<br>`True` |
| `generate_audio` | Questo parametro viene ignorato per qualsiasi modello eccetto `seedance-1-5-pro-251215` (predefinito: False). | BOOLEAN | No | `False`<br>`True` |

**Nota:** Il prompt non deve contenere le seguenti parole (senza distinzione tra maiuscole e minuscole): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Questi parametri vengono impostati tramite i rispettivi input dedicati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato in base all'immagine di input e ai parametri del prompt. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`
