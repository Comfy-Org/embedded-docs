# SoniloTextToMusic

Il nodo Sonilo Text to Music genera musica da una descrizione testuale utilizzando il modello AI di Sonilo. Fornisci un prompt che descrive la musica desiderata e il nodo invia una richiesta al servizio Sonilo per creare un file audio. Puoi impostare una durata target per il clip generato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale che descrive la musica da generare. Deve contenere da 1 a 1000 caratteri dopo la rimozione degli spazi bianchi. | STRING | Sì | 1 a 1000 caratteri |
| `duration` | Durata target in secondi. Massimo: 6 minuti. Predefinito: 30. | INT | No | 1 a 360 |
| `seed` | Seed per la riproducibilità. Attualmente ignorato dal servizio Sonilo ma mantenuto per coerenza del grafo. Predefinito: 0. | INT | No | 0 a 18446744073709551615 |

**Note:**
- L'input `seed` è fornito per coerenza del flusso di lavoro ma attualmente non influisce sull'output del servizio Sonilo.
- L'input `prompt` è obbligatorio e non deve essere vuoto; il nodo verifica che contenga almeno 1 carattere (dopo la rimozione degli spazi bianchi) e non più di 1000 caratteri.
- L'utilizzo viene fatturato a $0.0025 per secondo della `duration` richiesta.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `audio` | La musica generata come file audio. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/it.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
