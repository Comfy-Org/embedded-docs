# ModelMergeSimple

Il nodo ModelMergeSimple è progettato per unire due modelli fondendo i loro parametri in base a un rapporto specificato. Questo nodo facilita la creazione di modelli ibridi che combinano i punti di forza o le caratteristiche di entrambi i modelli di input.

Il parametro `ratio` determina il rapporto di fusione tra i due modelli. Quando questo valore è 1, il modello di output è 100% `model1`, e quando questo valore è 0, il modello di output è 100% `model2`.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model1` | Il primo modello da unire. Funge da modello di base su cui vengono applicate le patch del secondo modello. | `MODEL` |
| `model2` | Il secondo modello, le cui patch vengono applicate al primo modello, influenzate dal rapporto specificato. | `MODEL` |
| `ratio` | Quando questo valore è 1, il modello di output è 100% `model1`, e quando questo valore è 0, il modello di output è 100% `model2`. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello unito risultante, che incorpora elementi da entrambi i modelli di input in base al rapporto specificato. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/it.md)
