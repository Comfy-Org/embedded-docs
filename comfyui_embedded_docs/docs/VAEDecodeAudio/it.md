# Decodifica audio VAE

Questo nodo converte una rappresentazione latente audio in una forma d'onda audio riproducibile utilizzando un autoencoder variazionale (VAE). Prende i campioni codificati, li decodifica tramite il VAE selezionato e poi normalizza la forma d'onda risultante in modo che il livello di volume complessivo rimanga coerente. L'audio in output utilizza la frequenza di campionamento audio del VAE (44100 Hz per impostazione predefinita), oppure la frequenza di campionamento memorizzata nei campioni di input quando presente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `samples` | I campioni audio codificati nello spazio latente che verranno decodificati in una forma d'onda audio. Se i campioni contengono una propria frequenza di campionamento, viene utilizzato quel valore per l'output. | LATENT | Sì | - |
| `vae` | Il modello autoencoder variazionale utilizzato per decodificare i campioni latenti in audio. La sua frequenza di campionamento audio in output (predefinita 44100 Hz) determina la frequenza di campionamento della forma d'onda risultante quando i campioni di input non ne specificano una. | VAE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `AUDIO` | La forma d'onda audio decodificata con volume normalizzato, restituita insieme alla sua frequenza di campionamento (la frequenza di campionamento dei `samples` di input, se presente, altrimenti la frequenza di campionamento audio del VAE, predefinita 44100 Hz). | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/it.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
