# ByteDance Seed Audio 1.0

Genera parlato, musica, effetti sonori e dialoghi multi-speaker da un singolo prompt con ByteDance Seed Audio 1.0. Descrivi la/le voce/i, l'emozione, il ritmo, l'ambiente, la musica di sottofondo e gli effetti sonori nel prompt, e includi le battute da pronunciare. Opzionalmente seleziona una voce predefinita integrata, clona voci da un massimo di 3 clip di riferimento (contrassegnate come @Audio1-3 nel prompt), oppure deriva una voce da un'immagine di un personaggio. Fino a 2 minuti di audio per esecuzione. Il modello multilingue supporta 20 lingue e il controllo temporale basato su timestamp.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `text_prompt` | Descrivi la/le voce/i, l'emozione, il ritmo, l'ambiente, la musica di sottofondo e gli effetti sonori, e includi le battute da pronunciare (nomina i personaggi inline per i dialoghi). In modalità "audio reference", fai riferimento alle clip collegate in ordine come @Audio1, @Audio2, @Audio3. Con il modello multilingue, una riga tra virgolette può iniziare con un intervallo di timestamp che controlla quando e per quanto tempo viene pronunciata, ad es. `[5.5s:8.0s] Aspettami!`. Scrivi il prompt nella stessa lingua delle battute da pronunciare. Minimo 1 carattere, massimo 3000 caratteri. | STRING | Sì | da 1 a 3000 caratteri |
| `reference_mode` | Come condizionare la voce: "text only" (descrivi tutto nel prompt), "audio reference" (clona fino a 3 voci, contrassegnate @Audio1-3), "image reference" (deriva una voce da un'immagine di un personaggio), o "preset voice" (seleziona una voce predefinita con nome che legge il prompt). | COMBO | Sì | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | Clip di riferimento per il voice cloning, contrassegnata come @Audio1 nel prompt. Fino a 30s. Disponibile solo quando `reference_mode` è "audio reference". | AUDIO | No | Fino a 30 secondi |
| `reference_audio_2` | Clip di riferimento contrassegnata come @Audio2 nel prompt. Fino a 30s. Disponibile solo quando `reference_mode` è "audio reference". | AUDIO | No | Fino a 30 secondi |
| `reference_audio_3` | Clip di riferimento contrassegnata come @Audio3 nel prompt. Fino a 30s. Disponibile solo quando `reference_mode` è "audio reference". | AUDIO | No | Fino a 30 secondi |
| `reference_image` | Una singola immagine di un personaggio; il modello ne deriva una voce. Non può essere combinata con audio di riferimento. Disponibile solo quando `reference_mode` è "image reference". | IMAGE | No | - |
| `preset_voice` | Una voce TTS 2.0 integrata che legge il prompt. Nessuna clip di riferimento necessaria, e i tag @AudioN non vengono utilizzati in questa modalità. Obbligatorio quando `reference_mode` è "preset voice". | COMBO | No | Molteplici opzioni di voce predefinita integrata (prima opzione selezionata di default) |
| `sample_rate` | Frequenza di campionamento in uscita in Hz. (default: "24000") | COMBO | Sì | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Velocità di parlata. 0 = normale, 100 = 2.0x, -50 = 0.5x. (default: 0) | INT | Sì | da -50 a 100 |
| `loudness_rate` | Volume. 0 = normale, 100 = 2.0x, -50 = 0.5x. (default: 0) | INT | Sì | da -50 a 100 |
| `pitch_rate` | Spostamento di intonazione in semitoni (-12 a 12). (default: 0) | INT | Sì | da -12 a 12 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. (default: 42) | INT | Sì | da 0 a 2147483647 |
| `model` | Versione del modello. `seed-audio-1.0-multilingual` supporta 20 lingue e il controllo temporale per frase tramite timestamp `[5.5s:8.0s]`. `seed-audio-1.0` supporta solo inglese e cinese, senza controllo temporale. (default: "seed-audio-1.0-multilingual") | COMBO | No | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Vincoli dei parametri

- **Dipendenze della modalità di riferimento**: Il parametro `reference_mode` determina quali altri input sono richiesti:
  - **"text only"**: Nessun input aggiuntivo richiesto. Il prompt non deve contenere tag @AudioN.
  - **"audio reference"**: Richiede che almeno uno tra `reference_audio_1`, `reference_audio_2`, o `reference_audio_3` sia collegato. Le clip di riferimento devono essere collegate in ordine senza interruzioni. Ogni clip è limitata a una durata massima di 30 secondi. Se nel prompt vengono usati tag @AudioN, il numero di tag più alto non deve superare il numero di clip di riferimento collegate.
  - **"image reference"**: Richiede che `reference_image` sia collegato. I tag @AudioN non vengono usati; il prompt deve contenere solo il testo da sintetizzare.
  - **"preset voice"**: Richiede che venga selezionata una voce predefinita. L'intero prompt viene letto con la voce selezionata; i tag @AudioN non vengono usati come riferimenti, e tag come @Audio2 o superiori vengono rifiutati.

- **Ordinamento dei riferimenti audio**: In modalità "audio reference", gli input audio di riferimento devono essere collegati in sequenza partendo da `reference_audio_1` senza interruzioni. Ad esempio, puoi collegare `reference_audio_1` e `reference_audio_2`, ma non `reference_audio_1` e `reference_audio_3` senza `reference_audio_2`.

- **Numero massimo di tag audio**: In modalità "audio reference", è possibile collegare fino a 3 clip di riferimento (@Audio1, @Audio2, @Audio3), e il tag @AudioN più alto nel prompt non può superare il numero di input audio di riferimento collegati.

- **Differenze tra modelli**: Il modello `seed-audio-1.0-multilingual` supporta 20 lingue (inglese, cinese, giapponese, coreano, spagnolo messicano e castigliano, indonesiano, tedesco, portoghese brasiliano, francese, thailandese, vietnamita, malese, filippino, italiano, russo, olandese, polacco, turco, svedese) più il controllo temporale per frase usando timestamp nel formato `[5.5s:8.0s]`. Il modello `seed-audio-1.0` supporta solo inglese e cinese, senza controllo temporale.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `AUDIO` | L'output audio generato da ByteDance Seed Audio 1.0, contenente parlato, musica, effetti sonori o dialoghi multi-speaker come descritto nel prompt. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/it.md)

---
**Source fingerprint (SHA-256):** `e86e4edde424b4427d864350a9d3b082e271fbd2b1e335175637a9cc3ad51163`
