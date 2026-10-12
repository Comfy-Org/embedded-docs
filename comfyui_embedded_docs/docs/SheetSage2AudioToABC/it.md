# SheetSage2AudioToABC

Questo nodo trascrive melodie vocali e strumentali dalla musica in notazione ABC, un formato testuale per scrivere spartiti musicali. Analizza l'audio collegato e restituisce la notazione risultante come testo, che può poi essere fornita al nodo YuE2 Generate Music utilizzando la modalità corrispondente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio_encoder` | Il modello encoder audio usato per analizzare l'audio e produrre la notazione ABC. | AUDIO_ENCODER | Sì | - |
| `audio` | L'audio musicale da trascrivere in notazione ABC. | AUDIO | Sì | - |
| `mode` | Controlla cosa viene trascritto. "full" genera melodia e accordi; "melody" genera solo la melodia, consigliato per le cover. | COMBO | Sì | `"melody"`<br>`"full"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `abc` | La musica trascritta in notazione ABC, restituita come elenco di stringhe. Collega questo al nodo YuE2 Generate Music e usa la modalità corrispondente. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SheetSage2AudioToABC/it.md)

---
**Source fingerprint (SHA-256):** `612d18dedd09b64210087c340b8f304ace8cd7b30b1a6e8e8ba7c749b355a497`
