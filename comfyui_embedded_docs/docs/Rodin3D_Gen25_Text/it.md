# Rodin 3D Gen-2.5 - Testo a 3D

## Panoramica

Genera un modello 3D da un prompt testuale utilizzando l'API Rodin Gen-2.5. Puoi scegliere tra diverse modalità di qualità (Fast, Regular o Extreme-High) per bilanciare velocità di generazione e qualità dell'output.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per il modello 3D. | STRING | Sì | Da 1 a 1024 caratteri |
| `mode` | La modalità di qualità e velocità di generazione. "Fast" è la più rapida, "Extreme-High" produce la qualità più alta ma richiede più tempo. | COMBO | Sì | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | Lo stile del materiale per il modello 3D generato. | COMBO | Sì | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | Il formato file per il modello 3D di output. | COMBO | Sì | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | Modalità di generazione delle texture. "None" non produce texture, "Generated" crea texture standard, "Generated+HD" crea texture ad alta definizione. | COMBO | Sì | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | Seme casuale per risultati riproducibili. Usare lo stesso seme con gli stessi input produrrà lo stesso output. | INT | Sì | Da 0 a 2147483647 |
| `TAPose` | Indica se applicare la posa a T (braccia distese) al modello generato. | BOOLEAN | Sì | True / False |
| `hd_texture` | Indica se generare texture ad alta definizione per il modello. | BOOLEAN | Sì | True / False |
| `texture_delight` | Indica se applicare texture delight (qualità della texture migliorata) al modello. | BOOLEAN | Sì | True / False |
| `addon_highpack` | Indica se generare una versione ad alto numero di poligoni del modello oltre a quella standard. | BOOLEAN | Sì | True / False |
| `bbox_width` | La larghezza del bounding box in unità mondo. | INT | Sì | Da 1 a 1000 |
| `bbox_height` | L'altezza del bounding box in unità mondo. | INT | Sì | Da 1 a 1000 |
| `bbox_length` | La lunghezza del bounding box in unità mondo. | INT | Sì | Da 1 a 1000 |
| `height_cm` | L'altezza del modello generato in centimetri. | INT | Sì | Da 1 a 300 |

**Nota:** Il parametro `prompt` deve avere una lunghezza compresa tra 1 e 1024 caratteri. Se non specificato, il parametro `seed` ha valore predefinito 0 (casuale).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model_file` | Il file del modello 3D generato nel formato specificato. | FILE3DANY |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/it.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
