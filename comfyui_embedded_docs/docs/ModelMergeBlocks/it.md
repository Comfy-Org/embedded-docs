# ModelMergeBlocks

ModelMergeBlocks è progettato per operazioni avanzate di fusione di modelli, consentendo l'integrazione di due modelli con rapporti di miscelazione personalizzabili per diverse parti dei modelli. Questo nodo facilita la creazione di modelli ibridi unendo selettivamente componenti da due modelli di origine in base ai parametri specificati.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model1` | Il primo modello da fondere. Funge da modello di base su cui vengono applicate le patch dal secondo modello. | `MODEL` |
| `model2` | Il secondo modello dal quale vengono estratte e applicate le patch al primo modello, in base ai rapporti di miscelazione specificati. | `MODEL` |
| `input` | Specifica il rapporto di miscelazione per il livello di input dei modelli. Determina quanto del livello di input del secondo modello viene fuso nel primo modello. | `FLOAT` |
| `middle` | Definisce il rapporto di miscelazione per i livelli intermedi dei modelli. Questo parametro controlla il livello di integrazione dei livelli intermedi dei modelli. | `FLOAT` |
| `out` | Determina il rapporto di miscelazione per il livello di output dei modelli. Influisce sull'output finale regolando il contributo del livello di output del secondo modello. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello fuso risultante, ibrido dei due modelli di input, con le patch applicate in base ai rapporti di miscelazione specificati. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/it.md)
