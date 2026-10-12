# SaveVideo

Il nodo Save Video salva il video di input nella directory di output di ComfyUI. È possibile scegliere il prefisso del nome file, il formato del contenitore, il codec video e le opzioni di codifica come la qualità. Il nodo genera automaticamente un nome file univoco usando un contatore e può incorporare i metadati del workflow nel file salvato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Il video da salvare. | VIDEO | Sì | - |
| `filename_prefix` | Il prefisso per il file da salvare. Può includere informazioni di formattazione come `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%` per includere valori dai nodi (predefinito: `video/ComfyUI`). | STRING | Sì | - |
| `format` | Il contenitore di output. Auto usa MP4 per Auto/H.264 e WebM per AV1. MP4, MKV e WebM selezionano un contenitore specifico. Selezionare un formato determina anche quali opzioni di codec sono disponibili (predefinito: `auto`). | DYNAMIC_COMBO | Sì | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | Il codec video di output. Auto preserva un flusso sorgente compatibile. La ricodifica H.264 e AV1 supporta SDR, HDR (HLG) e HDR PQ. Questo selettore è annidato sotto il formato scelto (predefinito: `auto`). | DYNAMIC_COMBO | No | `"auto"`<br>`"h264"`<br>`"av1"` (non disponibile con il formato `webm`) |

### Input di H.264

Questi input compaiono quando `codec` è `"h264"` e sono disponibili con i formati `auto`, `mp4` e `mkv`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `encoding` | L'opzione automatica preserva i flussi H.264 compatibili. L'opzione di ricodifica applica opzioni di codifica personalizzate. | DYNAMIC_COMBO | No | `"auto"`<br>`"re-encode"` |
| `crf` | Valori più bassi producono una qualità più alta e file più grandi. Compare quando `encoding` è `"re-encode"` (predefinito: 23.0). | FLOAT | No | da 0.0 a 51.0 |

### Input di AV1

Questi input compaiono quando `codec` è `"av1"` e sono disponibili con i formati `auto`, `mp4`, `mkv` e `webm`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `encoding` | L'opzione automatica preserva i flussi AV1 compatibili. L'opzione di ricodifica applica opzioni di codifica personalizzate. | DYNAMIC_COMBO | No | `"auto"`<br>`"re-encode"` |
| `crf` | Valori più bassi producono una qualità più alta e file più grandi. Compare quando `encoding` è `"re-encode"` (predefinito: 30.0). | FLOAT | No | da 0.0 a 63.0 |

Nota: quando `format` è `"auto"`, il contenitore salvato viene scelto automaticamente: `av1` produce WebM, mentre `auto` e `h264` producono MP4. Il formato `webm` consente solo i codec `auto` e `av1`. Quando `codec` è `"auto"`, il flusso video sorgente viene preservato invece di essere ricodificato. Il file salvato usa un suffisso contatore per evitare di sovrascrivere i file esistenti. L'estensione del file è determinata dal contenitore risolto. I metadati del workflow (il prompt e le informazioni extra sui nodi) vengono incorporati nel file salvato, a meno che il salvataggio dei metadati non sia disabilitato all'avvio.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video di input, invariato. | VIDEO |
| `ui` | Un'anteprima del file video salvato, inclusi il percorso del file e le informazioni sulla sottocartella per la visualizzazione nell'interfaccia utente. | PREVIEW_VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/it.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`
