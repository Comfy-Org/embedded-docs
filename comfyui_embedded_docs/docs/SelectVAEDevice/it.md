# Seleziona Dispositivo VAE

## Panoramica

Questo nodo consente di selezionare manualmente il dispositivo GPU su cui deve essere posizionato il modello VAE. Per impostazione predefinita, il VAE viene posizionato sul dispositivo assegnato dal caricatore di modelli, ma è possibile fissarlo a una GPU specifica (ad es. `gpu:0`, `gpu:1`). Se il dispositivo selezionato non è disponibile sulla macchina, il nodo passerà il VAE invariato e registrerà un messaggio anziché fallire.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `vae` | Il modello VAE da assegnare a un dispositivo specifico. | VAE | Sì |  |
| `device` | Il dispositivo di destinazione per il VAE. `"default"` ripristina il dispositivo assegnato dal caricatore. `"gpu:N"` fissa il VAE alla N-esima GPU disponibile. La CPU non è una scelta supportata e verrà ignorata se fornita. (predefinito: `"default"`) | COMBO | Sì | `"default"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `vae` | Il modello VAE, ora assegnato al dispositivo selezionato. Se il dispositivo richiesto non è disponibile o non è valido, il VAE viene passato invariato. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/it.md)

---
**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`
