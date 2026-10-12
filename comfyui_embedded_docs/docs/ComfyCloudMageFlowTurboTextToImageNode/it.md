# Comfy Cloud Mage Flow Turbo Da testo a immagine [BETA]

Questo nodo Comfy Cloud genera un'immagine da un prompt testuale utilizzando il workflow Mage-Flow Turbo (`mage-flow-turbo/text-to-image`). Esegue una versione distillata del modello Mage-Flow che produce l'immagine in 4 passaggi con un valore cfg di 1, impiegando circa un settimo del tempo GPU di un passaggio Mage-Flow completo, il che lo rende la variante pensata per l'iterazione rapida.

## Input

La classe del nodo stessa non dichiara widget di input nel sorgente disponibile; il suo schema di input è ereditato dalla classe base condivisa `_ComfyCloudMageFlowNode`, la cui definizione non è inclusa nell'istantanea del sorgente. In base al riepilogo del nodo e al nome del workflow text-to-image, il nodo accetta un prompt testuale che descrive l'immagine da generare.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Il prompt testuale che descrive l'immagine da generare. Il nome esatto del parametro è impostato dallo schema base ereditato `_ComfyCloudMageFlowNode` e può differire da questa etichetta. | STRING | Sì | Testo libero |

Nota: parametri di input aggiuntivi possono esistere nella definizione del nodo base ereditata, che non è disponibile nel sorgente fornito.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata dal prompt testuale. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/it.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`
