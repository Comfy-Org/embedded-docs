# Ritaglia Maschera

Il nodo CropMask è progettato per ritagliare un'area specificata da una maschera data. Consente agli utenti di definire la regione di interesse specificando coordinate e dimensioni, estraendo di fatto una porzione della maschera per ulteriori elaborazioni o analisi.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | L'input `mask` rappresenta l'immagine maschera da ritagliare. È essenziale per definire l'area da estrarre in base alle coordinate e alle dimensioni specificate. | MASK |
| `x` | La coordinata `x` specifica il punto di partenza sull'asse orizzontale da cui deve iniziare il ritaglio. | INT |
| `y` | La coordinata `y` determina il punto di partenza sull'asse verticale per l'operazione di ritaglio. | INT |
| `width` | La larghezza (`width`) definisce l'estensione orizzontale dell'area di ritaglio dal punto di partenza. | INT |
| `height` | L'altezza (`height`) specifica l'estensione verticale dell'area di ritaglio dal punto di partenza. | INT |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | L'output è una maschera ritagliata, ovvero una porzione della maschera originale definita dalle coordinate e dalle dimensioni specificate. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/it.md)
