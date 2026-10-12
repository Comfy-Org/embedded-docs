# Vidu2ReferenceVideoNode

Il nodo Vidu2 Reference-to-Video Generation crea un video da un prompt testuale e più immagini di riferimento. Puoi definire fino a sette soggetti, ciascuno con il proprio insieme di immagini di riferimento, e fare riferimento a essi nel prompt usando `@subject{subject_id}`. Il nodo genera un video con durata, proporzioni e movimento configurabili.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI da utilizzare per la generazione del video. | COMBO | Sì | `"viduq2"` |
| `subjects` | Per ogni soggetto, fornisci fino a 3 immagini di riferimento (7 immagini in totale tra tutti i soggetti). Fai riferimento a essi nei prompt tramite `@subject{subject_id}`. | AUTOGROW | Sì | N/A |
| `prompt` | La descrizione testuale usata per guidare la generazione del video. Quando il parametro `audio` è abilitato, il video includerà parlato generato e musica di sottofondo in base a questo prompt. | STRING | Sì | N/A |
| `audio` | Quando abilitato, il video conterrà parlato generato e musica di sottofondo in base al prompt (predefinito: `False`). | BOOLEAN | No | N/A |
| `duration` | La durata del video generato in secondi (predefinito: `5`). | INT | No | da 1 a 10 |
| `seed` | Un numero usato per controllare la casualità della generazione per risultati riproducibili (predefinito: `1`). | INT | No | da 0 a 2147483647 |
| `aspect_ratio` | La forma del fotogramma del video. | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `resolution` | La risoluzione in pixel del video di output (predefinito: `"720p"`). | COMBO | No | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | Controlla l'ampiezza del movimento degli oggetti nel fotogramma (predefinito: `"auto"`). | COMBO | No | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Vincoli:**

* Il `prompt` deve avere una lunghezza compresa tra 1 e 2000 caratteri.
* Puoi definire più soggetti, ma il numero totale di immagini di riferimento tra tutti i soggetti non deve superare 7.
* Ogni singolo soggetto può avere al massimo 3 immagini di riferimento.
* Ogni immagine di riferimento deve avere un rapporto larghezza-altezza compreso tra 1:4 e 4:1.
* Ogni immagine di riferimento deve essere di almeno 128 pixel sia in larghezza sia in altezza.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `da4b0a24e186f24cff8031c786bb765299b00bbfa13cc4161d53d3a68e466744`
