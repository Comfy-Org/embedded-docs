# FreSca

Il nodo FreSca applica uno scaling dipendente dalla frequenza alla guida durante il processo di campionamento. Separa il segnale di guida in componenti a bassa frequenza e ad alta frequenza usando il filtraggio di Fourier, quindi applica fattori di scala diversi a ciascun intervallo di frequenza prima di ricombinarli. Ciò consente un controllo più sfumato su come la guida influisce su aspetti diversi dell'output generato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare lo scaling di frequenza | MODEL | Sì | - |
| `scale_low` | Fattore di scala per le componenti a bassa frequenza (predefinito: 1.0) | FLOAT | No | 0 - 10 |
| `scale_high` | Fattore di scala per le componenti ad alta frequenza (predefinito: 1.25) | FLOAT | No | 0 - 10 |
| `freq_cutoff` | Numero di indici di frequenza attorno al centro da considerare a bassa frequenza (predefinito: 20) | INT | No | 1 - 10000 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con scaling dipendente dalla frequenza applicato alla sua funzione di guida | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/it.md)

---
**Source fingerprint (SHA-256):** `2ff3517619d856db68a9091ae7c87af8c56a23420fa2176b089bf9700475a7a9`
