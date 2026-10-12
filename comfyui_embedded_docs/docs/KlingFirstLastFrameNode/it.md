# Kling 3.0 Primo-Ultimo Frame in Video

Questo nodo utilizza il modello Kling 3.0 per generare un video. Crea il video basandosi su un prompt testuale, una durata specificata e due immagini fornite: un fotogramma iniziale e un fotogramma finale. Il nodo può anche generare l'audio di accompagnamento per il video.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Impostazioni del modello e di generazione. Selezionando questa opzione viene mostrato un parametro `resolution` annidato. | DYNAMIC_COMBO | Sì | `"kling-v3"` |
| `prompt` | La descrizione testuale che guida la generazione del video. Deve contenere da 1 a 2500 caratteri. | STRING | Sì | N/A |
| `duration` | La durata del video in secondi (predefinito: 5). | INT | Sì | 3 a 15 |
| `first_frame` | L'immagine iniziale del video. Deve essere di almeno 300x300 pixel e avere un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1. | IMAGE | Sì | N/A |
| `end_frame` | L'immagine finale del video. Deve essere di almeno 300x300 pixel e avere un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1. | IMAGE | Sì | N/A |
| `generate_audio` | Controlla se generare l'audio per il video (predefinito: True). | BOOLEAN | Sì | N/A |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | 0 a 2147483647 |

### Input di Kling V3

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `resolution` | La risoluzione per il video generato (predefinito: `"1080p"`). | COMBO | Sì | `"4k"`<br>`"1080p"`<br>`"720p"` |

**Nota:** Le immagini `first_frame` e `end_frame` devono essere di almeno 300x300 pixel e avere un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1 affinché il nodo funzioni correttamente. Il `prompt` deve contenere tra 1 e 2500 caratteri. L'opzione `resolution` corrisponde a una modalità di generazione Kling: `"4k"`, `"1080p"` (pro) e `"720p"` (standard).

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `b71119c3267e2a74d2180e5182463c78828e892bfcf1eeb7c33a0f4d7019997f`
