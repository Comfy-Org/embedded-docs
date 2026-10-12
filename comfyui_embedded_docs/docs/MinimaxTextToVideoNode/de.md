# MinimaxTextToVideoNode

Erzeugt synchron Videos basierend auf einem Text-Prompt und optionalen Parametern über die API von MiniMax. Dieser Node erstellt Videoinhalte aus Textbeschreibungen, indem er eine Verbindung zum Text-zu-Video-Dienst von MiniMax herstellt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt_text` | Text-Prompt zur Steuerung der Videoerzeugung | STRING | Ja | - |
| `model` | Modell, das für die Videoerzeugung verwendet wird (Standard: "T2V-01") | COMBO | Nein | "T2V-01"<br>"T2V-01-Director" |
| `seed` | Der Zufalls-Seed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0) | INT | Nein | 0 bis 18446744073709551615 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `output` | Das generierte Video basierend auf dem Eingabe-Prompt | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `1d389bdcc48f903e04dad043a8609250f34466b9084b1319c411e155a8040422`
