# MeshyTextToModelNode

Der Node Meshy: Text to Model verwendet die Meshy-API, um aus einer Textbeschreibung ein 3D-Modell zu generieren. Er sendet eine Anfrage mit Ihrem Prompt und Ihren Einstellungen an die API, wartet dann, bis die Generierung abgeschlossen ist, und lädt die resultierenden Modelldateien herunter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Gibt die KI-Modellversion an, die für die Generierung verwendet werden soll. | COMBO | Ja | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | Die Textbeschreibung des 3D-Modells, das Sie generieren möchten. Muss zwischen 1 und 600 Zeichen lang sein. Standardwert ist eine leere Zeichenkette. | STRING | Ja | 1 - 600 Zeichen |
| `style` | Der künstlerische Stil für das generierte 3D-Modell. | COMBO | Ja | `"realistic"` |
| `should_remesh` | Wenn auf false gesetzt, wird ein unverarbeitetes Dreiecksnetz zurückgegeben. Bei Auswahl von "true" werden zusätzliche Parameter für Topologie und Ziel-Polygonanzahl eingeblendet. | DYNAMIC_COMBO | Ja | `"true"`<br>`"false"` |
| `topology` | Der Ziel-Polygontyp für das neu vermaschte Modell. Dieser Parameter ist nur verfügbar, wenn `should_remesh` auf "true" gesetzt ist. | COMBO | Nein* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Die Zielanzahl an Polygonen für das neu vermaschte Modell. Standardwert ist 300000. Dieser Parameter ist nur verfügbar, wenn `should_remesh` auf "true" gesetzt ist. | INT | Nein* | 100 - 300000 |
| `symmetry_mode` | Steuert die Symmetrie im generierten Modell. Dies ist ein erweiterter Parameter. Optionen sind `"auto"`, `"on"` und `"off"`. | COMBO | Ja | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | Gibt den Posenmodus für das generierte Modell an. Eine leere Zeichenkette bedeutet, dass keine bestimmte Pose angefordert wird. Dies ist ein erweiterter Parameter. | COMBO | Ja | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standardwert ist 0. | INT | Ja | 0 - 2147483647 |
| `ultra_mode` | Führt einen zusätzlichen Verfeinerungsdurchlauf für eine höherwertige Geometrie mit feinerem Oberflächendetail aus. Standardwert ist false. | BOOLEAN | Ja | true<br>false |
| `ultra_resolution` | Auflösung des Ultra-Durchlaufs: `"2k"` führt ihn mit 2048³ aus, `"4k"` mit 4096³ für das feinste Oberflächendetail. 4k erfordert das Modell `"meshy-7.1"` oder `"latest"`. Wird nur verwendet, wenn `ultra_mode` aktiviert ist (Standard: `"2k"`). | COMBO | Nein | `"2k"`<br>`"4k"` |

*Hinweis: Die Parameter `topology` und `target_polycount` sind bedingt verfügbar. Sie erscheinen nur, wenn der Parameter `should_remesh` auf "true" gesetzt ist.

Wenn `ultra_mode` aktiviert ist, muss der Parameter `model` auf `"meshy-7.1"`, `"meshy-7"` oder `"latest"` gesetzt werden; jedes andere Modell führt zu einem Fehler. Bei `"meshy-7"` läuft der Ultra-Durchlauf immer mit 2048³, und die Ultra-Auflösung `"4k"` erfordert `"meshy-7.1"` oder `"latest"`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Der Dateiname des generierten GLB-Modells. Diese Ausgabe wird aus Gründen der Abwärtskompatibilität bereitgestellt. | STRING |
| `meshy_task_id` | Der eindeutige Bezeichner für die Meshy-API-Aufgabe. | MESHY_TASK_ID |
| `GLB` | Die generierte 3D-Modell-Datei im GLB-Format. | FILE3DGLB |
| `FBX` | Die generierte 3D-Modell-Datei im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/de.md)

---
**Source fingerprint (SHA-256):** `a02a5ae28bcae343c628d11ba3efa952b61b8bdf867669f58f1beb0f7c9e49f9`
