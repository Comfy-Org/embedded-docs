# MergeSplat

Il nodo Merge Splats combina più modelli di splat gaussiani in un unico splat concatenandone i dati. È utile per unire diverse decodifiche dello stesso latente generate con seed diversi, il che può densificare la superficie e migliorare la qualità durante la creazione di mesh 3D.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `splat0` | Primo splat gaussiano da unire | SPLAT | Sì | Almeno 1 splat richiesto |
| `splat1` | Secondo splat gaussiano da unire | SPLAT | Sì | Almeno 1 splat richiesto |
| `splat2` | Splat gaussiano aggiuntivo da unire (opzionale) | SPLAT | No | Fino a 32 splat totali |
| `splat3` | Splat gaussiano aggiuntivo da unire (opzionale) | SPLAT | No | Fino a 32 splat totali |
| ... | Splat aggiuntivi (fino a splat31) | SPLAT | No | Fino a 32 splat totali |

**Nota:** L'elenco degli input cresce automaticamente aggiungendo nuovi slot man mano che colleghi gli splat. Devi collegare almeno uno splat. Il nodo accetta un minimo di 2 e un massimo di 32 splat.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `splat` | Lo splat gaussiano unito che contiene tutti gli splat di input concatenati insieme | SPLAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeSplat/it.md)

---
**Source fingerprint (SHA-256):** `597671a3c37d1a4fb7b5a772396e08b7041b3fe8f04120891b1382d42e409d26`
