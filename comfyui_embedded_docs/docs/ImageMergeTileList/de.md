# ImageMergeTileList

Dieser Node nimmt eine Liste von Bildkacheln entgegen und fügt sie wieder zu einem einzelnen, größeren Bild zusammen. Er wurde entwickelt, um ein Bild zu rekonstruieren, das zuvor in ein Raster aus überlappenden Kacheln aufgeteilt wurde, wobei eine gewichtete Mischtechnik verwendet wird, um ein nahtloses Endergebnis zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image_list` | Eine Liste von Bildkacheln, die zusammengefügt werden sollen. Die erste Kachel in der Liste wird verwendet, um die Kachelabmessungen und den Datentyp für den gesamten Prozess zu bestimmen. | IMAGE | Ja | N/A |
| `final_width` | Die Breite des finalen zusammengefügten Bildes in Pixeln (Standard: 1024). | INT | Ja | 64 - 32768 |
| `final_height` | Die Höhe des finalen zusammengefügten Bildes in Pixeln (Standard: 1024). | INT | Ja | 64 - 32768 |
| `overlap` | Der Überlappungsbetrag zwischen benachbarten Kacheln in Pixeln. Ein Wert größer als 0 aktiviert einen weichen Mischungseffekt an den Kachelnähten (Standard: 128). | INT | Ja | 0 - 4096 |

**Hinweis:** Die `image_list` ist eine dynamische Eingabeliste. Der Node verarbeitet die Kacheln in der Reihenfolge, in der sie bereitgestellt werden, bis zu der Anzahl, die erforderlich ist, um das durch `final_width`, `final_height` und die Abmessungen der ersten Kachel definierte Raster zu füllen. Wenn die Liste mehr Kacheln als benötigt enthält, werden die überzähligen Kacheln ignoriert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das final zusammengefügte Bild, rekonstruiert aus den Eingabekacheln. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/de.md)

---
**Source fingerprint (SHA-256):** `41b570bf758093f3693c015e7976b946b9d93ca56db2bf66617149f259ae8c06`
