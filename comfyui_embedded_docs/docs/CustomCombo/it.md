# Combinazione Personalizzata

Il nodo Custom Combo consente di definire un proprio elenco di opzioni testuali per un menu a discesa anziché scegliere tra valori fissi. È un nodo incentrato sul frontend che dispone anche di una rappresentazione backend, quindi i workflow che lo contengono rimangono compatibili. Quando si seleziona un'opzione, il nodo restituisce in output il testo selezionato e la sua posizione di indice.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `choice` | L'opzione testuale selezionata dal menu a discesa personalizzato. L'elenco delle opzioni disponibili è definito dall'utente nell'interfaccia frontend del nodo. | COMBO | Sì | Definito dall'utente |
| `index` | Un valore intero che può essere utilizzato per specificare un indice. Predefinito: 0. | INT | No | Qualsiasi intero (predefinito: 0) |

**Nota:** La validazione degli input di questo nodo è intenzionalmente disabilitata. Ciò consente di scrivere qualsiasi opzione testuale personalizzata nel frontend senza che il backend verifichi se la selezione corrisponde a un elenco predefinito. I widget diversi dal menu a discesa combo sono completamente definiti nel frontend. Questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `STRING` | La stringa di testo dell'opzione selezionata dalla casella combinata personalizzata. | STRING |
| `INDEX` | La posizione di indice dell'opzione selezionata nell'elenco a discesa. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/it.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
