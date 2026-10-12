# Recraft Stile - Immagine Realistica

Questo nodo crea una configurazione di stile per generare immagini realistiche utilizzando l'API di Recraft. Seleziona lo stile `realistic_image` e consente di scegliere un sottostile opzionale per perfezionare l'aspetto dell'output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `substyle` | Il sottostile specifico da applicare allo stile realistic_image. Se impostato su "None", non verrà applicato alcun sottostile. | STRING | Sì | Opzioni multiple disponibili (determinate dall'API Recraft) |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `recraft_style` | Un oggetto di configurazione dello stile Recraft contenente lo stile `realistic_image` e le impostazioni del sottostile selezionato. Questo output può essere collegato ad altri nodi Recraft che accettano un input di stile. | STYLEV3 |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/it.md)

---
**Source fingerprint (SHA-256):** `df3a09ae0956dd5807b7475248359085fdbe5abb5c40291e37db3ceabafef2ac`
