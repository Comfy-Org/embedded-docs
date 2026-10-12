# SaveImage

Der SaveImage-Node speichert die Eingabebilder als PNG-Dateien in Ihrem ComfyUI-Ausgabeverzeichnis. Er kann Workflow-Metadaten wie den Prompt in jede gespeicherte Datei einbetten und gibt die Bilder unverändert zurück, sodass sie weiterhin von anderen Nodes verwendet werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Die zu speichernden Bilder. | IMAGE | Ja | - |
| `filename_prefix` | Das Präfix für die zu speichernde Datei. Dies kann Formatierungsinformationen wie `%date:yyyy-MM-dd%` oder `%Empty Latent Image.width%` enthalten, um Werte aus Nodes aufzunehmen (Standard: "ComfyUI"). | STRING | Ja | - |

Der Node empfängt außerdem zwei versteckte Eingaben, `prompt` und `extra_pnginfo`, die von ComfyUI automatisch mit dem Workflow-Prompt und zusätzlichen PNG-Informationen befüllt werden. Wenn Metadaten aktiviert sind, werden diese Informationen als Textmetadaten in jede gespeicherte PNG-Datei eingebettet.

Der Dateiname für jedes gespeicherte Bild wird aus `filename_prefix`, einem optionalen `%batch_num%`-Platzhalter, der durch die Position des Bildes im Batch ersetzt wird, und einem fünfstelligen Zähler gebildet, zum Beispiel `ComfyUI_00001_.png`. Bilder werden mit PNG-Komprimierungsstufe 4 geschrieben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Die ursprünglichen Eingabebilder, unverändert zurückgegeben, nachdem sie auf der Festplatte gespeichert wurden. | IMAGE |
| `ui` | Ein reines UI-Ergebnis, das die Liste der gespeicherten Bilddateien (Dateiname, Unterordner und Typ) zur Anzeige im Frontend enthält. | UI_RESULT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/de.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
