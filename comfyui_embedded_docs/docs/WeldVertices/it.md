# WeldVertices

Weld Vertices unisce i vertici coincidenti in una mesh 3D, così le facce che prima avevano punti d'angolo separati finiscono per condividere gli stessi vertici. Raggruppa i vertici vicini usando la quantizzazione su griglia con una tolleranza basata sul bounding box della mesh e calcola la media dei colori dei vertici per ogni gruppo unito. Questo è utile quando una mesh arriva non saldata, cioè ogni faccia ha i propri vertici e nessun bordo condiviso, e può servire come pre-passaggio prima di operazioni che tengono conto della topologia come FillHoles o DecimateMesh.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh 3D di input i cui vertici coincidenti verranno uniti. | MESH | Sì | - |
| `epsilon_rel` | Tolleranza di saldatura (frazione della diagonale del bounding box). 1e-5 per la deduplicazione dei float; 1e-3 per vertici visivamente vicini ma distinti. Predefinito: 1e-5. | FLOAT | Sì | 0.0 a illimitato (passo 1e-6) |
| `epsilon_abs` | Tolleranza di saldatura assoluta (sostituisce `epsilon_rel` quando > 0). Predefinito: 0.0. | FLOAT | Sì | 0.0 a illimitato (passo 1e-6) |

Nota: quando `epsilon_abs` è maggiore di 0, ha la precedenza su `epsilon_rel` e la tolleranza relativa viene ignorata. Quando `epsilon_abs` è 0, viene utilizzata la tolleranza relativa `epsilon_rel`, convertita in una distanza assoluta moltiplicandola per la diagonale del bounding box della mesh.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `mesh` | La mesh saldata con vertici uniti, indici delle facce aggiornati e colori dei vertici mediati (se la mesh di input aveva colori). | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/it.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
