# Fusione Latent

Il nodo LatentBlend combina due campioni latenti miscelandoli insieme utilizzando un fattore di miscelazione specificato. Prende due input latenti e crea un nuovo output in cui il primo campione è ponderato in base al fattore di miscelazione e il secondo campione è ponderato in base all'inverso. Se i campioni di input hanno forme diverse, il secondo campione viene ridimensionato automaticamente per corrispondere alle dimensioni del primo campione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples1` | Il primo campione latente da miscelare | LATENT | Sì | - |
| `samples2` | Il secondo campione latente da miscelare | LATENT | Sì | - |
| `blend_factor` | Controlla il rapporto di miscelazione tra i due campioni (predefinito: 0.5) | FLOAT | Sì | 0 to 1 |

**Nota:** Se `samples1` e `samples2` hanno forme diverse, `samples2` verrà ridimensionato automaticamente per corrispondere alle dimensioni di `samples1` usando l'interpolazione bicubica con ritaglio centrale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | Il campione latente miscelato che combina entrambi i campioni di input | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/it.md)

---
**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`
