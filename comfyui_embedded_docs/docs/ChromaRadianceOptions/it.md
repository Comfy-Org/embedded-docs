# ChromaRadianceOptions

Il nodo ChromaRadianceOptions consente di configurare impostazioni avanzate per il modello Chroma Radiance. Collega un wrapper a un modello esistente e applica le opzioni selezionate durante il processo di denoising solo quando il valore sigma corrente rientra nell'intervallo configurato, offrendo controllo sulla dimensione dei tile NeRF e sulla gestione degli ID dei token di testo.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello a cui applicare le opzioni Chroma Radiance | MODEL | Sì | - |
| `preserve_wrapper` | Se abilitato, delega a un wrapper di funzione del modello esistente, se presente. In genere dovrebbe essere lasciato abilitato. (predefinito: True) | BOOLEAN | No | - |
| `start_sigma` | Primo sigma in cui queste opzioni saranno attive. (predefinito: 1.0) | FLOAT | No | da 0.0 a 1.0 |
| `end_sigma` | Ultimo sigma in cui queste opzioni saranno attive. (predefinito: 0.0) | FLOAT | No | da 0.0 a 1.0 |
| `nerf_tile_size` | Consente di sovrascrivere la dimensione tile NeRF predefinita. -1 significa usare il valore predefinito (32). 0 significa usare la modalità senza tiling (potrebbe richiedere molta VRAM). (predefinito: -1) | INT | No | -1 e superiori |
| `force_sequential_txt_ids` | Forza l'uso di ID sequenziali dei token di testo invece di zeri. Dovrebbe essere usato per checkpoint dal 2026-05-22 al 2026-06-01 addestrati in questo modo ma che non contengono la chiave __sequential__ nello state dict. (predefinito: False) | BOOLEAN | No | - |

**Nota:** Le opzioni Chroma Radiance hanno effetto solo quando il valore sigma corrente rientra tra `end_sigma` e `start_sigma` (inclusi). L'opzione `nerf_tile_size` viene applicata solo se impostata a 0 o a un valore superiore (un valore di -1 usa la dimensione tile predefinita di 32 e non memorizza alcuna sovrascrittura). L'opzione `force_sequential_txt_ids` viene applicata solo se impostata a True. Quando `nerf_tile_size` è -1 e `force_sequential_txt_ids` è False, non viene configurata alcuna opzione e il modello viene restituito invariato senza alcun wrapper applicato.

**Nota:** Tutti gli input diversi da `model` sono opzioni avanzate.

## Output
| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model` | Il modello con le opzioni Chroma Radiance applicate, oppure il modello invariato se nessuna opzione è attiva | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/it.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
