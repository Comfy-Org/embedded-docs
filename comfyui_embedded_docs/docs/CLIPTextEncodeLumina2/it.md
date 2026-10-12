# CLIP Text Encode (Lumina 2)

Questo nodo codifica un prompt di sistema e un prompt utente usando un modello CLIP in un embedding che può essere utilizzato per guidare il modello di diffusione verso la generazione di immagini specifiche. Combina un prompt di sistema Lumina 2 predefinito con il tuo prompt testuale personalizzato e li elabora tramite il modello CLIP per creare dati di condizionamento per la generazione di immagini.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2 fornisce due tipi di prompt di sistema: Superior: Sei un assistente progettato per generare immagini superiori con il grado superiore di allineamento immagine-testo basato su prompt testuali o prompt utente. Alignment: Sei un assistente progettato per generare immagini di alta qualità con il massimo grado di allineamento immagine-testo basato su prompt testuali. | COMBO | Sì | `"superior"`<br>`"alignment"` |
| `user_prompt` | Il testo da codificare. Supporta input multilinea e prompt dinamici. | STRING | Sì | N/A |
| `clip` | Il modello CLIP utilizzato per codificare il testo. | CLIP | Sì | N/A |

**Nota:** L'input `clip` è obbligatorio e non può essere None. Se l'input clip non è valido, il nodo genererà un errore indicando che il checkpoint potrebbe non contenere un modello CLIP o un text encoder validi.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Un condizionamento contenente il testo incorporato utilizzato per guidare il modello di diffusione. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/it.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
