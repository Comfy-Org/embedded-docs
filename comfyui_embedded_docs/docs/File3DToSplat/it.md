# Ottieni Splat

Questo nodo converte un file 3D contenente dati gaussian splat in un formato gaussian splat utilizzabile nel grafo dei nodi. Supporta i formati di file PLY, SPLAT, KSPLAT e SPZ, con il formato del file rilevato automaticamente dal contenuto del file.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Un file 3D di gaussian splat | FILE3D | Sì | - |

Il file di input deve essere in uno dei formati supportati: PLY, SPLAT, KSPLAT o SPZ. I file PLY contengono dati completi delle armoniche sferiche, mentre gli altri formati contengono solo informazioni sul colore di base. Il formato viene rilevato automaticamente dal contenuto del file.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `splat` | Un gaussian splat contenente dati di posizione, scala, rotazione, opacità e armoniche sferiche | SPLAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/File3DToSplat/it.md)

---
**Source fingerprint (SHA-256):** `9f45210a1366e57a91de6e1251f0e2e09f39e6498dbec1db7bf9826ebedd167b`
