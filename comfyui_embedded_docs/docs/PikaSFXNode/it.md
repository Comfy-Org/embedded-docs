# Pika SFX

Questo nodo genera un effetto sonoro a partire da una descrizione testuale con Pika. Descrivi il suono e la sua durata; il nodo restituisce una clip audio.

## Ingressi

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | L'effetto sonoro desiderato. Non deve essere vuoto. Predefinito: "" (stringa vuota). | STRING | Sì | da 1 a 4000 caratteri |
| `duration` | Durata dell'effetto sonoro in secondi. Predefinito: 5.0. | FLOAT | Sì | da 1.0 a 20.0 (passo: 0.1) |
| `seed` | Seme per il campionamento. Predefinito: 42. | INT | Sì | da 0 a 2147483647 |

## Uscite

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `AUDIO` | L'effetto sonoro generato. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSFXNode/it.md)

---
**Source fingerprint (SHA-256):** `a1dcd374d158009aceae2aecd87ed08f8105bff7db75160a99e8624be9459dfa`
