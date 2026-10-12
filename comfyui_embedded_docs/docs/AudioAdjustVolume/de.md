# Audiolautstärke anpassen

Der AudioAdjustVolume-Node modifiziert die Lautstärke von Audio durch Anwendung von Lautstärkeanpassungen in Dezibel (dB). Er nimmt einen Audio-Eingang entgegen und wendet einen Verstärkungsfaktor basierend auf dem angegebenen Lautstärkepegel an, wobei positive Werte die Lautstärke erhöhen und negative Werte sie verringern. Der Node gibt das modifizierte Audio mit derselben Abtastrate wie das Original zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Der zu verarbeitende Audio-Eingang | AUDIO | Ja | - |
| `volume` | Lautstärkeanpassung in Dezibel (dB). 0 = keine Änderung, +6 = doppelt, -6 = halb, usw. (Standard: 1) | INT | Ja | -100 bis 100 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Das verarbeitete Audio mit angepasstem Lautstärkepegel | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/de.md)

---
**Source fingerprint (SHA-256):** `8c19625104901a0c57021b1a775fdf287c8bd0fb1fd535809e1983b1949ca752`
