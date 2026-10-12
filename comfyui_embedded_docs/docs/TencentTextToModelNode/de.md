# TencentTextToModelNode

Dieser Node verwendet die Hunyuan3D Pro API von Tencent, um aus einer Textbeschreibung ein 3D-Modell zu erzeugen. Er sendet eine Anfrage zum Erstellen einer Generierungsaufgabe, fragt das Ergebnis wiederholt ab und lädt die endgültigen Modelldateien im GLB- und OBJ-Format herunter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Die Version des zu verwendenden Hunyuan3D-Modells. Die Option LowPoly ist für das Modell `3.1` nicht verfügbar. | COMBO | Ja | `"3.0"`<br>`"3.1"` |
| `prompt` | Die Textbeschreibung des zu generierenden 3D-Modells. Unterstützt bis zu 1024 Zeichen. | STRING | Ja | - |
| `face_count` | Die Zielanzahl der Flächen für das generierte 3D-Modell. Standard: 500000. | INT | Ja | 3000 - 1500000 |
| `generate_type` | Der Typ des zu generierenden 3D-Modells. Die verfügbaren Optionen und ihre zugehörigen Parameter sind:<br>- **Normal**: Erzeugt ein Standardmodell. Enthält einen `pbr`-Parameter (Standard: `False`).<br>- **LowPoly**: Erzeugt ein Modell mit niedriger Polygonzahl. Enthält die Parameter `polygon_type` (`"triangle"` oder `"quadrilateral"`) und `pbr` (Standard: `False`).<br>- **Geometry**: Erzeugt ein Modell, das nur aus Geometrie besteht. | DYNAMICCOMBO | Ja | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `seed` | Ein Seed-Wert für die Generierung. Die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Das Setzen eines neuen Seeds steuert, ob der Node erneut ausgeführt werden soll. Standard: 0. | INT | Nein | 0 - 2147483647 |

**Hinweis:** Der Parameter `generate_type` ist dynamisch. Wenn Sie `"LowPoly"` auswählen, werden zusätzliche Eingaben für `polygon_type` und `pbr` eingeblendet. Wenn Sie `"Normal"` auswählen, wird eine Eingabe für `pbr` eingeblendet. Wenn Sie `"Geometry"` auswählen, werden keine zusätzlichen Eingaben eingeblendet.

**Einschränkung:** Der Generierungstyp `"LowPoly"` kann nicht mit dem Modell `"3.1"` verwendet werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Eine Legacy-Ausgabe für Abwärtskompatibilität. | STRING |
| `GLB` | Das generierte 3D-Modell im GLB-Dateiformat. | FILE3DGLB |
| `OBJ` | Das generierte 3D-Modell im OBJ-Dateiformat. | FILE3DOBJ |
| `texture_image` | Das aus der generierten OBJ-Datei extrahierte Texturbild, falls verfügbar. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `8110b6a70cdd26d5d0dcb791e654a6292895693e25076b982951c65f787422d6`
