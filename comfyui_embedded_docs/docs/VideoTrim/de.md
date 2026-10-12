# VideoTrim

Dieser Node schneidet ein Video auf ein gewähltes Zeitfenster, indem eine Startzeit und eine Dauer festgelegt werden. Er bietet außerdem einen strikten Modus, der einen Fehler auslöst, wenn die angeforderte Dauer nicht erreicht werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Das zu schneidende Video. | VIDEO | Ja | — |
| `trim` | Schneidefenster unter Verwendung von Start-/Endframes. Das Fenster wird in eine Startzeit (in Sekunden ab Beginn des Videos) und eine Dauer (in Sekunden) umgewandelt. Wenn sowohl die Startzeit als auch die Dauer 0 sind, wird das Video ohne Kürzung zurückgegeben. | VIDEO_EDIT | Ja | start_time: >= 0, default 0<br>duration: >= 0, default 0 |
| `strict_duration` | Wenn True, wird ein Fehler ausgelöst, wenn die angegebene Dauer nicht möglich ist. (Standard: False) | BOOLEAN | Nein | true<br>false |

Hinweis: Die Trim-Dauer muss >= 0 sein; negative Werte lösen einen Fehler aus. Das angeforderte Trim-Fenster muss in das Quellvideo passen. Wenn der Trim nicht angewendet werden kann, wird ein Fehler ausgelöst, der die Quelldauer, die Startzeit und die Zieldauer meldet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das geschnittene Video. Wenn das Trim-Fenster leer ist (Startzeit und Dauer beide 0), wird das Originalvideo unverändert zurückgegeben. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/de.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`
