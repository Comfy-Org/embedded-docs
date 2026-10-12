# ByteDanceCreateVideoAsset

Questo nodo crea un asset video personale per Seedance 2.0. Carica il video di input e lo registra all'interno di uno specifico gruppo di asset. Se non fornisci un ID gruppo, ti guiderà attraverso un processo di verifica dell'identità della persona reale nel browser per creare prima un nuovo gruppo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Video da registrare come asset personale. | VIDEO | Sì | - |
| `group_id` | Riutilizza l'ID di un gruppo di asset Seedance esistente per saltare la verifica umana ripetuta per la stessa persona. Lascia vuoto per eseguire l'autenticazione della persona reale nel browser e creare un nuovo gruppo. (predefinito: stringa vuota) | STRING | No | - |

**Vincoli del video:**
- **Durata:** Deve essere compresa tra 2 e 15 secondi.
- **Dimensioni:** Larghezza e altezza devono essere ciascuna comprese tra 300 e 6000 pixel.
- **Rapporto d'aspetto:** Il rapporto larghezza-altezza deve essere compreso tra 0.4 e 2.5.
- **Pixel totali:** Il numero totale di pixel (larghezza × altezza) deve essere compreso tra 409.600 e 927.408.
- **Frequenza fotogrammi:** Deve essere compresa tra 24 e 60 fotogrammi al secondo (FPS).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `asset_id` | L'identificatore univoco per il nuovo asset video creato. | STRING |
| `group_id` | L'identificatore del gruppo di asset che contiene il nuovo video. Sarà il `group_id` fornito oppure uno appena creato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/it.md)

---
**Source fingerprint (SHA-256):** `2c7376185f3273a80c763c2c9bd41305575b58e7902200ff77bebb609aea58b8`
