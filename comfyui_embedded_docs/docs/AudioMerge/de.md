# AudioMerge

Der AudioMerge-Node kombiniert zwei Audiospuren, indem er ihre Wellenformen überlagert. Er gleicht automatisch die Abtastraten beider Audioeingaben an und passt ihre Längen an, sodass sie vor dem Zusammenführen gleich lang sind. Der Node bietet mehrere mathematische Methoden zum Kombinieren der Audiosignale und stellt sicher, dass die Ausgabe innerhalb akzeptabler Lautstärkepegel bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio1` | Erste Audioeingabe zum Zusammenführen | AUDIO | Ja | - |
| `audio2` | Zweite Audioeingabe zum Zusammenführen | AUDIO | Ja | - |
| `merge_method` | Die Methode zum Kombinieren der Audiowellenformen. | COMBO | Ja | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `AUDIO` | Die zusammengeführte Audioausgabe, die die kombinierte Wellenform und die Abtastrate enthält | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/de.md)

---
**Source fingerprint (SHA-256):** `3bb8c223e9a5155b5e60f901e8653c6654336a10a56d25ba7a3c5e8f5382ad27`
