# Rodin3D_Regular

Il nodo Rodin 3D Regular genera asset 3D utilizzando l'API Rodin. Prende in input delle immagini e le elabora tramite il servizio Rodin per creare modelli 3D. Il nodo gestisce l'intero flusso di lavoro dalla creazione dell'attività al download dei file del modello 3D finale.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `Images` | Immagini di input utilizzate per la generazione del modello 3D. È possibile fornire fino a 5 immagini. È richiesta almeno 1 immagine. | IMAGE | Sì | - |
| `Seed` | Valore di seed casuale per risultati riproducibili (predefinito: 0). | INT | No | 0 a 65535 |
| `Material_Type` | Tipo di materiale da applicare al modello 3D (predefinito: "PBR"). | STRING | No | `"PBR"`<br>`"Shaded"` |
| `Polygon_count` | Numero di poligoni target e tipo di mesh per il modello 3D generato (predefinito: "18K-Quad"). | STRING | No | `"4K-Quad"`<br>`"8K-Quad"`<br>`"18K-Quad"`<br>`"50K-Quad"`<br>`"200K-Triangle"` |

**Nota:** È richiesta almeno 1 immagine per la generazione del modello 3D. È possibile fornire un massimo di 5 immagini.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `3D Model Path` | Percorso del file del modello 3D generato (mantenuto per compatibilità con le versioni precedenti). | STRING |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/it.md)

---
**Source fingerprint (SHA-256):** `e0bd8ef311f33481fec877801dea80302eba076f2d9e12f52467e889242a9637`
