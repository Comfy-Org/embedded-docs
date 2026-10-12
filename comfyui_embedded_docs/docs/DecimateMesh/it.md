# Decima mesh

Semplifica una mesh 3D a un numero target di facce usando la semplificazione QEM (quadric error metric), eseguendo il calcolo sul dispositivo di calcolo attivo. La modalità di posizionamento `"midpoint"` è il preset fedele a cumesh che offre la migliore qualità preservando al contempo le caratteristiche sottili come i capelli, mentre `"qem"` posiziona i vertici nella posizione ottimale secondo QEM con controlli opzionali per linee e bordi di feature. La mesh di output rimane saldata.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh 3D da semplificare. | MESH | Sì | - |
| `target_face_count` | Numero massimo di facce target. 0 disabilita. (predefinito: 200000) | INT | Sì | 0 a 50000000 |
| `placement_mode` | midpoint: fedele a cumesh (consigliato). qem: posizionamento ottimale secondo QEM. (predefinito: `"midpoint"`) | DYNAMIC_COMBO | Sì | `"midpoint"`<br>`"qem"` |

### Input di Midpoint

La modalità di posizionamento `"midpoint"` non espone sottoparametri aggiuntivi; utilizza il preset di posizionamento midpoint predefinito.

### Input di QEM

I seguenti sottoparametri compaiono nell'interfaccia solo quando `placement_mode` è impostato su `"qem"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `line_quadric_weight` | Peso della quadrica di linea per bordo; preserva creste/valli nette. 0 = disattivato. (predefinito: 0.0) | FLOAT | No | 0.0 a 100.0 |
| `feature_edge_quadric_weight` | Peso quadrico aggiuntivo sui bordi di feature diedrali (pieghe). 0 = disattivato. (predefinito: 0.0) | FLOAT | No | 0.0 a 1000.0 |
| `feature_edge_min_dihedral_deg` | Angolo diedrale minimo (in gradi) per considerare un bordo come bordo di feature. (predefinito: 30.0) | FLOAT | No | 0.0 a 180.0 |
| `clamp_v_to_edge` | Proietta la posizione ottimale secondo QEM sul segmento del bordo collassato. (predefinito: true) | BOOLEAN | No | `true`<br>`false` |

Nota: la decimazione viene saltata quando `target_face_count` è 0 o quando la mesh ha già un numero di facce non superiore a quello target. Il nodo mostra su se stesso un riepilogo della riduzione delle facce, ad esempio `faces: 1.23M → 200K (-84%)`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mesh` | La mesh semplificata con il numero di facce ridotto; la connettività rimane saldata. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/it.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
