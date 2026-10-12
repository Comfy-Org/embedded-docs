# SeedVR2Conditioning

Costruisce il condizionamento positivo e negativo da un latente VAE da utilizzare con il modello SeedVR2. Convalida la struttura del latente e del modello in input, aggiunge un canale di maschera al latente e restituisce entrambi gli output di condizionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello SeedVR2. | MODEL | Sì | - |
| `vae_conditioning` | Il latente VAE di SeedVR2 da cui costruire il condizionamento (nome visualizzato: latent). | LATENT | Sì | - |

Nota: il latente `vae_conditioning` deve essere un tensore 5-D nel layout channel-first di Comfy (B, C, T, H, W), dove C è il numero di canali previsto per il VAE SeedVR2. Il nodo genera un errore se il latente non è 5-D, se il numero di canali non corrisponde o se il tensore sembra essere in layout channel-last. L'input `model` deve avere la struttura SeedVR2 prevista; il nodo risolve il suo modello di diffusione interno e legge il suo condizionamento positivo e negativo. Internamente, il nodo aggiunge un canale di maschera costante al latente e collega il condizionamento risultante a entrambi gli output di condizionamento `positive` e `negative`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | Il condizionamento positivo per il campionamento. | CONDITIONING |
| `negative` | Il condizionamento negativo per il campionamento. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
