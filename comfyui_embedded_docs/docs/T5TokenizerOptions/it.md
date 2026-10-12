# Opzioni Tokenizer T5

## Panoramica

Il nodo T5TokenizerOptions configura le impostazioni del tokenizer per vari tipi di modello T5. Imposta i parametri di padding minimo e lunghezza minima per diverse varianti del modello T5, tra cui t5xxl, pile_t5xl, t5base, mt5xl e umt5xxl. Il nodo riceve un input CLIP, applica le impostazioni a una copia di esso e restituisce il CLIP modificato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP per cui configurare le opzioni del tokenizer | CLIP | Sì | - |
| `min_padding` | Valore minimo di padding da impostare per tutti i tipi di modello T5 (predefinito: 0) | INT | Sì | 0 a 10000 |
| `min_length` | Valore minimo di lunghezza da impostare per tutti i tipi di modello T5 (predefinito: 0) | INT | Sì | 0 a 10000 |

Nota: questo nodo è contrassegnato come sperimentale in ComfyUI. Le impostazioni vengono applicate contemporaneamente a tutte le varianti T5 supportate: t5xxl, pile_t5xl, t5base, mt5xl e umt5xxl. L'input `clip` viene clonato prima della modifica, quindi il CLIP originale non viene alterato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il modello CLIP modificato con le opzioni del tokenizer aggiornate applicate a tutte le varianti T5 | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/it.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
