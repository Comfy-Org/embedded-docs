# LoadImageMask

Il nodo LoadImageMask è progettato per caricare immagini e le relative maschere da un percorso specificato, elaborandole per garantirne la compatibilità con ulteriori attività di manipolazione o analisi delle immagini. Si concentra sulla gestione di vari formati e condizioni delle immagini, come la presenza di un canale alfa per le maschere, e prepara le immagini e le maschere per l'elaborazione a valle convertendole in un formato standardizzato.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Il parametro `image` specifica il file immagine da caricare ed elaborare. Svolge un ruolo cruciale nel determinare l'output fornendo l'immagine di origine per l'estrazione della maschera e la conversione del formato. | COMBO[STRING] |
| `channel` | Il parametro `channel` specifica il canale di colore dell'immagine che verrà utilizzato per generare la maschera. Ciò consente flessibilità nella creazione della maschera in base a diversi canali di colore, migliorando l'utilità del nodo in vari scenari di elaborazione delle immagini. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `mask` | Questo nodo restituisce la maschera generata dall'immagine e dal canale specificati, preparata in un formato standardizzato adatto per ulteriori elaborazioni in attività di manipolazione delle immagini. | `MASK` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageMask/it.md)
