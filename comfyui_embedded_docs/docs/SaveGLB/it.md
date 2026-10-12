# Salva Modello 3D

Il nodo SaveGLB salva dati mesh 3D o input di file 3D nella directory di output. Accetta dati mesh e comuni formati di file 3D (GLB, GLTF, OBJ, FBX, STL, USDZ, PLY, SPLAT, SPZ, KSPLAT) e li esporta con il prefisso del nome file specificato. Gli input mesh vengono scritti come file GLB, uno per ogni elemento del batch, mentre gli input di file 3D vengono salvati nel loro formato originale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | Mesh o file 3D da salvare | MESH o FILE3D | Sì | Dati mesh<br>GLB<br>GLTF<br>OBJ<br>FBX<br>STL<br>USDZ<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT<br>Qualsiasi formato splat<br>Qualsiasi formato point cloud<br>Qualsiasi formato di file 3D |
| `filename_prefix` | Il prefisso per il nome file di output (predefinito: "3d/ComfyUI"). Il prefisso può includere un percorso di sottocartella, quindi per impostazione predefinita i file vengono salvati nella sottocartella "3d" della directory di output | STRING | No | - |

Nota: quando l'input `mesh` è un file 3D, il nodo lo salva usando l'estensione del suo formato originale (viene usato GLB se il file non ha un formato). Quando sono dati mesh, ogni elemento nel batch viene salvato come file `.glb` separato; gli elementi vuoti (senza vertici o facce) vengono saltati con un avviso. I nomi file di output seguono il pattern `{filename_prefix}_{counter:05}_.{ext}` con un contatore incrementale. I metadati del workflow (prompt e informazioni PNG extra) vengono incorporati nei file salvati quando i metadati sono abilitati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `ui` | Visualizza i file 3D salvati nell'interfaccia utente con informazioni su nome file, sottocartella e tipo | UI |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/it.md)

---
**Source fingerprint (SHA-256):** `366b56c4fd6e3c2f7783222990792a982857b3419a2becfa27ddfa37853bb22c`
