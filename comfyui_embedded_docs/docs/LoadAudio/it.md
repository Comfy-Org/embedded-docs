# LoadAudio

Il nodo LoadAudio carica i file audio dalla directory di input e li converte in un formato che può essere elaborato da altri nodi audio di ComfyUI. Legge i file audio ed estrae sia i dati della forma d'onda sia la frequenza di campionamento, rendendoli disponibili per le attività di elaborazione audio a valle.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | Il file audio da caricare dalla directory di input | AUDIO | Sì | Tutti i file audio e video supportati nella directory di input |

**Nota:** Il nodo accetta solo file audio e video presenti nella directory di input di ComfyUI. Il file deve esistere ed essere accessibile per un caricamento riuscito.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `AUDIO` | Dati audio contenenti informazioni sulla forma d'onda e sulla frequenza di campionamento | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/it.md)

---
**Source fingerprint (SHA-256):** `5631a5c50471e4612344c4bd0457e9824e9a7a8f8b75b22d06f13d5136c75258`
