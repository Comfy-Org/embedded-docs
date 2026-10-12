# ByteDanceFirstLastFrameNode

Questo nodo genera un video utilizzando un prompt testuale insieme alle immagini del primo e dell'ultimo fotogramma. Prende la tua descrizione e i due fotogrammi chiave per creare una sequenza video completa che esegue la transizione tra essi. Il nodo fornisce varie opzioni per controllare la risoluzione, il rapporto d'aspetto, la durata e altri parametri di generazione del video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello utilizzato per la generazione video (predefinito: `"seedance-1-5-pro-251215"`). | COMBO | Sì | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `prompt` | Il prompt testuale utilizzato per generare il video. Non deve essere vuoto e non deve contenere parole chiave riservate per i parametri (`resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`). | STRING | Sì | - |
| `first_frame` | Primo fotogramma da utilizzare per il video. Deve essere compreso tra 300x300 e 6000x6000 pixel, con un rapporto d'aspetto compreso tra 0.4 e 2.5. | IMAGE | Sì | - |
| `last_frame` | Ultimo fotogramma da utilizzare per il video. Deve essere compreso tra 300x300 e 6000x6000 pixel, con un rapporto d'aspetto compreso tra 0.4 e 2.5. | IMAGE | Sì | - |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Il rapporto d'aspetto del video di output. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | La durata del video di output in secondi. Quando si utilizza `seedance-1-5-pro-251215`, la durata minima è 4 secondi. (predefinito: 5) | INT | Sì | 3 - 12 |
| `seed` | Seed da utilizzare per la generazione. (predefinito: 0) | INT | No | 0 - 2147483647 |
| `camera_fixed` | Specifica se fissare la camera. La piattaforma aggiunge un'istruzione per fissare la camera al tuo prompt, ma non garantisce l'effetto reale. (predefinito: False) | BOOLEAN | No | - |
| `watermark` | Indica se aggiungere una filigrana "AI generated" al video. (predefinito: False) | BOOLEAN | No | - |
| `generate_audio` | Questo parametro viene ignorato per qualsiasi modello eccetto `seedance-1-5-pro-251215`. (predefinito: False) | BOOLEAN | No | - |

**Nota:** Per il modello `seedance-1-5-pro-251215`, `duration` deve essere pari o superiore a 4 secondi. Sia `first_frame` che `last_frame` devono essere compresi tra 300x300 e 6000x6000 pixel e avere un rapporto d'aspetto compreso tra 0.4 e 2.5. Il `prompt` viene controllato e rifiutato se contiene parole chiave riservate per i parametri.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
