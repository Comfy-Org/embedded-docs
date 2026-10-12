# LTXVAudioVAEDecode

Il nodo LTXV Audio VAE Decode converte una rappresentazione latente di un audio in una forma d'onda audio. Utilizza un modello Audio VAE specializzato per eseguire questo processo di decodifica, producendo un output audio con la relativa frequenza di campionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | Il latente da decodificare. | LATENT | Sì | N/A |
| `audio_vae` | Il modello Audio VAE utilizzato per decodificare il latente. | VAE | Sì | N/A |

**Nota:** Se il latente fornito è annidato (contiene più latenti), il nodo utilizza automaticamente l'ultimo latente della sequenza per la decodifica.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `Audio` | La forma d'onda audio decodificata e la relativa frequenza di campionamento. La forma d'onda viene collocata sullo stesso dispositivo del latente di input, e la frequenza di campionamento è determinata dal modello Audio VAE. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/it.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
