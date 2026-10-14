# Fish Audio Text zu Sprache

Dieser Node wandelt geschriebenen Text mithilfe von Fish Audio Text-to-Speech-Modellen in gesprochenes Audio um. Er unterstützt Hinweise, die in den Text eingebettet werden: [happy] und [whispering] bei s2.1-pro, (happy) bei s1 sowie natürlichsprachliche [directions] plus `<whisper>...</whisper>`-Wort-Tags bei drama-3. Mehrsprecher-Dialoge verwenden @Voice1/@Voice2-Tags, wenn mehrere Stimmen verbunden sind. Drei Modelle sind verfügbar: drama-3 und s2.1-pro, die beide bis zu fünf Stimmen und Mehrsprecher-Dialoge unterstützen, sowie s1, das eine einzelne optionale Stimme verwendet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `Text` | Der in Sprache umzuwandelnde Text. Wenn zwei oder mehr Stimmen verbunden sind, markieren Sie Sprecherwechsel mit @Voice1, @Voice2 usw. (Standard: leer) | STRING | Ja | Beliebiger nicht leerer Text |
| `Modell` | Modell, das für Text-to-Speech verwendet werden soll. | DYNAMIC_COMBO | Ja | "drama-3"<br>"s2.1-pro"<br>"s1" |
| `Seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### drama-3 und s2.1-pro Eingaben

Diese Eingaben erscheinen, wenn das Modell `drama-3` oder `s2.1-pro` ausgewählt ist. Die Parametersätze sind identisch.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `voices` | Erweiterbarer Slot: Verbinden Sie 0 bis 5 Stimmelemente (`voice_1`, `voice_2`, ...). Stimmen für die Synthese. Leer lassen für eine zufällige Stimme. Bei zwei oder mehr Stimmen markieren Sie Sprecherwechsel im Text mit @Voice1, @Voice2 usw. | FISHAUDIO_VOICE | Nein | 0 bis 5 Stimmen |
| `temperature` | Ausdrucksstärke. Höhere Werte sind variabler, niedrigere Werte konsistenter. (Standard: 0.7) | FLOAT | Ja | 0.0 bis 1.0 |
| `top_p` | Vielfalt durch Nucleus-Sampling. (Standard: 0.7) | FLOAT | Ja | 0.01 bis 1.0 |
| `speed` | Sprechgeschwindigkeit. 1.0 ist normal, <1.0 langsamer, >1.0 schneller. (Standard: 1.0) | FLOAT | Ja | 0.5 bis 2.0 |
| `volume` | Lautstärkeanpassung in Dezibel. 0 bedeutet keine Änderung. (Standard: 0.0) | FLOAT | Ja | -10.0 bis 10.0 |
| `normalize` | Zahlen und Text für Englisch und Chinesisch normalisieren; verbessert die Stabilität bei Zahlen und Datumsangaben. (Standard: true) | BOOLEAN | Ja | true / false |

### s1 Eingaben

Diese Eingaben erscheinen, wenn das Modell s1 ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `voice` | Stimme für die Synthese. Nicht verbunden lassen für eine zufällige Stimme. | FISHAUDIO_VOICE | Nein | Optionale einzelne Stimme |
| `temperature` | Ausdrucksstärke. Höhere Werte sind variabler, niedrigere Werte konsistenter. (Standard: 0.7) | FLOAT | Ja | 0.0 bis 1.0 |
| `top_p` | Vielfalt durch Nucleus-Sampling. (Standard: 0.7) | FLOAT | Ja | 0.01 bis 1.0 |
| `speed` | Sprechgeschwindigkeit. 1.0 ist normal, <1.0 langsamer, >1.0 schneller. (Standard: 1.0) | FLOAT | Ja | 0.5 bis 2.0 |
| `volume` | Lautstärkeanpassung in Dezibel. 0 bedeutet keine Änderung. (Standard: 0.0) | FLOAT | Ja | -10.0 bis 10.0 |
| `normalize` | Zahlen und Text für Englisch und Chinesisch normalisieren; verbessert die Stabilität bei Zahlen und Datumsangaben. (Standard: true) | BOOLEAN | Ja | true / false |

**Hinweis:** Die Eingabe `text` darf nicht leer sein. Sprecher-Tags (@Voice1, @Voice2 usw.) unterscheiden nicht zwischen Groß- und Kleinschreibung und müssen auf eine verbundene Stimme verweisen; das Markieren einer nicht verbundenen Stimme löst einen Fehler aus. Wenn zwei oder mehr Stimmen verbunden sind, muss der Text jede verbundene Stimme mindestens einmal referenzieren, sonst meldet der Node die fehlenden Tags. Bei drama-3 und s2.1-pro verwendet das Verbinden von 0 Stimmen eine zufällige Stimme, 1 Stimme verwendet nur diese Stimme, und 2 oder mehr Stimmen aktivieren Mehrsprecher-Dialoge. Bei s1 wird eine einzelne optionale Stimme verwendet; wird sie nicht verbunden, wird eine zufällige Stimme verwendet. Hinweise können im Text platziert werden: [happy] und [whispering] bei s2.1-pro, (happy) bei s1 sowie natürlichsprachliche [directions] und `<whisper>...</whisper>`-Wort-Tags bei drama-3.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `audio` | Die generierte Sprachausgabe als Audiodatei. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/de.md)

---
**Source fingerprint (SHA-256):** `adcfe8f994b8fbe07efb3dd3f86c8955ea3cec62cc3f0321efd2b63c0470b7a3`
