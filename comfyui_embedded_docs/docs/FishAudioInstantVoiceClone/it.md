# Clonazione vocale istantanea Fish Audio

Questo nodo crea una voce clonata privata dalle tue registrazioni audio utilizzando l'API Fish Audio. Fornisci uno o più campioni audio e il nodo crea una voce personalizzata che può essere utilizzata immediatamente per la sintesi vocale. Accetta da 1 a 20 registrazioni, con una durata consigliata da 10 a 30 secondi ciascuna e un limite totale di 270 secondi.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `files` | Registrazioni audio per la clonazione vocale. Questo è un input espandibile: collega uno o più elementi audio (ad esempio `audio_1`, `audio_2`, ...) per fornire i campioni vocali. | AUDIO | Sì | Da 1 a 20 registrazioni |
| `enhance_audio_quality` | Migliora la qualità dell'audio di riferimento prima dell'addestramento (predefinito: True). | BOOLEAN | Sì | True<br>False |

**Nota:** La durata totale di tutto l'audio di riferimento combinato deve essere inferiore a 270 secondi. Se la durata combinata raggiunge o supera i 270 secondi, il nodo restituisce un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `voice` | La voce clonata appena creata, identificata da un ID voce univoco restituito dall'API Fish Audio. Questa voce può essere utilizzata per la sintesi vocale. | FISHAUDIO_VOICE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/it.md)

---
**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`
