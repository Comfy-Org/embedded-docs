# AutogrowNamesTestNode

Questo nodo è un test per la funzionalità di input Autogrow. Accetta un gruppo dinamico di input float, ciascuno con un nome predefinito, e combina i loro valori in un'unica stringa separata da virgole.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `autogrow` | Un gruppo di input dinamico. È possibile aggiungere più input float, ciascuno con un nome predefinito dall'elenco: "a", "b" o "c". Il nodo accetta qualsiasi combinazione di questi input denominati. | FLOAT | Sì | Slot denominati: `a`, `b`, `c` |

**Nota:** L'input `autogrow` è dinamico. I singoli input float denominati "a", "b" e "c" possono essere aggiunti o rimossi secondo necessità. Tutti i valori forniti vengono elaborati dal nodo.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Una singola stringa contenente i valori di tutti gli input float forniti, uniti insieme da virgole. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/it.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
