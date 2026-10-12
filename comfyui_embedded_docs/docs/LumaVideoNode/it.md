# Luma Text to Video

Genera video in modo sincrono in base a un prompt testuale e alle impostazioni di output. Questo nodo crea contenuti video utilizzando descrizioni testuali e vari parametri di generazione, producendo il video finale una volta completato il processo di generazione.

**Nota:** Questo nodo è contrassegnato come deprecato nel codice sorgente. Luma rimuoverà gli endpoint chiamati da questo nodo il 24 ottobre 2026, quindi utilizza invece i nodi Luma Ray 3.2.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione del video (predefinito: stringa vuota). Deve contenere almeno 3 caratteri. | STRING | Sì | - |
| `model` | Il modello di generazione video da utilizzare. | COMBO | Sì | `"ray-1-6"`<br>`"ray-2"` |
| `aspect_ratio` | Il rapporto d'aspetto per il video generato (predefinito: "16:9"). | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `resolution` | La risoluzione di output per il video (predefinito: "540p"). Questo parametro viene ignorato quando si utilizza il modello `ray-1-6`. | COMBO | Sì | `"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | La durata del video generato. Questo parametro viene ignorato quando si utilizza il modello `ray-1-6`. | COMBO | Sì | `"5s"`<br>`"9s"` |
| `loop` | Indica se il video deve essere riprodotto in loop (predefinito: False). | BOOLEAN | Sì | - |
| `seed` | Seme per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seme (predefinito: 0). | INT | Sì | 0 a 18446744073709551615 |
| `luma_concepts` | Camera Concepts opzionali per determinare il movimento della telecamera tramite il nodo Luma Concepts. | CUSTOM | No | - |

**Nota:** Quando si utilizza il modello `ray-1-6`, i parametri `duration` e `resolution` vengono ignorati automaticamente e non influenzano la generazione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `86ebb2d035d35f142709546566d1041b66765ae3e0c2751e71c05df138a5ecf2`
