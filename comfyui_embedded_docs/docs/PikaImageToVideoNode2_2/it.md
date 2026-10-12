# PikaImageToVideoNode2_2

Il nodo Pika Image to Video invia un'immagine e un prompt testuale all'API Pika versione 2.2 per generare un video. Converte l'immagine di input in formato video in base alla descrizione e alle impostazioni fornite. Il nodo gestisce la comunicazione con l'API e restituisce il video generato come output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine da convertire in video | IMAGE | Sì | - |
| `prompt_text` | La descrizione testuale che guida la generazione del video | STRING | Sì | - |
| `negative_prompt` | Testo che descrive cosa evitare nel video | STRING | Sì | - |
| `seed` | Valore di seed casuale per risultati riproducibili | INT | Sì | - |
| `resolution` | Impostazione della risoluzione del video in output | STRING | Sì | - |
| `duration` | Durata del video generato in secondi | INT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/it.md)

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
