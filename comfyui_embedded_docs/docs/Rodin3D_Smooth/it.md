# Rodin3D_Smooth

Il nodo Rodin 3D Smooth genera asset 3D utilizzando l'API Rodin, elaborando immagini di input e convertendole in modelli 3D levigati. Accetta più immagini come input e produce un file di modello 3D scaricabile. Il nodo gestisce automaticamente l'intero processo di generazione, inclusi la creazione dell'attività, il polling dello stato e il download dei file.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `Images` | Immagini di input da utilizzare per la generazione del modello 3D. È possibile fornire più immagini (fino a 5). | IMAGE | Sì | - |
| `Seed` | Valore di seed casuale per la coerenza della generazione (predefinito: 0). | INT | No | 0 to 65535 |
| `Material_Type` | Tipo di materiale da applicare al modello 3D (predefinito: "PBR"). | STRING | No | "PBR"<br>"Shaded" |
| `Polygon_count` | Numero target di poligoni per il modello 3D generato. Determina la qualità della mesh e il livello di dettaglio (predefinito: "18K-Quad"). | STRING | No | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"200K-Triangle" |

**Nota:** Il nodo accetta fino a 5 immagini di input. Se non viene fornita alcuna immagine, verrà generato un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `3D Model Path` | Percorso del file del modello 3D scaricato (solo per retrocompatibilità). | STRING |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/it.md)

---
**Source fingerprint (SHA-256):** `c7dc23d2a7a8e2d425fc389476ef381f4ebf974f522c6e3774222866eee064e9`
