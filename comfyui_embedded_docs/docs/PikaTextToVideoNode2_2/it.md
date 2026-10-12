# PikaTextToVideoNode2_2

Il nodo Pika Text2Video v2.2 invia un prompt testuale all'API Pika versione 2.2 per generare un video. Converte la descrizione testuale in un video utilizzando il servizio di generazione video AI di Pika. Il nodo consente di personalizzare vari aspetti del processo di generazione video, tra cui rapporto d'aspetto, durata e risoluzione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt_text` | La descrizione testuale principale che descrive ciò che si desidera generare nel video | STRING | Sì | - |
| `negative_prompt` | Testo che descrive ciò che non si desidera far apparire nel video generato | STRING | Sì | - |
| `seed` | Un numero che controlla la casualità della generazione per ottenere risultati riproducibili | INT | Sì | - |
| `resolution` | L'impostazione di risoluzione per il video di output | STRING | Sì | - |
| `duration` | La durata del video in secondi | INT | Sì | - |
| `aspect_ratio` | Rapporto d'aspetto (larghezza / altezza) (predefinito: 1.7777777777777777) | FLOAT | No | 0.4 - 2.5 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il file video generato restituito dall'API Pika | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/it.md)

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`
