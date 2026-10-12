# TextEncodeAceStepAudio1.5

Der Node TextEncodeAceStepAudio1.5 bereitet Text- und audiobezogene Metadaten für die Verwendung mit dem AceStepAudio 1.5-Modell vor. Er nimmt beschreibende Tags, Liedtexte und musikalische Parameter entgegen und verwendet dann ein CLIP-Modell, um sie in ein Conditioning-Format umzuwandeln, das für die Audiogenerierung geeignet ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das zum Tokenisieren und Codieren des Eingabetexts verwendet wird. | CLIP | Ja | N/A |
| `tags` | Beschreibende Tags für das Audio, wie Genre, Stimmung oder Instrumente. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | N/A |
| `lyrics` | Der Liedtext für die Audiospur. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | N/A |
| `seed` | Ein zufälliger Seed-Wert für reproduzierbare Generierung. Verfügt über ein `control_after_generate`-Widget. Standard: 0. | INT | Nein | 0 to 18446744073709551615 |
| `bpm` | Die Beats pro Minute (BPM) für das generierte Audio. Standard: 120. | INT | Nein | 10 to 300 |
| `duration` | Die gewünschte Dauer des Audios in Sekunden. Standard: 120.0. | FLOAT | Nein | 0.0 to 2000.0 |
| `timesignature` | Die musikalische Taktart. | COMBO | Nein | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | Die Sprache des Eingabetexts. Standard: "en". | COMBO | Nein | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | Die musikalische Tonart und Skala (Dur oder Moll). | COMBO | Nein | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | Aktiviert das LLM, das Audio-Codes generiert. Dies kann langsam sein, erhöht aber die Qualität des generierten Audios. Deaktivieren Sie dies, wenn Sie dem Modell eine Audioreferenz geben. Standard: True. | BOOLEAN | Nein | N/A |
| `cfg_scale` | Die Classifier-Free-Guidance-Skala. Höhere Werte bewirken, dass die Ausgabe dem Prompt stärker folgt. Standard: 2.0. | FLOAT | Nein | 0.0 to 100.0 |
| `temperature` | Eine Sampling-Temperatur. Niedrigere Werte machen die Ausgabe deterministischer. Standard: 0.85. | FLOAT | Nein | 0.0 to 2.0 |
| `top_p` | Die Nucleus-Sampling-Wahrscheinlichkeit (top-p). Standard: 0.9. | FLOAT | Nein | 0.0 to 2000.0 |
| `top_k` | Die Anzahl der Token mit höchster Wahrscheinlichkeit, die berücksichtigt werden (top-k). Standard: 0. | INT | Nein | 0 to 100 |
| `min_p` | Der Mindestwahrscheinlichkeitsschwellenwert für Token-Sampling (min-p). Standard: 0.000. | FLOAT | Nein | 0.0 to 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die Conditioning-Daten, die den codierten Text und die Audioparameter für das AceStepAudio 1.5-Modell enthalten. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/de.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
