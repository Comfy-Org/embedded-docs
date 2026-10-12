# Vidu Q3 Generazione Testo-a-Video

Il nodo Vidu Q3 Text-to-Video Generation crea un video a partire da una descrizione testuale. Utilizza il modello Vidu Q3 Pro o Q3 Turbo per generare contenuti video in base al tuo prompt, consentendoti di controllare la durata, la risoluzione, il rapporto d'aspetto e se include l'audio.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare per la generazione video. Selezionando un modello vengono mostrati parametri di configurazione aggiuntivi per rapporto d'aspetto, risoluzione, durata e audio. | DYNAMIC_COMBO | Sì | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | Una descrizione testuale per la generazione video, con una lunghezza massima di 2000 caratteri. | STRING | Sì | N/A |
| `seed` | Un valore di seed per controllare la casualità della generazione (predefinito: 1). | INT | Sì | da 0 a 2147483647 |

### Input di viduq3-pro e viduq3-turbo

I seguenti parametri di configurazione sono condivisi dai modelli `viduq3-pro` e `viduq3-turbo`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Il rapporto d'aspetto del video di output. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `duration` | Durata del video di output in secondi (predefinito: 5). | INT | Sì | da 1 a 16 |
| `audio` | Quando abilitato, produce un video con audio (inclusi dialoghi ed effetti sonori) (predefinito: False). | BOOLEAN | Sì | True/False |

**Nota:** I parametri `aspect_ratio`, `resolution`, `duration` e `audio` sono obbligatori una volta selezionato un `model`, poiché fanno parte della sua configurazione. Il `prompt` non deve essere vuoto e non può superare i 2000 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
