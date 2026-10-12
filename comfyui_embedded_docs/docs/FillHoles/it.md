# Riempi buchi

Questo nodo riempie i buchi in una mesh 3D rilevando i bordi di confine aperti e creando nuove facce per chiuderli. Viene eseguito sulla GPU, preserva la geometria e gli UV esistenti e può elaborare mesh singole, elenchi di mesh o batch di mesh.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh 3D da elaborare. Accetta una mesh singola, un elenco di mesh o una mesh in batch. | MESH | Sì | - |
| `max_perimeter` | Perimetro massimo del buco da riempire. 0 disabilita. (predefinito: 0.03) | FLOAT | Sì | da 0.0 a nessun limite superiore (passo 0.0001) |
| `weld_epsilon_rel` | Tolleranza di pre-saldatura (frazione della diagonale del bounding box); il rilevamento dei bordi richiede vertici saldati. 0 salta questa fase. (predefinito: 1e-5) | FLOAT | Sì | da 0.0 a nessun limite superiore (passo 1e-6) |
| `max_vertices` | Limita i vertici di confine per ciclo; il ventaglio dal centroide funziona solo per buchi piccoli e quasi planari. Mantieni ≤16. (predefinito: 16) | INT | Sì | da 3 a 1024 |
| `fill_chains` | Riempie anche catene aperte (non solo cicli). Può generare risultati rumorosi; OFF corrisponde a cumesh. (predefinito: False) | BOOLEAN | Sì | True o False |

Nota: quando `max_perimeter` è maggiore di 0, il nodo riempie i buchi; quando è 0, il riempimento dei buchi viene saltato del tutto. Quando `weld_epsilon_rel` è maggiore di 0, il nodo pre-salda i vertici duplicati prima di rilevare i buchi. La tolleranza di saldatura parte dalla frazione indicata della diagonale del bounding box e aumenta automaticamente raddoppiando finché la mesh non viene considerata saldata o la tolleranza raggiunge un limite massimo di 1e-2. I buchi con più di 8 vertici di confine usano un riempimento a ventaglio dal centroide (inserendo un nuovo vertice centroide), mentre i buchi più piccoli usano un riempimento a ventaglio dal vertice che riutilizza un vertice di confine esistente. Per impostazione predefinita vengono riempiti solo i cicli di confine chiusi; imposta `fill_chains` su True per chiudere anche le catene aperte.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `mesh` | La mesh con i buchi riempiti, corrispondente al formato batch di input. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/it.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
