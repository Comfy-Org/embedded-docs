# Meshy: Texture Model (N1)

Questo nodo applica una texture a un modello 3D creato in precedenza con il modello di texturing Meshy N1, utilizzando da 1 a 4 viste di riferimento dello stesso oggetto. Collega l'ID attività del modello originale insieme alle viste; il nodo le invia a Meshy, attende il completamento del lavoro e restituisce il modello texturizzato come file GLB e FBX insieme al nuovo ID attività.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI utilizzato per il lavoro di texturing. Attualmente è disponibile solo `"meshy-n1"`. | COMBO | Sì | `"meshy-n1"` |
| `meshy_task_id` | ID attività del modello 3D creato in precedenza che deve essere texturizzato. | MESHY_TASK_ID | Sì | N/A |
| `front_view` | La vista che Meshy considera come fronte. Una sola immagine applica la texture al fronte e lascia il retro senza texture; aggiungi viste posteriori e laterali in `extra_views` per ottenere un retro fedele. | IMAGE | Sì | Immagine singola |
| `extra_views` | Ulteriori viste dello stesso oggetto, in qualsiasi ordine. Slot espandibile: collega da 0 a 3 immagini (`view_1` ... `view_3`). Insieme a `front_view`, al massimo 4 immagini. | IMAGE | No | 0 a 3 immagini |
| `enable_original_uv` | Usa gli UV originali del modello invece di generare nuovi UV. Se abilitato, Meshy preserva le texture esistenti del modello caricato. Se il modello non ha UV originali, la qualità dell'output potrebbe non essere altrettanto buona. (predefinito: True; opzione avanzata) | BOOLEAN | No | True / False |

**Nota:** `front_view` e `extra_views` possono contenere insieme al massimo 4 immagini; il nodo genera un errore quando ne vengono collegate di più. Se un'immagine collegata trasporta un batch, ogni immagine del batch concorre a tale limite. La risoluzione della texture è fissa a 2K e non vengono generate mappe PBR.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `meshy_task_id` | ID attività del lavoro di texturing, utilizzabile dai nodi Meshy successivi. | MESHY_TASK_ID |
| `GLB` | Il modello 3D texturizzato scaricato in formato GLB. | FILE3DGLB |
| `FBX` | Il modello 3D texturizzato scaricato in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/it.md)

---
**Source fingerprint (SHA-256):** `808df4f5a32b2d9ca6e74668051409836f2fcbc078d4ee3e85c07121d7a81f76`
