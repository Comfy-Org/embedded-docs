# SplatToFile3D

Il nodo SplatToFile3D converte uno splat gaussiano in un oggetto File3D che può essere utilizzato con i nodi Save o Preview 3D. Supporta un solo elemento per batch e consente di scegliere tra diversi formati di file di output per i dati 3D esportati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `splat` | I dati dello splat gaussiano da serializzare in un file | SPLAT | Sì | - |
| `format` | Il formato del file di output per il file 3D (predefinito: "ply"). ply: Gaussian Splat 3D standard con armoniche sferiche complete. ksplat: mkkellogg SplatBuffer (livello 0, non compresso), solo colore di base. spz: Niantic compresso con gzip (circa 10 volte più piccolo), solo colore di base | COMBO | Sì | "ply"<br>"ksplat"<br>"spz" |

Nota: questo nodo supporta un solo elemento per batch. Se lo splat gaussiano di input contiene più di un elemento nel batch, il nodo registra un avviso e utilizza il primo elemento. Se viene fornito un formato non supportato, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model_3d` | Un oggetto File3D contenente i dati dello splat gaussiano serializzati nel formato selezionato, pronti per il salvataggio o l'anteprima | FILE3D |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/it.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
