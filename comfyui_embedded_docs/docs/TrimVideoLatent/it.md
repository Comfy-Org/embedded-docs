# Taglia Latent Video

Il nodo TrimVideoLatent rimuove i frame dall'inizio di una rappresentazione latente video. Prende un campione video latente e taglia un numero specificato di frame dall'inizio, restituendo la porzione rimanente del video. Ciò consente di accorciare le sequenze video rimuovendo i frame iniziali.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `samples` | La rappresentazione latente video di input contenente i frame video da tagliare | LATENT | Sì | - |
| `trim_amount` | Il numero di frame da rimuovere dall'inizio del video (predefinito: 0) | INT | Sì | 0 to 99999 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | La rappresentazione latente video tagliata con il numero specificato di frame rimossi dall'inizio | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/it.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
