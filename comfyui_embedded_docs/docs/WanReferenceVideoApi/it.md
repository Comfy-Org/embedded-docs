# Wan Reference to Video

Il nodo Wan Reference to Video utilizza l'aspetto visivo e la voce di uno o più video di riferimento in input, insieme a un prompt testuale, per generare un nuovo video. Mantiene la coerenza con i personaggi del materiale di riferimento mentre crea nuovi contenuti in base alla tua descrizione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI specifico da utilizzare per la generazione del video. | COMBO | Sì | `"wan2.6-r2v"` |
| `prompt` | Una descrizione degli elementi e delle caratteristiche visive del nuovo video. Supporta l'inglese e il cinese. Usa identificatori come `character1` e `character2` per fare riferimento ai personaggi dei video di riferimento. | STRING | Sì | - |
| `negative_prompt` | Una descrizione di elementi o caratteristiche da evitare nel video generato. | STRING | No | - |
| `reference_videos` | Un elenco di input video utilizzati come riferimenti per l'aspetto e la voce dei personaggi. Devi fornire almeno un video. A ogni video può essere assegnato un nome come `character1`, `character2` o `character3`. | AUTOGROW | Sì | - |
| `size` | La risoluzione e le proporzioni (aspect ratio) per il video di output. | COMBO | Sì | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` |
| `duration` | La durata del video generato in secondi (predefinito: 5). | INT | Sì | da 5 a 10 |
| `seed` | Un valore di seed casuale per risultati riproducibili. Un valore pari a 0 genererà un seed casuale. | INT | No | da 0 a 2147483647 |
| `shot_type` | Specifica se il video generato è un'unica ripresa continua o contiene più riprese con tagli. | COMBO | Sì | `"single"`<br>`"multi"` |
| `watermark` | Se abilitato, una filigrana generata dall'IA viene aggiunta al video finale (predefinito: False). | BOOLEAN | No | - |

**Vincoli:**

* Ogni video fornito in `reference_videos` deve avere una durata compresa tra 2 e 30 secondi.
* Il parametro `duration` è limitato ai valori di 5 o 10 secondi.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video appena generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `65ca81a7b5e83f8d8f4c00db41e24d5238ef438887362838351464e77a3af0c2`
