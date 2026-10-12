# Codifica VAE Audio

Il nodo VAE Encode Audio converte i dati audio in una rappresentazione latente usando un Autoencoder Variazionale (VAE). Elabora l'audio in ingresso attraverso il VAE per produrre campioni latenti compressi che possono essere usati per ulteriori attività di generazione o manipolazione audio. Se la frequenza di campionamento dell'audio differisce da quella prevista dal VAE, l'audio viene ricampionato automaticamente prima della codifica.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | I dati audio da codificare, contenenti informazioni sulla forma d'onda e sulla frequenza di campionamento | AUDIO | Sì | - |
| `vae` | Il modello Autoencoder Variazionale usato per codificare l'audio nello spazio latente | VAE | Sì | - |

**Nota:** L'input audio viene ricampionato automaticamente per corrispondere alla frequenza di campionamento prevista dal VAE (predefinita: 44100 Hz) se la frequenza di campionamento originale differisce da questo valore. Se l'audio di input è None (ad esempio, quando il video di origine non ha una traccia audio), il nodo genererà un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `LATENT` | La rappresentazione audio codificata nello spazio latente, contenente campioni compressi | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/it.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`
