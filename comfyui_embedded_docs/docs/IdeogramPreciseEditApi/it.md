# IdeogramPreciseEditApi

Modifica un'immagine guidata da un prompt testuale con la modifica precisa di Ideogram 4.5: cambia solo ciò che il prompt richiede, i pixel non toccati rimangono identici e l'output mantiene la dimensione dell'immagine 1. L'immagine 1 è l'immagine da modificare e fino a 4 ulteriori immagini possono essere collegate come riferimenti.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `model` | Modello da usare. (predefinito: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sì | `"ideogram-4.5"` |
| `images` | Slot espandibile: l'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti opzionali (`image_1` ... `image_5`). Fai riferimento a esse nel prompt come @Image1, @Image2, ...; un input in batch conta una volta per immagine. Ogni immagine deve avere un rapporto d'aspetto compreso tra 1:6 e 6:1. | IMAGE | Sì | da 1 a 5 immagini |
| `prompt` | Istruzioni di modifica. Supporta riferimenti in stile @Image1 alle immagini collegate. (predefinito: stringa vuota) | STRING | Sì | da 1 a 10000 caratteri |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo. (predefinito: `"medium"`) | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed per la generazione. Le stesse immagini, prompt, impostazioni e seed danno lo stesso risultato. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |

### Vincoli dei parametri

- **Numero di immagini:** almeno 1 e al massimo 5 immagini; un input in batch conta una volta per immagine. L'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti.
- **Dimensione output:** il risultato mantiene la dimensione dell'immagine 1, quindi questo nodo non ha input size, width o height.
- **Rapporto d'aspetto dell'immagine:** ogni immagine non deve essere più larga di 6 volte la sua altezza né più alta di 6 volte la sua larghezza (tra 1:6 e 6:1).
- **Tag del prompt:** `@ImageN` viene confrontato senza distinzione tra maiuscole e minuscole e non deve superare il numero di immagini collegate; il prompt non deve contenere solo spazi bianchi e deve contenere al massimo 10000 caratteri.
- **Ridimensionamento al caricamento:** le immagini più grandi di circa 4 MP, o più grandi di 4608 px sul lato lungo, vengono ridimensionate prima di essere inviate.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca il risultato, il nodo genera un errore invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine modificata come batch, alla dimensione dell'immagine 1. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/it.md)

---
**Source fingerprint (SHA-256):** `74ba429ac93e4528e44c864ccfd3928f6c42108cfcc83577c8963a099a66f527`
