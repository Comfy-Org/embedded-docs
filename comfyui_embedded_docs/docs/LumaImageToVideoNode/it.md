# Luma Da Immagine a Video

Genera video in modo sincrono in base a un prompt testuale e a immagini opzionali di inizio/fine. Questo nodo utilizza l'API Luma per creare video, consentendoti di definire il contenuto del video tramite un prompt e, facoltativamente, di specificare il primo e/o l'ultimo fotogramma per controllare la struttura del video.

**Nota:** Questo nodo è contrassegnato come deprecato nel codice sorgente. Luma rimuoverà gli endpoint chiamati da questo nodo il 24 ottobre 2026, quindi usa invece i nodi Luma Ray 3.2.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione del video (predefinito: "") | STRING | Sì | - |
| `model` | Seleziona il modello di generazione video tra i modelli Luma disponibili | COMBO | Sì | `"ray-1-6"`<br>`"ray-2"` |
| `resolution` | Risoluzione di output per il video generato (predefinito: "540p"). Questo parametro viene ignorato quando si utilizza il modello `ray-1-6`. | COMBO | Sì | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `duration` | Durata del video generato. Questo parametro viene ignorato quando si utilizza il modello `ray-1-6`. | COMBO | Sì | `"5s"`<br>`"9s"` |
| `loop` | Indica se il video generato deve essere riprodotto in loop (predefinito: False) | BOOLEAN | Sì | - |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | 0 to 18446744073709551615 |
| `first_image` | Primo fotogramma del video generato. (opzionale) | IMAGE | No | - |
| `last_image` | Ultimo fotogramma del video generato. (opzionale) | IMAGE | No | - |
| `luma_concepts` | Camera Concepts opzionali per determinare il movimento della camera tramite il nodo Luma Concepts. (opzionale) | CUSTOM | No | - |

**Nota:** Almeno uno tra `first_image` e `last_image` deve essere fornito. Il nodo solleva un'eccezione se mancano entrambi. I parametri `resolution` e `duration` vengono ignorati quando il `model` è impostato su `ray-1-6`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `c69d09286aba39062faa292e054d313833d977888a3cc7188a5ea8fdc9e66913`
