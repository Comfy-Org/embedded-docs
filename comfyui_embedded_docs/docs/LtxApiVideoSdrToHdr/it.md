# LTX Video SDR to HDR

Converte un video SDR in un video HDR a 10 bit in BT.2020 con funzione di trasferimento HLG, alla stessa risoluzione. L'audio non viene conservato.

## Ingressi

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video SDR da convertire, al massimo 3840x2160 in entrambi gli orientamenti. Fino a 273 fotogrammi a 1080p, 193 fotogrammi a 1440p e 65 fotogrammi a 4K. | VIDEO | Sì | - |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 4294967295 |

## Uscite

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video HDR a 10 bit convertito, senza audio. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoSdrToHdr/it.md)

---
**Source fingerprint (SHA-256):** `e5c0ef901f504a9477f042b4aef24935f4b85da52ccfaddfc764e9efec490915`
