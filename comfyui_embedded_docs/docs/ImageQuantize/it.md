# ImageQuantize

Il nodo ImageQuantize è progettato per ridurre il numero di colori in un'immagine a un numero specificato, applicando opzionalmente tecniche di dithering per mantenerne la qualità visiva. Questo processo è utile per creare immagini basate su palette o per ridurre la complessità cromatica in determinate applicazioni.

## Input
| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | Il tensore immagine di input da quantizzare. Influisce sull'esecuzione del nodo essendo il dato principale su cui viene eseguita la riduzione cromatica. | `IMAGE` |
| `colors` | Specifica il numero di colori a cui ridurre l'immagine. Influisce direttamente sul processo di quantizzazione determinando la dimensione della palette di colori. | `INT` |
| `dither` | Determina la tecnica di dithering da applicare durante la quantizzazione, influenzando la qualità visiva e l'aspetto dell'immagine di output. | COMBO[STRING] |

## Output
| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | La versione quantizzata dell'immagine di input, con complessità cromatica ridotta e opzionalmente sottoposta a dithering per mantenerne la qualità visiva. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/it.md)
