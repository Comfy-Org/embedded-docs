# WanDancerPadKeyframes

## Panoramica

Questo nodo prepara una sequenza di fotogrammi chiave per uno specifico segmento di un processo più lungo di generazione video. Riceve un batch di immagini di input e una traccia audio, calcola quanti fotogrammi totali dovrebbe avere il video completo in base alla durata dell'audio, quindi distribuisce le immagini di input come fotogrammi chiave lungo il segmento scelto, riempiendo il resto con fotogrammi vuoti. Estrae inoltre la porzione corrispondente dell'audio per quel segmento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Le immagini di input da distribuire come fotogrammi chiave. | IMAGE | Sì | Batch di immagini |
| `segment_length` | Lunghezza di questo segmento in fotogrammi (predefinito: 149). | INT | Sì | da 1 a 10000 |
| `segment_index` | Quale segmento è questo (0 per il primo, 1 per il secondo, ecc., predefinito: 0). | INT | Sì | da 0 a 100 |
| `audio` | Audio da cui calcolare il numero totale di fotogrammi di output ed estrarre l'audio del segmento. | AUDIO | Sì | Dati audio |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `keyframes_sequence` | Sequenza di fotogrammi chiave con riempimento per il segmento specificato. | IMAGE |
| `keyframes_mask` | Maschera che indica i fotogrammi validi (1 per le posizioni dei fotogrammi chiave, 0 per le posizioni riempite). | MASK |
| `audio_segment` | Segmento audio per questo segmento video. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/it.md)

---
**Source fingerprint (SHA-256):** `93393e39cb1968b6e8720dfad213c16c534857bcfafcc577be64e0733ab3a760`
