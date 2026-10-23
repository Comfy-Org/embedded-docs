# ClipMergeSimple

`CLIPMergeSimple` è un nodo di fusione di modelli che combina due modelli di text encoder CLIP in base a un rapporto specificato. Clona il primo modello CLIP e applica patch ponderate dal secondo modello CLIP, saltando i componenti ID di posizione e scala logit, per produrre un modello ibrido che fonde caratteristiche da entrambe le fonti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip1` | Il primo modello CLIP da fondere. Funge da modello base per il processo di fusione. | CLIP | Sì | - |
| `clip2` | Il secondo modello CLIP da fondere. Le sue patch chiave, a eccezione degli ID di posizione e della scala logit, vengono applicate al primo modello in base al rapporto specificato. | CLIP | Sì | - |
| `ratio` | Determina la proporzione di caratteristiche del secondo modello da fondere nel primo modello. Un rapporto di 1.0 significa adottare completamente le caratteristiche del secondo modello, mentre 0.0 mantiene solo le caratteristiche del primo modello. Predefinito: 1.0. | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `clip` | Il modello CLIP fuso risultante, che incorpora caratteristiche da entrambi i modelli di input in base al rapporto specificato. | CLIP |

## Meccanismo di fusione spiegato

### Algoritmo di fusione

Il nodo utilizza una media ponderata per fondere i due modelli:

1. **Clona il modello base**: Per prima cosa clona `clip1` come modello base
2. **Ottieni le patch**: Recupera tutte le patch chiave da `clip2`
3. **Filtra le chiavi speciali**: Salta le chiavi che terminano con `.position_ids` e `.logit_scale`
4. **Applica la fusione ponderata**: Usa la formula `(1.0 - ratio) * clip1 + ratio * clip2`

### Spiegazione del parametro ratio

- **ratio = 0.0**: Usa completamente clip1, ignora clip2
- **ratio = 0.5**: Contributo del 50% da ciascun modello
- **ratio = 1.0**: Usa completamente clip2, ignora clip1

## Casi d'uso

1. **Fusione di stili di modello**: Combina le caratteristiche di modelli CLIP addestrati su dati diversi
2. **Ottimizzazione delle prestazioni**: Bilancia i punti di forza e di debolezza di modelli diversi
3. **Ricerca sperimentale**: Esplora combinazioni di diversi encoder CLIP

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/it.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
