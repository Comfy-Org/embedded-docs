# ByteDance Seed Audio 1.0

Generiert Sprache, Musik, Soundeffekte und Dialoge mit mehreren Sprechern aus einem einzelnen Prompt mit ByteDance Seed Audio 1.0. Beschreiben Sie die Stimme(n), Emotionen, Atmosphäre, Hintergrundmusik und Soundeffekte im Prompt und geben Sie die zu sprechenden Zeilen an. Wählen Sie optional eine integrierte voreingestellte Stimme, klonen Sie Stimmen aus bis zu 3 Referenzclips (im Prompt mit @Audio1-3 markiert) oder leiten Sie eine Stimme aus einem Charakterbild ab. Bis zu 2 Minuten Audio pro Ausführung. Das mehrsprachige Modell unterstützt 20 Sprachen und zeitstempelbasierte Zeitsteuerung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `text_prompt` | Beschreiben Sie die Stimme(n), Emotion, das Tempo, die Atmosphäre, Hintergrundmusik und Soundeffekte und fügen Sie die zu sprechenden Zeilen hinzu (benennen Sie Charaktere für Dialoge direkt im Text). Im Modus "audio reference" beziehen Sie sich auf verbundene Clips der Reihenfolge nach als @Audio1, @Audio2, @Audio3. Beim mehrsprachigen Modell kann eine zitierte Zeile mit einem Zeitstempelbereich beginnen, der steuert, wann und wie lange sie gesprochen wird, z. B. `[5.5s:8.0s] Wait for me!`. Schreiben Sie den Prompt in derselben Sprache wie die zu sprechenden Zeilen. Mindestens 1 Zeichen, maximal 3000 Zeichen. | STRING | Ja | 1 bis 3000 Zeichen |
| `reference_mode` | Wie die Stimme konditioniert wird: "text only" (alles im Prompt beschreiben), "audio reference" (bis zu 3 Stimmen klonen, gekennzeichnet mit @Audio1-3), "image reference" (eine Stimme aus einem Charakterbild ableiten) oder "preset voice" (eine integrierte benannte Stimme auswählen, die den Prompt vorliest). | COMBO | Ja | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | Referenzclip für Voice-Cloning, im Prompt mit @Audio1 gekennzeichnet. Bis zu 30 s. Nur verfügbar, wenn `reference_mode` "audio reference" ist. | AUDIO | Nein | Bis zu 30 Sekunden |
| `reference_audio_2` | Referenzclip, im Prompt mit @Audio2 gekennzeichnet. Bis zu 30 s. Nur verfügbar, wenn `reference_mode` "audio reference" ist. | AUDIO | Nein | Bis zu 30 Sekunden |
| `reference_audio_3` | Referenzclip, im Prompt mit @Audio3 gekennzeichnet. Bis zu 30 s. Nur verfügbar, wenn `reference_mode` "audio reference" ist. | AUDIO | Nein | Bis zu 30 Sekunden |
| `reference_image` | Ein einzelnes Charakterbild; das Modell leitet daraus eine Stimme ab. Kann nicht mit Audio-Referenzen kombiniert werden. Nur verfügbar, wenn `reference_mode` "image reference" ist. | IMAGE | Nein | - |
| `preset_voice` | Eine integrierte TTS 2.0-Stimme, die den Prompt vorliest. Kein Referenzclip erforderlich, und @AudioN-Tags werden in diesem Modus nicht verwendet. Erforderlich, wenn `reference_mode` "preset voice" ist. | COMBO | Nein | Mehrere integrierte Preset-Stimmenoptionen (standardmäßig ist die erste Option ausgewählt) |
| `sample_rate` | Ausgabe-Abtastrate in Hz. (Standard: "24000") | COMBO | Ja | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Sprechgeschwindigkeit. 0 = normal, 100 = 2,0x, -50 = 0,5x. (Standard: 0) | INT | Ja | -50 bis 100 |
| `loudness_rate` | Lautstärke. 0 = normal, 100 = 2,0x, -50 = 0,5x. (Standard: 0) | INT | Ja | -50 bis 100 |
| `pitch_rate` | Tonhöhenverschiebung in Halbtönen (-12 bis 12). (Standard: 0) | INT | Ja | -12 bis 12 |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |
| `model` | Modellversion. `seed-audio-1.0-multilingual` unterstützt 20 Sprachen und Timing-Steuerung pro Satz über `[5.5s:8.0s]`-Zeitstempel. `seed-audio-1.0` unterstützt nur Englisch und Chinesisch, ohne Timing-Steuerung. (Standard: "seed-audio-1.0-multilingual") | COMBO | Nein | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### Parameterbeschränkungen

- **Abhängigkeiten des Referenzmodus**: Der Parameter `reference_mode` bestimmt, welche anderen Eingaben erforderlich sind:
  - **"text only"**: Keine zusätzlichen Eingaben erforderlich. Der Prompt darf keine @AudioN-Tags enthalten.
  - **"audio reference"**: Erfordert, dass mindestens einer von `reference_audio_1`, `reference_audio_2` oder `reference_audio_3` verbunden ist. Referenzclips müssen in der Reihenfolge und ohne Lücken verbunden werden. Jeder Clip ist auf eine maximale Dauer von 30 Sekunden begrenzt. Wenn @AudioN-Tags im Prompt verwendet werden, darf die höchste Tag-Nummer die Anzahl der verbundenen Referenzclips nicht überschreiten.
  - **"image reference"**: Erfordert, dass `reference_image` verbunden ist. @AudioN-Tags werden nicht verwendet; der Prompt sollte nur den zu synthetisierenden Text enthalten.
  - **"preset voice"**: Erfordert, dass eine Preset-Stimme ausgewählt ist. Der gesamte Prompt wird in der ausgewählten Stimme vorgelesen; @AudioN-Tags werden nicht als Referenzen verwendet, und Tags wie @Audio2 oder höher werden abgelehnt.

- **Reihenfolge der Audio-Referenzen**: Im Modus "audio reference" müssen die Audio-Referenzeingaben sequenziell beginnend mit `reference_audio_1` und ohne Lücken verbunden werden. Zum Beispiel können Sie `reference_audio_1` und `reference_audio_2` verbinden, aber nicht `reference_audio_1` und `reference_audio_3` ohne `reference_audio_2`.

- **Maximale Audio-Tags**: Im Modus "audio reference" können bis zu 3 Referenzclips verbunden werden (@Audio1, @Audio2, @Audio3), und das höchste @AudioN-Tag im Prompt darf die Anzahl der verbundenen Audio-Referenzeingaben nicht überschreiten.

- **Modellunterschiede**: Das Modell `seed-audio-1.0-multilingual` unterstützt 20 Sprachen (Englisch, Chinesisch, Japanisch, Koreanisch, Mexikanisches und Kastilisches Spanisch, Indonesisch, Deutsch, Brasilianisches Portugiesisch, Französisch, Thailändisch, Vietnamesisch, Malaiisch, Filipino, Italienisch, Russisch, Niederländisch, Polnisch, Türkisch, Schwedisch) sowie Timing-Steuerung pro Satz unter Verwendung von Zeitstempeln im Format `[5.5s:8.0s]`. Das Modell `seed-audio-1.0` unterstützt nur Englisch und Chinesisch, ohne Timing-Steuerung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Die generierte Audio-Ausgabe von ByteDance Seed Audio 1.0, die Sprache, Musik, Soundeffekte oder Multi-Speaker-Dialoge gemäß der Beschreibung im Prompt enthält. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/de.md)

---
**Source fingerprint (SHA-256):** `e86e4edde424b4427d864350a9d3b082e271fbd2b1e335175637a9cc3ad51163`
