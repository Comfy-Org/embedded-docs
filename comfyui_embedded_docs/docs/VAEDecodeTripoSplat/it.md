# Decodifica TripoSplat

Decodifica una rappresentazione latente TripoSplat in uno splat gaussiano 3D. Questo nodo prende il latente campionato da un modello TripoSplat e lo ricostruisce come un insieme di gaussiane 3D, la cui densità può essere regolata modificando il numero di gaussiane prodotte.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `samples` | I campioni latenti da decodificare. Se i campioni contengono un flusso camera annidato insieme al latente, viene decodificato solo il flusso latente. | LATENT | Sì | - |
| `vae` | Decoder VAE di TripoSplat | VAE | Sì | - |
| `num_gaussians` | Numero di gaussiane da produrre (arrotondato a un multiplo di 32). 262144 corrisponde alla densità dei punti dell'octree; valori più alti sovracampionano gli stessi punti (più denso, ma senza nuovi dettagli) e costano proporzionalmente più VRAM/tempo. Predefinito: 262144 | INT | Sì | da 32 a 1048576 (passo: 32) |
| `seed` | Imposta il seme del campionatore di punti dell'octree (RNG globale) per decodifiche deterministiche. Predefinito: 0 | INT | Sì | da 0 a 18446744073709551615 |

**Nota:** Il valore di `num_gaussians` viene automaticamente limitato all'intervallo consentito e arrotondato a un multiplo dell'impostazione gaussiane per punto del decoder VAE. Il numero effettivo utilizzato può differire leggermente dal valore inserito.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `splat` | Lo splat gaussiano 3D decodificato contenente posizioni, scale, rotazioni, opacità e coefficienti delle armoniche sferiche | SPLAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/it.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
