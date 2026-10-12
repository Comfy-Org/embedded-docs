# ModelMergeAuraflow

Il nodo ModelMergeAuraflow combina due modelli Auraflow assegnando un peso di miscelazione separato a ciascuna parte del modello, dai layer iniziali fino all'output finale. Ogni peso controlla quanto del secondo modello viene miscelato nel primo modello in quella specifica componente, offrendo un controllo preciso sull'unione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `init_x_linear.` | Peso di miscelazione per la trasformazione lineare iniziale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `positional_encoding` | Peso di miscelazione per i componenti di codifica posizionale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `cond_seq_linear.` | Peso di miscelazione per i layer lineari della sequenza condizionale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `register_tokens` | Peso di miscelazione per i componenti di registrazione dei token (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `t_embedder.` | Peso di miscelazione per i componenti di embedding temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `double_layers.0.` | Peso di miscelazione per il gruppo di layer doppi 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `double_layers.1.` | Peso di miscelazione per il gruppo di layer doppi 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `double_layers.2.` | Peso di miscelazione per il gruppo di layer doppi 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `double_layers.3.` | Peso di miscelazione per il gruppo di layer doppi 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.0.` | Peso di miscelazione per il layer singolo 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.1.` | Peso di miscelazione per il layer singolo 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.2.` | Peso di miscelazione per il layer singolo 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.3.` | Peso di miscelazione per il layer singolo 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.4.` | Peso di miscelazione per il layer singolo 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.5.` | Peso di miscelazione per il layer singolo 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.6.` | Peso di miscelazione per il layer singolo 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.7.` | Peso di miscelazione per il layer singolo 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.8.` | Peso di miscelazione per il layer singolo 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.9.` | Peso di miscelazione per il layer singolo 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.10.` | Peso di miscelazione per il layer singolo 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.11.` | Peso di miscelazione per il layer singolo 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.12.` | Peso di miscelazione per il layer singolo 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.13.` | Peso di miscelazione per il layer singolo 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.14.` | Peso di miscelazione per il layer singolo 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.15.` | Peso di miscelazione per il layer singolo 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.16.` | Peso di miscelazione per il layer singolo 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.17.` | Peso di miscelazione per il layer singolo 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.18.` | Peso di miscelazione per il layer singolo 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.19.` | Peso di miscelazione per il layer singolo 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.20.` | Peso di miscelazione per il layer singolo 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.21.` | Peso di miscelazione per il layer singolo 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.22.` | Peso di miscelazione per il layer singolo 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.23.` | Peso di miscelazione per il layer singolo 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.24.` | Peso di miscelazione per il layer singolo 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.25.` | Peso di miscelazione per il layer singolo 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.26.` | Peso di miscelazione per il layer singolo 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.27.` | Peso di miscelazione per il layer singolo 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.28.` | Peso di miscelazione per il layer singolo 28 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.29.` | Peso di miscelazione per il layer singolo 29 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.30.` | Peso di miscelazione per il layer singolo 30 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `single_layers.31.` | Peso di miscelazione per il layer singolo 31 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `modF.` | Peso di miscelazione per i componenti modF (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `final_linear.` | Peso di miscelazione per la trasformazione lineare finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

Tutti i pesi di miscelazione sono valori FLOAT con valore predefinito 1.0, minimo 0.0, massimo 1.0 e passo 0.01.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello unito che combina le caratteristiche di entrambi i modelli di input in base ai pesi di miscelazione specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/it.md)

---
**Source fingerprint (SHA-256):** `e9d3d81b2a3f81b082f9dc9f662f4e51df66f1f077e2899a1fea9a7061c4a97b`
