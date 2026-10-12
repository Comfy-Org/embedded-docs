# Anteprima Maschera

Il nodo MaskPreview visualizza un'anteprima visiva dei dati della maschera direttamente nell'interfaccia di ComfyUI, senza salvarla nella directory di output. Ciò consente di ispezionare la maschera in qualsiasi punto del workflow, mentre la maschera passa anche attraverso il nodo invariata, così da poter continuare a essere utilizzata nelle fasi successive.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mask` | I dati della maschera da visualizzare in anteprima | MASK | Sì | - |
| `filename_prefix` | Prefisso del nome file utilizzato per l'anteprima (predefinito: "ComfyUI") | STRING | No | - |
| `prompt` | Informazioni sul prompt per i metadati (fornite automaticamente) | PROMPT | No | - |
| `extra_pnginfo` | Informazioni PNG aggiuntive per i metadati (fornite automaticamente) | EXTRA_PNGINFO | No | - |

Solo `mask` è un input visibile che deve essere collegato. I parametri `filename_prefix`, `prompt` ed `extra_pnginfo` sono forniti dal sistema: `filename_prefix` utilizza il suo valore predefinito, mentre `prompt` ed `extra_pnginfo` sono nascosti e forniti automaticamente dal runtime di ComfyUI.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mask` | Gli stessi dati della maschera visualizzati in anteprima, restituiti invariati in modo che possano essere utilizzati altrove nel workflow | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/it.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
