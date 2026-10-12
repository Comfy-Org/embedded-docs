# Flux3ImageToVideoNode

Flux 3 Image to Video anima da 1 a 10 immagini con FLUX 3. Ogni immagine diventa un fotogramma della clip: un'immagine la apre, due eseguono un morphing dalla prima alla seconda, mentre un numero maggiore di immagini viene distribuito lungo la clip o fissato ai tempi scelti.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `placement` | "spread across the clip" consente a FLUX 3 di posizionare le immagini (una apre la clip, due ne diventano l'inizio e la fine); "at times" fissa ogni immagine a un secondo scelto da te. | DYNAMIC_COMBO | Sì | `"spread across the clip"` (predefinito)<br>`"at times"` |
| `prompt` | Come la scena deve muoversi e suonare; il prompt viene interpretato ed espanso prima della generazione. Deve contenere almeno un carattere. | STRING | Sì | Testo multiriga (predefinito: vuoto) |
| `aspect_ratio` | Rapporto d'aspetto dell'output. "auto" ne sceglie uno dal prompt e dagli input. | COMBO | Sì | `"auto"` (predefinito)<br>altri rapporti d'aspetto disponibili |
| `duration` | Durata della clip in secondi. "auto" adatta la durata al contenuto. | COMBO | Sì | `"auto"` (predefinito)<br>altre durate disponibili |
| `resolution` | Risoluzione dell'output. | COMBO | Sì | `"720p"` (predefinito)<br>`"1080p"` |
| `generate_audio` | Genera audio sincronizzato (ambiente, parlato, effetti). Disattivato produce un video senza traccia audio. | BOOLEAN | Sì | true / false (predefinito: true) |
| `safety_tolerance` | Tolleranza di moderazione; 0 è il valore più restrittivo. Le richieste che inviano immagini o video sono limitate a 2 indipendentemente dal valore impostato qui. | INT | Sì | 0 a 4 (predefinito: 2, impostazione avanzata) |
| `seed` | Seme per determinare se il nodo deve essere rieseguito; FLUX 3 sceglie il proprio seme, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. | INT | Sì | 0 a 4294967295 (predefinito: 42, controllo dopo la generazione) |

### Input di spread across the clip

Questa opzione di posizionamento non ha parametri aggiuntivi.

### Input di at times

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `times` | Un tempo in secondi per immagine, separato da virgole e crescente, ad es. "0, 2.5, 5". Compare solo quando `placement` è "at times"; è richiesto un tempo per ogni immagine chiave. | STRING | No | Secondi separati da virgole (predefinito: "0") |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `keyframes` | Slot espandibile: collega da 1 a 10 immagini chiave nell'ordine di riproduzione, ad es. `image_1`, `image_2`, e così via. Ogni immagine diventa un fotogramma della clip. Minimo 256x256 pixel ciascuna; il rapporto d'aspetto non può essere più estremo di 64:1. | IMAGE | Sì | 1 a 10 immagini |

Nota: `keyframes` deve contenere almeno un'immagine; il nodo genera un errore se non ne viene collegata nessuna. Ogni immagine chiave deve essere di almeno 256x256 pixel e il suo rapporto d'aspetto non può essere più estremo di 64:1.

Quando `placement` è "spread across the clip" e sono collegate 3 o più immagini chiave, `duration` deve essere impostato su un valore esplicito, non "auto"; altrimenti il nodo genera un errore.

Quando `placement` è "at times", `times` deve fornire un tempo in secondi per ogni immagine. I tempi devono aumentare, non possono essere negativi e l'ultimo tempo non può andare oltre la fine della clip (fino a 20 secondi quando `duration` è "auto").

Poiché questo nodo invia immagini, `safety_tolerance` è limitato a 2 indipendentemente dal valore impostato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | La clip video generata, costruita dalle immagini chiave con il rapporto d'aspetto, la durata, la risoluzione e l'impostazione audio scelti. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`
