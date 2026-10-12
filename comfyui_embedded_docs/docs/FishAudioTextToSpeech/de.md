# FishAudioTextToSpeech

Dieser Node wandelt geschriebenen Text mithilfe von Fish Audio Text-to-Speech-Modellen in gesprochenes Audio um. Er unterstützt Emotionshinweise, die in den Text eingebettet sind ([happy], [whispering] bei s2.1-pro; (happy) bei s1), sowie Multi-Speaker-Dialoge mit @Voice1/@Voice2-Tags, wenn mehrere Stimmen verbunden sind. Zwei Modelle sind verfügbar: s2.1-pro, das bis zu fünf Stimmen und Multi-Speaker-Dialoge unterstützt, und s1, das eine einzelne optionale Stimme verwendet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `text` | Der in Sprache umzuwandelnde Text. Wenn zwei oder mehr Stimmen verbunden sind, kennzeichnen Sie Sprecherwechsel mit @Voice1, @Voice2 usw. (Standard: leer) | STRING | Ja | Beliebiger nicht leerer Text |
| `model` | Modell für Text-to-Speech. | DYNAMIC_COMBO | Ja | "s2.1-pro"<br>"s1" |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### s2.1-pro Eingaben

Diese Eingaben werden angezeigt, wenn das Modell s2.1-pro ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `voices` | Erweiterbarer Slot: Verbinden Sie 0 bis 5 Voice-Elemente (`voice_1`, `voice_2`, ...). Stimmen für die Synthese. Leer lassen für die Standardstimme. Bei zwei oder mehr Stimmen markieren Sie Sprecherwechsel im Text mit @Voice1, @Voice2 usw. | FISHAUDIO_VOICE | Nein | 0 bis 5 Stimmen |
| `temperature` | Ausdrucksstärke. Höhere Werte sind variabler, niedrigere Werte konsistenter. (Standard: 0.7) | FLOAT | Ja | 0.0 bis 1.0 |
| `top_p` | Vielfalt durch Nucleus-Sampling. (Standard: 0.7) | FLOAT | Ja | 0.01 bis 1.0 |
| `speed` | Sprechgeschwindigkeit. 1.0 ist normal, <1.0 langsamer, >1.0 schneller. (Standard: 1.0) | FLOAT | Ja | 0.5 bis 2.0 |
| `volume` | Lautstärkeanpassung in Dezibel. 0 bedeutet keine Änderung. (Standard: 0.0) | FLOAT | Ja | -10.0 bis 10.0 |
| `normalize` | Normalisiert Zahlen und Text für Englisch und Chinesisch und verbessert die Stabilität bei Zahlen und Datumsangaben. (Standard: true) | BOOLEAN | Ja | true / false |

### s1 Eingaben

Diese Eingaben werden angezeigt, wenn das Modell s1 ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `voice` | Stimme für die Synthese. Nicht verbunden lassen für die Standardstimme. | FISHAUDIO_VOICE | Nein | Optionale einzelne Stimme |
| `temperature` | Ausdrucksstärke. Höhere Werte sind variabler, niedrigere Werte konsistenter. (Standard: 0.7) | FLOAT | Ja | 0.0 bis 1.0 |
| `top_p` | Vielfalt durch Nucleus-Sampling. (Standard: 0.7) | FLOAT | Ja | 0.01 bis 1.0 |
| `speed` | Sprechgeschwindigkeit. 1.0 ist normal, <1.0 langsamer, >1.0 schneller. (Standard: 1.0) | FLOAT | Ja | 0.5 bis 2.0 |
| `volume` | Lautstärkeanpassung in Dezibel. 0 bedeutet keine Änderung. (Standard: 0.0) | FLOAT | Ja | -10.0 bis 10.0 |
| `normalize` | Normalisiert Zahlen und Text für Englisch und Chinesisch und verbessert die Stabilität bei Zahlen und Datumsangaben. (Standard: true) | BOOLEAN | Ja | true / false |

**Hinweis:** Die Eingabe `text` darf nicht leer sein. Sprecher-Tags (@Voice1, @Voice2 usw.) sind groß-/kleinschreibungsunabhängig und müssen auf eine verbundene Stimme verweisen; das Taggen einer nicht verbundenen Stimme löst einen Fehler aus. Wenn zwei oder mehr Stimmen verbunden sind, muss der Text jede verbundene Stimme mindestens einmal referenzieren, andernfalls meldet der Node die fehlenden Tags. Bei s2.1-pro verwendet das Verbinden von 0 Stimmen die Standardstimme, 1 Stimme verwendet nur diese Stimme, und 2 oder mehr Stimmen aktivieren Multi-Speaker-Dialoge. Bei s1 wird eine einzelne optionale Stimme verwendet; bleibt sie nicht verbunden, wird die Standardstimme verwendet. Emotionshinweise können im Text platziert werden: [happy] und [whispering] bei s2.1-pro sowie (happy) bei s1.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die generierte Sprachausgabe als Audiodatei. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/de.md)

---
**Source fingerprint (SHA-256):** `6cc005ae76fc7b60d9399b1b0a3c5de40a6eff47cd6f0f0b73b4212c0270ae29`
