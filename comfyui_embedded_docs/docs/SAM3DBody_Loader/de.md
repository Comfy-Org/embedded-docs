# SAM3D-Körpermodell laden

Lädt ein SAM3D-Body-Modell aus einer im Detection-Ordner gespeicherten Checkpoint-Datei und bereitet es für die Verwendung zur 3D-Körpererkennung vor. Der Node lädt die Modellgewichte, erkennt und wendet Quantisierungseinstellungen an, falls vorhanden, und umhüllt das Modell für die automatische Speicherverwaltung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_file` | Die zu ladende SAM3D-Body-Checkpoint-Datei. Die Datei muss im Detection-Ordner abgelegt werden. Alle im Detection-Ordner verfügbaren Modelldateien werden als Optionen aufgelistet. | COMBO | Ja | Alle im Detection-Ordner verfügbaren Modelldateien |

Hinweis: Die Modelldatei muss sich im Detection-Ordner befinden. Das Laden schlägt mit einem Fehler fehl, wenn die Schlüssel des State-Dictionarys des Checkpoints nicht mit der Struktur des SAM3D-Body-Modells übereinstimmen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `sam3d_body_model` | Das geladene SAM3D-Body-Modell, umhüllt für die automatische Speicherverwaltung zwischen GPU und CPU. Die Gewichte der Hand-Erkennung werden entfernt, sodass das Modell ausschließlich auf die Körpererkennung spezialisiert ist. | SAM3D_BODY_MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Loader/de.md)

---
**Source fingerprint (SHA-256):** `c66a1639b5f19dafcfb1466d68908969a4d33ab0d01c30e8b31d1f1ce41fd782`
