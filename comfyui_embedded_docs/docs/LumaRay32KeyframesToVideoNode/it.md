# Luma Ray 3.2 Keyframes to Video

Questo nodo genera un video che interpola attraverso una sequenza di immagini guida, ciascuna ancorata a una posizione specifica sulla timeline, utilizzando Luma Ray 3.2. Costruisci la sequenza di keyframe utilizzando i nodi Luma Ray 3.2 Keyframe, collegando almeno 2 keyframe per definire l'animazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione del video (predefinito: stringa vuota). | STRING | Sì | da 1 a 6000 caratteri |
| `resolution` | La risoluzione di output del video generato (predefinito: "720p"). | STRING | Sì | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | La durata del video generato (predefinito: "5s"). | STRING | Sì | `"5s"`<br>`"10s"` |
| `seed` | Seme per la generazione di numeri casuali per controllare la riproducibilità. | INT | Sì | da 0 a 4294967295 |
| `keyframes` | Sequenza di keyframe dai nodi Luma Ray 3.2 Keyframe (almeno 2). | LUMA_RAY32_KEYFRAME | Sì | da 2 a 64 keyframe |

**Nota:** La sequenza di keyframe deve contenere almeno 2 keyframe e al massimo 64 keyframe. Ogni keyframe deve avere una posizione distinta sulla timeline. Le posizioni dei keyframe vengono risolte in indici di fotogramma di output in base alla durata selezionata (120 fotogrammi per 5s, 240 fotogrammi per 10s). Le posizioni dei keyframe in modalità secondi non devono superare la durata totale del video.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video generato in output. | VIDEO |
| `generation_id` | L'identificatore univoco per la richiesta di generazione. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`
