# ComboOptionTestNode

Questo nodo riceve due selezioni da caselle combinate e le inoltra direttamente alle proprie uscite senza modificarle.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `combo` | La prima selezione, scelta da un insieme di tre opzioni di test. | COMBO | Sì | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | La seconda selezione, scelta da un diverso insieme di tre opzioni di test. | COMBO | Sì | `"option4"`<br>`"option5"`<br>`"option6"` |

## Output
| Nome uscita | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output_1` | Restituisce il valore selezionato nella prima casella combinata (`combo`), invariato. | COMBO |
| `output_2` | Restituisce il valore selezionato nella seconda casella combinata (`combo2`), invariato. | COMBO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/it.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
