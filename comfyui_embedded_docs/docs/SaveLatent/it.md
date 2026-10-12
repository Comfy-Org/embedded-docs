# Salva Latent

SaveLatent salva i tensori latenti su disco come file `.latent`, così possono essere riutilizzati o condivisi in seguito. Riceve campioni latenti, li scrive nella cartella di output con un nome generato automaticamente e può incorporare metadati del workflow, come il prompt, all'interno del file salvato. Gli stessi campioni latenti vengono anche passati invariati per ulteriori elaborazioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | I campioni latenti da salvare su disco. | LATENT | Sì | - |
| `filename_prefix` | Il prefisso usato per costruire il nome del file di output. Può includere sottocartelle, ad esempio "latents/ComfyUI" (predefinito: "latents/ComfyUI"). | STRING | Sì | - |
| `prompt` | Il prompt del workflow, serializzato come JSON e memorizzato nei metadati del file salvato (parametro nascosto, fornito automaticamente). | PROMPT | No | - |
| `extra_pnginfo` | Informazioni aggiuntive del workflow, serializzate come JSON e memorizzate nei metadati del file salvato (parametro nascosto, fornito automaticamente). | EXTRA_PNGINFO | No | - |

Nota: ogni file salvato viene denominato usando il prefisso e un contatore a 5 cifre, ad esempio `ComfyUI_00001_.latent`, e viene inserito nella directory di output. Il file contiene il tensore latente e un marcatore di versione del formato latente. I metadati vengono incorporati nel file salvato solo quando il supporto ai metadati è abilitato, cioè quando ComfyUI non viene avviato con l'opzione `--disable-metadata`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Gli stessi campioni latenti forniti come input, passati invariati. | LATENT |
| `ui` | Dati di visualizzazione dell'interfaccia che descrivono il file salvato: il suo nome file, la sottocartella e il tipo di output ("output"). | UI |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/it.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
