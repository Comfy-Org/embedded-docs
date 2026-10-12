# GetVideoComponents

Il nodo Get Video Components estrae tutti gli elementi principali da un file video. Separa il video in singoli fotogrammi, estrae la traccia audio e fornisce la frequenza dei fotogrammi, la profondità di bit e lo spazio colore del video. Ciò consente di lavorare con ciascun componente in modo indipendente per ulteriori elaborazioni o analisi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il video da cui estrarre i componenti. | VIDEO | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `images` | I singoli fotogrammi estratti dal video come immagini separate. | IMAGE |
| `audio` | La traccia audio estratta dal video. | AUDIO |
| `fps` | La frequenza dei fotogrammi del video, in fotogrammi al secondo. | FLOAT |
| `bit_depth` | La profondità di bit del video. | COMBO |
| `color_space` | Lo spazio colore del video. | COMBO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/it.md)

---
**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`
