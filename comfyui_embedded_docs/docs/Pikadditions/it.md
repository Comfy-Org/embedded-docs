# Pikadditions

Il nodo Pikadditions consente di aggiungere qualsiasi oggetto o immagine al tuo video. Carichi un video e specifichi ciò che desideri aggiungere per creare un risultato integrato in modo armonioso. Questo nodo utilizza l'API Pika per inserire immagini nei video con un'integrazione dall'aspetto naturale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Il video a cui aggiungere un'immagine. | VIDEO | Sì | - |
| `image` | L'immagine da aggiungere al video. | IMAGE | Sì | - |
| `prompt_text` | Descrizione testuale di ciò che si desidera aggiungere al video. | STRING | Sì | - |
| `negative_prompt` | Descrizione testuale di ciò che si desidera evitare nel video. | STRING | Sì | - |
| `seed` | Valore di seed casuale per risultati riproducibili. | INT | Sì | 0 a 4294967295 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il video elaborato con l'immagine inserita. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/it.md)

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
