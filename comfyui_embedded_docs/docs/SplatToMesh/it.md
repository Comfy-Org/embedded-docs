# SplatToMesh

Questo nodo converte uno splat gaussiano 3D in una superficie mesh colorata. Funziona rasterizzando le gaussiane su una griglia di densità, estraendo una iso-superficie a un livello di densità scelto, quindi applicando smoothing e pulizia opzionali per produrre una mesh triangolare colorata e pulita.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `splat` | Lo splat gaussiano di input da convertire in una mesh | SPLAT | Sì | - |
| `resolution` | Risoluzione della griglia di densità lungo l'asse più lungo. Valori più alti producono dettagli superficiali più fini ma richiedono più VRAM e tempo di elaborazione (cresce con resolution^3). Predefinito: 384 | INT | Sì | 64 - 768 (passo 16) |
| `kernel` | Massima semiampiezza dello splat in voxel. Ogni gaussiana viene rasterizzata su una finestra dimensionata al suo 3-sigma, limitata a questo valore. I surfel piccoli restano economici mentre quelli grandi non vengono troncati. Aumenta se splat radi lasciano vuoti. Predefinito: 5 | INT | Sì | 1 - 8 |
| `smooth` | Iterazioni di smoothing della mesh di Taubin. Leviga la superficie senza restringerla (a volume costante), a differenza della sfocatura della densità. 0 significa nessuno smoothing. Predefinito: 0 | INT | Sì | 0 - 60 |
| `level` | Livello dell'iso-superficie. Selezionato automaticamente tramite sogliatura di Otsu; questo valore influenza la selezione automatica (1.0 = auto, valori più bassi producono superfici più spesse/più connesse, valori più alti producono superfici più sottili/più strette). Predefinito: 0.4 | FLOAT | Sì | 0.0 - 2.0 (passo 0.01) |
| `min_component` | Elimina le componenti connesse più piccole di questo numero di vertici. Rimuove blob fluttuanti staccati e il guscio interno delle pareti doppie. 0 mantiene tutte le componenti. Predefinito: 500 | INT | Sì | 0 - 100000 (passo 50) |
| `min_opacity` | Ignora le gaussiane più deboli di questo valore prima della generazione della mesh. Predefinito: 0.02 | FLOAT | Sì | 0.0 - 1.0 (passo 0.01) |
| `color_sharpen` | Rende più nitida la texture dei vertici. 1.0 fornisce una fusione fisicamente corretta; valori più alti spingono il colore di ciascun voxel verso la sua gaussiana dominante invece di fare la media dei vicini (riduce lo sbavamento della texture). Influisce solo sul colore, non sulla geometria. Predefinito: 2.0 | FLOAT | Sì | 1.0 - 8.0 (passo 0.5) |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `mesh` | La mesh colorata estratta con rendering non illuminato (simile a emissivo) per corrispondere all'aspetto dello splat | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToMesh/it.md)

---
**Source fingerprint (SHA-256):** `5a7060c26252b587ce533e5682abe880a6fcc83f6671232489c3de64b094cd84`
