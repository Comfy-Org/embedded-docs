# Bild-Text laden (aus Ordner)

Dieser Node lädt einen Datensatz aus Bild-Text-Bildbeschreibungspaaren aus einem ausgewählten Ordner und gibt sie als Liste zurück. Er unterstützt PNG-, JPG-, JPEG- und WEBP-Bilder und sucht für jedes Bild nach einer Bildbeschreibung in einer `.txt`-Datei mit demselben Basisnamen. Der Node unterstützt außerdem die Ordnerstruktur von kohya-ss/sd-scripts, bei der ein Unterordnername, der mit einer Zahl beginnt (z. B. `10_cats`), die Bilder in diesem Unterordner entsprechend oft in der Ausgabe wiederholt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `folder` | Der Ordner, aus dem Bilder und Textbeschriftungen geladen werden. | COMBO | Ja | Unterordner innerhalb des Eingabeverzeichnisses von ComfyUI (dynamisch geladen) |

**Hinweis:** Der ausgewählte Ordner muss ein Unterordner des Eingabeverzeichnisses von ComfyUI sein. Der Node erwartet eine `.txt`-Bildbeschreibungsdatei pro Bild: Für jede Bilddatei (`.png`, `.jpg`, `.jpeg`, `.webp`) sucht er nach einer `.txt`-Datei mit demselben Basisnamen am selben Speicherort und verwendet deren getrimmten Inhalt als Bildbeschreibung. Wenn keine Bildbeschreibungsdatei gefunden wird, wird eine leere Zeichenkette verwendet. Der Node unterstützt außerdem die Ordnerstruktur von kohya-ss/sd-scripts: Unterordner, deren Name mit einer Zahl und einem Unterstrich beginnt (zum Beispiel `5_cats`), wiederholen die darin enthaltenen Bilder entsprechend oft in der endgültigen Ausgabeliste. Wenn der ausgewählte Ordner keine gültigen Bilder enthält, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Liste der geladenen Bilder. Bilder werden in RGB konvertiert und auf den Gleitkommabereich 0–1 normalisiert. | IMAGE |
| `texts` | Liste von Textbeschreibungen, eine für jedes geladene Bild. Bildbeschreibungen sind die getrimmten Inhalte der passenden `.txt`-Datei oder eine leere Zeichenkette, wenn keine Bildbeschreibungsdatei existiert. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/de.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
