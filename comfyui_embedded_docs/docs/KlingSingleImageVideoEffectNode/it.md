# KlingSingleImageVideoEffectNode

Il nodo Kling Single Image Video Effect crea video con diversi effetti speciali basati su una singola immagine di riferimento. Applica vari effetti visivi e scene per trasformare immagini statiche in contenuti video dinamici. Il nodo supporta diverse scene con effetti, opzioni del modello e durate video per ottenere il risultato visivo desiderato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Immagine di riferimento. URL o stringa codificata in Base64 (senza prefisso data:image). La dimensione del file non può superare 10MB, la risoluzione non deve essere inferiore a 300x300px, il rapporto d'aspetto deve essere compreso tra 1:2.5 e 2.5:1 | IMAGE | Sì | - |
| `effect_scene` | Il tipo di scena con effetto speciale da applicare alla generazione del video. Alcuni effetti possono avere prezzi diversi. | COMBO | Sì | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_name` | La versione specifica del modello da utilizzare per generare l'effetto video. | COMBO | Sì | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `duration` | La durata del video generato in secondi. | COMBO | Sì | `"5"`<br>`"10"` |

**Nota:** Il parametro `effect_scene` influisce sul costo del nodo. Gli effetti `dizzydizzy` e `bloombloom` costano $0.49 USD per generazione, mentre tutti gli altri effetti costano $0.28 USD per generazione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato con gli effetti applicati | VIDEO |
| `video_id` | L'identificatore univoco del video generato | STRING |
| `duration` | La durata del video generato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/it.md)

---
**Source fingerprint (SHA-256):** `fb4a8b044daa99154a58d6926ff746bd2397b71ea32f1fafc851589f163ab51a`
