# ElevenLabs Testo in Effetti Sonori

Il nodo ElevenLabs Text to Sound Effects genera effetti sonori audio a partire da una descrizione testuale. Utilizza l'API ElevenLabs per creare effetti sonori basati sul tuo prompt, consentendoti di controllare la durata, il comportamento di loop e quanto fedelmente il suono segue il testo.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da usare per la generazione degli effetti sonori. Sono disponibili due modelli: `eleven_sfx_v3` (predefinito) ed `eleven_sfx_v2`. | DYNAMIC_COMBO | Sì | `"eleven_sfx_v3"`<br>`"eleven_sfx_v2"` |
| `text` | Descrizione testuale dell’effetto sonoro da generare. Scrivila in inglese, con un massimo di 450 caratteri; i prompt in altre lingue vengono spesso letti ad alta voce invece di diventare un suono. (predefinito: vuoto) | STRING | Sì | da 1 a 450 caratteri |
| `output_format` | Formato di output audio. | COMBO | Sì | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Input di eleven_sfx_v3 e eleven_sfx_v2

Questi parametri vengono mostrati quando è selezionato uno dei due modelli; entrambi usano le stesse impostazioni.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `duration` | Durata del suono generato in secondi. (predefinito: 5.0) | FLOAT | Sì | 0.5 a 30.0 |
| `loop` | Crea un effetto sonoro con loop fluido. (predefinito: False) | BOOLEAN | No | True<br>False |
| `prompt_influence` | Quanto fedelmente la generazione segue il prompt. Valori più alti fanno sì che il suono segua più fedelmente il testo. (predefinito: 0.3) | FLOAT | Sì | 0.0 a 1.0 |

**Nota:** Il parametro `text` deve contenere da 1 a 450 caratteri; viene validato prima che venga inviata la richiesta di generazione del suono.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `audio` | Il file audio dell'effetto sonoro generato. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/it.md)

---
**Source fingerprint (SHA-256):** `bf7735aed642b2d795a18f7ca2631cab6856a2e0980f4c9e7a8699f08784177c`
