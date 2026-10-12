# Rimuovi Spazi Testo

Il nodo StringTrim rimuove gli spazi bianchi (come spazi, tabulazioni e ritorni a capo) dall'inizio, dalla fine o da entrambi i lati di una stringa di testo. È possibile scegliere di rimuoverli dal lato sinistro, dal lato destro o da entrambi i lati della stringa. Questo è utile per ripulire gli input di testo rimuovendo spazi bianchi indesiderati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `string` | La stringa di testo da elaborare. Supporta input multilinea. | STRING | Sì | - |
| `mode` | Specifica da quale lato (o lati) della stringa rimuovere gli spazi bianchi. "Both" rimuove gli spazi bianchi da entrambe le estremità, "Left" li rimuove solo dall'inizio, "Right" li rimuove solo dalla fine. | COMBO | Sì | "Both"<br>"Left"<br>"Right" |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | La stringa di testo ripulita, con gli spazi bianchi rimossi in base alla modalità selezionata. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/it.md)

---
**Source fingerprint (SHA-256):** `b7d0694b752f3017a5f8ee9a6ca1d88260f761576b5960f2cb210e34efb09d18`
