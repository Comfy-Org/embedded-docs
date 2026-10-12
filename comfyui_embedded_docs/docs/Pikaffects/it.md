# Pikaffects

Il nodo Pikaffects genera video con vari effetti visivi applicati a un'immagine di input. Utilizza l'API di generazione video di Pika per trasformare immagini statiche in video animati con effetti specifici come scioglimento, esplosione o levitazione. Il nodo richiede una chiave API e un token di autenticazione per accedere al servizio Pika.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di riferimento a cui applicare il Pikaffect. | IMAGE | Sì | - |
| `pikaffect` | L'effetto visivo specifico da applicare all'immagine (predefinito: "Cake-ify"). | COMBO | Sì | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | Descrizione testuale che guida la generazione del video. | STRING | Sì | - |
| `negative_prompt` | Descrizione testuale di ciò che deve essere evitato nel video generato. | STRING | Sì | - |
| `seed` | Valore di seed casuale per risultati riproducibili. | INT | Sì | 0 to 4294967295 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il video generato con il Pikaffect applicato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/it.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`
