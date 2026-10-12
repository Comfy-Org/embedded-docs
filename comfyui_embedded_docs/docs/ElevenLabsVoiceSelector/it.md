# Selettore Voce ElevenLabs

Il nodo ElevenLabs Voice Selector consente di scegliere una voce specifica da un elenco predefinito di voci text-to-speech di ElevenLabs. Prende in input un nome di voce e restituisce l'identificatore di voce corrispondente necessario per la generazione audio. Questo nodo semplifica il processo di selezione di una voce compatibile da usare con gli altri nodi audio di ElevenLabs.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `voice` | Scegli una voce tra le voci predefinite di ElevenLabs. | STRING | Sì | `"Adam (male, american)"`<br>`"Antoni (male, british)"`<br>`"Arnold (male, american)"`<br>`"Bella (female, american)"`<br>`"Domi (female, american)"`<br>`"Elli (female, american)"`<br>`"Josh (male, american)"`<br>`"Rachel (female, american)"`<br>`"Sam (male, american)"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `voice` | L'identificatore univoco della voce ElevenLabs selezionata, che può essere passato ad altri nodi per la generazione text-to-speech. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/it.md)

---
**Source fingerprint (SHA-256):** `72e2239bb0da15a88cd346ede2051b4fb717f3bf49faaf5d63c0622b03ccd80d`
