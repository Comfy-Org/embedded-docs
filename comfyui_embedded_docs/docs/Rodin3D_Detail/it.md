# Rodin 3D Genera - Generazione Dettaglio

Il nodo Rodin 3D Detail genera asset 3D dettagliati utilizzando l'API Rodin. Accetta immagini di input e le elabora tramite il servizio Rodin per creare modelli 3D di alta qualità con geometria e materiali dettagliati. Il nodo gestisce l'intero flusso di lavoro, dalla creazione dell'attività allo scaricamento del file del modello 3D finale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `Images` | Immagini di input utilizzate per la generazione del modello 3D. È richiesta almeno 1 immagine e possono essere fornite al massimo 5 immagini. | IMAGE | Sì | - |
| `Seed` | Valore di seed casuale per risultati riproducibili (predefinito: 0) | INT | No | 0 a 65535 |
| `Material_Type` | Tipo di materiale da applicare al modello 3D (predefinito: "PBR") | STRING | No | `"PBR"`<br>`"Shaded"` |
| `Polygon_count` | Numero di poligoni target per il modello 3D generato. Determina il livello di qualità della mesh (predefinito: "18K-Quad") | STRING | No | `"4K-Quad"`<br>`"8K-Quad"`<br>`"18K-Quad"`<br>`"50K-Quad"`<br>`"200K-Triangle"` |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `3D Model Path` | Percorso del file del modello 3D generato (solo per compatibilità con le versioni precedenti) | STRING |
| `GLB` | Il modello 3D generato in formato GLB | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/it.md)

---
**Source fingerprint (SHA-256):** `941265733c20d27d67621a83a05be822731696f4dd376299510d4279a35f51ee`
