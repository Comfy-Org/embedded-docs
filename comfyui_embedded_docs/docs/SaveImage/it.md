# SaveImage

Il nodo SaveImage salva le immagini di input come file PNG nella directory di output di ComfyUI. Può incorporare metadati del workflow, come il prompt, in ciascun file salvato e restituisce le immagini invariate, così che possano ancora essere utilizzate da altri nodi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Le immagini da salvare. | IMAGE | Sì | - |
| `filename_prefix` | Il prefisso per il file da salvare. Può includere informazioni di formattazione come `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%` per includere valori dai nodi (predefinito: "ComfyUI"). | STRING | Sì | - |

Il nodo riceve anche due input nascosti, `prompt` e `extra_pnginfo`, che vengono popolati automaticamente da ComfyUI con il prompt del workflow e informazioni PNG aggiuntive. Quando i metadati sono abilitati, queste informazioni vengono incorporate come metadati testuali in ciascun file PNG salvato.

Il nome del file per ciascuna immagine salvata viene costruito a partire da `filename_prefix`, un segnaposto opzionale `%batch_num%` che viene sostituito con la posizione dell'immagine nel batch, e un contatore a cinque cifre, ad esempio `ComfyUI_00001_.png`. Le immagini vengono scritte con livello di compressione PNG 4.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | Le immagini originali di input, restituite invariate dopo essere state salvate su disco. | IMAGE |
| `ui` | Un risultato solo per la UI contenente l'elenco dei file immagine salvati (nome file, sottocartella e tipo) per la visualizzazione nel frontend. | UI_RESULT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/it.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
