# SaveImageTextDataSetToFolder

Save Image-Text (to Folder) speichert einen Datensatz aus Paaren von Bildern und Textbeschriftungen in einem Ordner innerhalb des Ausgabeverzeichnisses von ComfyUI. Jedes Bild wird als PNG-Datei gespeichert, und die zugehörige Beschriftung wird als TXT-Datei mit demselben Basisdateinamen gespeichert, sodass jedes Bild mit seiner Beschreibung gepaart wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Liste der zu speichernden Bilder. | IMAGE | Ja | - |
| `texts` | Liste der zu speichernden Textbeschriftungen. Diese Eingabe ist optional. | STRING | Nein | - |
| `folder_name` | Name des Ordners, in dem die Bilder gespeichert werden (innerhalb des Ausgabeverzeichnisses). (Standard: "dataset") | STRING | Ja | - |
| `filename_prefix` | Präfix für Dateinamen gespeicherter Bilder. (Standard: "image") | STRING | Ja | - |
| `mode` | Ob vorhandene Dateien überschrieben oder Dateinamen inkrementiert werden sollen, um ein Überschreiben zu vermeiden. (Standard: "overwrite") | COMBO | Ja | "overwrite"<br>"increment" |

**Hinweis:** Die `images`-Eingabe ist eine Liste, und der Node erhält sowohl `images` als auch `texts` als Listen. Die `texts`-Eingabe ist optional; falls angegeben, sollte sie eine Liste von Textbeschriftungen sein und die gleiche Anzahl an Elementen wie `images` enthalten. Jede Beschriftung wird als `.txt`-Datei gespeichert, die zu ihrem zugehörigen Bild gehört. Im `overwrite`-Modus werden Dateien als `{filename_prefix}_{index}.png` benannt und ersetzen alle vorhandenen Dateien mit demselben Namen. Im `increment`-Modus wird den Dateinamen ein eindeutiger Zähler hinzugefügt, sodass vorhandene Dateien nicht überschrieben werden. Der `folder_name` muss zu einem Pfad innerhalb des Ausgabeverzeichnisses aufgelöst werden; Ordnernamen, die versuchen, daraus auszubrechen (zum Beispiel mit `..`), werden abgelehnt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| - | Dieser Node gibt keine Daten zurück. Er speichert Dateien direkt im Dateisystem. | - |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/de.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
