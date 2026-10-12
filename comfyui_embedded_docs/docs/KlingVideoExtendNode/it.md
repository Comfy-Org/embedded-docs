# KlingVideoExtendNode

Il nodo Kling Video Extend consente di estendere i video creati da altri nodi Kling. Prende un video esistente identificato dal suo ID video e genera contenuto aggiuntivo in base ai tuoi prompt di testo. Il nodo funziona inviando la richiesta di estensione all'API Kling e restituendo il video esteso insieme al suo nuovo ID e alla sua durata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt di testo positivo per guidare l'estensione del video | STRING | No | - |
| `negative_prompt` | Prompt di testo negativo per gli elementi da evitare nel video esteso | STRING | No | - |
| `cfg_scale` | Controlla la forza della guida del prompt (predefinito: 0.5) | FLOAT | No | 0.0 - 1.0 |
| `video_id` | L'ID del video da estendere. Supporta video generati da operazioni text-to-video, image-to-video e precedenti estensioni video. Non può superare 3 minuti di durata totale dopo l'estensione. | STRING | Sì | - |

**Nota:** Il `video_id` deve fare riferimento a un video creato da altri nodi Kling, e la durata totale dopo l'estensione non può superare 3 minuti. Il prompt positivo non deve essere vuoto e entrambi i prompt devono essere inferiori a 2500 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il video esteso generato dall'API Kling | VIDEO |
| `video_id` | L'identificatore univoco per il video esteso | STRING |
| `duration` | La durata del video esteso | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/it.md)

---
**Source fingerprint (SHA-256):** `56674dee721a1784138852f5fd1cce137acf0b5e09bd9ee17353dde6fb251b5e`
