# Luma Concepts

Contiene uno o più concetti di camera da usare con i nodi Luma Text to Video e Luma Image to Video. Questo nodo consente di selezionare fino a quattro concetti di camera e, facoltativamente, di combinarli con catene di concetti esistenti.

**Nota:** Questo nodo è contrassegnato come deprecato nel codice sorgente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `concept1` | Selezione del primo concetto di camera tra i concetti Luma disponibili | STRING | Sì | Più opzioni disponibili<br>Include l'opzione "None" |
| `concept2` | Selezione del secondo concetto di camera tra i concetti Luma disponibili | STRING | Sì | Più opzioni disponibili<br>Include l'opzione "None" |
| `concept3` | Selezione del terzo concetto di camera tra i concetti Luma disponibili | STRING | Sì | Più opzioni disponibili<br>Include l'opzione "None" |
| `concept4` | Selezione del quarto concetto di camera tra i concetti Luma disponibili | STRING | Sì | Più opzioni disponibili<br>Include l'opzione "None" |
| `luma_concepts` | Concetti di camera opzionali da aggiungere a quelli scelti qui | LUMA_CONCEPTS | No | N/A |

**Nota:** Tutti i parametri dei concetti (`concept1` fino a `concept4`) possono essere impostati su "None" se non vuoi usare tutti e quattro gli slot dei concetti. Il nodo unirà gli eventuali `luma_concepts` forniti con i concetti selezionati per creare una catena di concetti combinata.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `luma_concepts` | Catena combinata di concetti di camera contenente tutti i concetti selezionati | LUMA_CONCEPTS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/it.md)

---
**Source fingerprint (SHA-256):** `fc9da6288e29d89519f13e2412381ad8d689fc48353a80546a380dbe8f979037`
