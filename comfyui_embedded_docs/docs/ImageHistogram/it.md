# Istogramma immagine

Il nodo ImageHistogram analizza la distribuzione cromatica di un'immagine in input. Calcola e restituisce diversi istogrammi, ovvero grafici che mostrano quanti pixel dell'immagine hanno ciascun possibile valore di intensità. Genera istogrammi separati per i canali di colore rosso, verde e blu, un istogramma RGB composito e un istogramma di luminanza basato su una formula standard di luminosità. Ogni istogramma contiene 256 bin, che coprono livelli di intensità da 0 a 255.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da analizzare. Il nodo elabora la prima immagine del batch. | IMAGE | Sì | N/A |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `rgb` | Un istogramma composito che rappresenta l'intensità media dei pixel nei canali rosso, verde e blu. | HISTOGRAM |
| `luminance` | Un istogramma della luminosità percepita dell'immagine, calcolato usando la formula standard di luminanza ITU-R BT.709. | HISTOGRAM |
| `red` | Un istogramma che mostra la distribuzione delle intensità dei pixel nel canale di colore rosso. | HISTOGRAM |
| `green` | Un istogramma che mostra la distribuzione delle intensità dei pixel nel canale di colore verde. | HISTOGRAM |
| `blue` | Un istogramma che mostra la distribuzione delle intensità dei pixel nel canale di colore blu. | HISTOGRAM |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/it.md)

---
**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`
