# Video-Text laden (aus Ordner)

Dieser Node lädt Videodateien und die zugehörigen Textbeschriftungen aus einem Ordner innerhalb des ComfyUI-Eingabeverzeichnisses und gibt sie als zwei Listen zurück: Videos und Beschriftungen. Die Videoeinträge sind Lazy-Referenzen, sodass Frames erst dekodiert werden, wenn ein nachgelagerter Node sie benötigt. Unterstützte Formate sind MP4, AVI, MOV, WEBM, MKV und FLV; verschachtelte Ordner mit einem Präfix für die Wiederholungsanzahl (zum Beispiel `5_classname/`, wie es von Tools wie kohya-ss/sd-scripts verwendet wird) werden ebenfalls unterstützt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `folder` | Der Ordner, der Videodateien und .txt-Beschriftungen enthält. | COMBO | Ja | Listet dynamisch alle Unterordner innerhalb des ComfyUI-Eingabeverzeichnisses auf |

Der ausgewählte Ordner muss ein Unterordner des ComfyUI-Eingabeverzeichnisses sein; ein Ordnername, der außerhalb dieses Verzeichnisses aufgelöst wird, führt zu einem Fehler. Wenn der ausgewählte Ordner keine Dateien mit einer unterstützten Videoerweiterung (MP4, AVI, MOV, WEBM, MKV, FLV) enthält, löst der Node einen Fehler aus. Bei verschachtelten Ordnern, deren Name mit einer Zahl gefolgt von einem Unterstrich beginnt (zum Beispiel `5_classname`), wird jedes Video in diesem Ordner so oft in den Datensatz aufgenommen, wie es das Präfix angibt. Die Beschriftung jedes Videos wird aus einer `.txt`-Datei mit demselben Basisnamen gelesen; wenn keine passende `.txt`-Datei existiert, ist die Beschriftung eine leere Zeichenkette.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `videos` | Lazy-Video-Referenzen; Frames werden erst dekodiert, wenn sie nachgelagert benötigt werden. Ein Eintrag pro im Ordner gefundener Videodatei. | VIDEO (list) |
| `texts` | Liste von Textbeschriftungen. Eine Beschriftung pro Video; wenn ein Video keine passende `.txt`-Datei hat, ist seine Beschriftung eine leere Zeichenkette. | STRING (list) |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/de.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
