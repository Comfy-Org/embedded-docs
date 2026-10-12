# RecordAudio

Il nodo RecordAudio carica file audio registrati o selezionati tramite l'interfaccia di registrazione audio. Elabora il file audio e lo converte in un formato waveform utilizzabile da altri nodi di elaborazione audio nel workflow. Il nodo rileva automaticamente la frequenza di campionamento e prepara i dati audio per ulteriori manipolazioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | L'input della registrazione audio dall'interfaccia di registrazione audio | AUDIO_RECORD | Sì | N/A |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `AUDIO` | I dati audio elaborati contenenti informazioni sulla forma d'onda e sulla frequenza di campionamento | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/it.md)

---
**Source fingerprint (SHA-256):** `ca4dde492ecc4f57fcf87b022162692e3123ee90cce51186433ff8f14f606b70`
