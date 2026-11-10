# LTX Video AlphaGen

Estrae una matte alpha in scala di grigi, bianca per il primo piano, che corrisponde al video di input fotogramma per fotogramma. Invia la matte a Get Video Components e Image To Mask per trasformarla in una maschera. L'audio non viene conservato.

## Ingressi

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video da convertire in matte, fino a 10 secondi e 3840x2160 in entrambi gli orientamenti. | VIDEO | Sì | - |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 4294967295 |

## Uscite

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `matte` | La matte alpha come video, un fotogramma per ogni fotogramma di input e senza audio. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/it.md)

---
**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`
