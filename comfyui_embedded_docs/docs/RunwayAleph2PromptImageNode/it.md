# RunwayAleph2PromptImageNode

Questo nodo fissa un'immagine di guida a un momento specifico del video di output, controllando l'aspetto del video modificato in quel punto. Collega questo nodo all'input `prompt_images` del nodo Runway Aleph2 Video to Video e concatenane diversi (fino a 5) usando l'input opzionale `prompt_images`.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di guida da posizionare nel momento scelto del video di output. | IMAGE | Sì | - |
| `position` | Come posizionare questa immagine sulla timeline del video di output. Scegli tra temporizzazione assoluta (secondi dall'inizio) o temporizzazione frazionaria (frazione della durata del video). Selezionando un'opzione viene mostrato il sottoparametro corrispondente. | COMBO | Sì | `Absolute (seconds)`<br>`Fraction (0.0 to 1.0)` |
| `prompt_images` | Immagini di prompt precedenti opzionali da concatenare con questa. Collega qui l'output di un altro nodo Runway Aleph2 Prompt Image per creare una catena di massimo 5 immagini di guida. | PROMPT_IMAGE_CHAIN | No | - |

**Dettagli della modalità di posizione:**

- **Absolute (seconds):** Quando selezionata, devi fornire un valore `seconds` (predefinito: 0.0, intervallo: da 0.0 a 30.0, passo: 0.1). Questo specifica il tempo in secondi dall'inizio del video di output a cui si applica questa immagine.
- **Fraction (0.0 to 1.0):** Quando selezionata, devi fornire un valore `fraction` (predefinito: 0.0, intervallo: da 0.0 a 1.0, passo: 0.01). Questo specifica il punto nel video di output come frazione della sua durata totale (0.0 = inizio, 1.0 = fine).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `prompt_images` | Una catena di immagini di prompt che può essere collegata all'input `prompt_images` del nodo Runway Aleph2 Video to Video. Concatenando più nodi Runway Aleph2 Prompt Image si crea una sequenza di massimo 5 immagini di guida. | PROMPT_IMAGE_CHAIN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2PromptImageNode/it.md)

---
**Source fingerprint (SHA-256):** `a8b86fb5d73d27cc58aa59c195ca058eec8a5c9433ea09522ff3e905f6b88193`
