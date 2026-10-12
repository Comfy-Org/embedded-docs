# Audio-Equalizer (3-Band)

Der Node Audio Equalizer (3-Band) ermöglicht es Ihnen, die Bass-, Mitten- und Höhenfrequenzen einer Audio-Wellenform anzupassen. Er wendet drei separate Filter an: einen Low-Shelf für den Bass, einen Peaking-Filter für die Mitten und einen High-Shelf für die Höhen. Jedes Band kann unabhängig über Einstellungen für Verstärkung, Frequenz und Bandbreite gesteuert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Die eingegebenen Audiodaten, die die Wellenform und die Abtastrate enthalten. | AUDIO | Ja | - |
| `low_gain_dB` | Verstärkung für tiefe Frequenzen (Bass). Positive Werte verstärken, negative Werte senken. (Standard: 0.0) | FLOAT | Nein | -24.0 bis 24.0 |
| `low_freq` | Grenzfrequenz für den Low-Shelf-Filter in Hertz (Hz). (Standard: 100) | INT | Nein | 20 bis 500 |
| `mid_gain_dB` | Verstärkung für mittlere Frequenzen. Positive Werte verstärken, negative Werte senken. (Standard: 0.0) | FLOAT | Nein | -24.0 bis 24.0 |
| `mid_freq` | Mittenfrequenz für den Mitten-Peaking-Filter in Hertz (Hz). (Standard: 1000) | INT | Nein | 200 bis 4000 |
| `mid_q` | Q-Faktor (Bandbreite) für den Mitten-Peaking-Filter. Niedrigere Werte erzeugen ein breiteres Band, höhere Werte ein schmaleres Band. (Standard: 0.707) | FLOAT | Nein | 0.1 bis 10.0 |
| `high_gain_dB` | Verstärkung für hohe Frequenzen (Höhen). Positive Werte verstärken, negative Werte senken. (Standard: 0.0) | FLOAT | Nein | -24.0 bis 24.0 |
| `high_freq` | Grenzfrequenz für den High-Shelf-Filter in Hertz (Hz). (Standard: 5000) | INT | Nein | 1000 bis 15000 |

**Hinweis:** Die Parameter `low_gain_dB`, `mid_gain_dB` und `high_gain_dB` werden nur angewendet, wenn ihr Wert nicht null ist. Wenn eine Verstärkung auf 0.0 gesetzt ist, wird die entsprechende Filterstufe übersprungen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Die verarbeiteten Audiodaten mit angewendeter Entzerrung, die die geänderte Wellenform und die ursprüngliche Abtastrate enthalten. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/de.md)

---
**Source fingerprint (SHA-256):** `be3a0981d8285885cb465e82717c3f56c9d301d55708962f9a9dd5b2c400ec81`
