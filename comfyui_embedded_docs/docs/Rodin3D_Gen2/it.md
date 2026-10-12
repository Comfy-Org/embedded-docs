# Rodin 3D Genera - Generazione Gen-2

Il nodo Rodin3D_Gen2 genera asset 3D utilizzando l'API Rodin. Prende immagini di input e le converte in modelli 3D con vari tipi di materiale e conteggi poligonali. Il nodo gestisce automaticamente l'intero processo di generazione, inclusi la creazione dell'attività, il polling dello stato e il download dei file.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `Images` | Immagini di input da utilizzare per la generazione del modello 3D. Accetta da 1 a 5 immagini. | IMAGE | Sì | - |
| `Seed` | Valore del seed casuale per la generazione (predefinito: 0) | INT | No | 0-65535 |
| `Material_Type` | Tipo di materiale da applicare al modello 3D (predefinito: "PBR") | COMBO | No | "PBR"<br>"Shaded" |
| `Polygon_count` | Conteggio poligonale obiettivo e tipo di mesh per il modello 3D generato. Le opzioni "Quad" usano mesh basate su quad, le opzioni "Triangle" usano mesh basate su triangoli (predefinito: "500K-Triangle") | COMBO | No | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" |
| `TAPose` | Indica se applicare l'elaborazione TAPose (predefinito: False). Questo è un parametro avanzato. | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `3D Model Path` | Percorso del file del modello 3D generato (per retrocompatibilità) | STRING |
| `GLB` | Il modello 3D generato in formato GLB | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/it.md)

---
**Source fingerprint (SHA-256):** `6ee8b52152e84cca48c7875ce066ab19805a42e5cccc84865c6027a4f6fd3b16`
