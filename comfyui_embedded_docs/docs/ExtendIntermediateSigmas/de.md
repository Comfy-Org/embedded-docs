# ExtendIntermediateSigmas

Der Node ExtendIntermediateSigmas nimmt eine vorhandene Sequenz von Sigma-Werten und fügt zusätzliche intermediäre Sigma-Werte zwischen ihnen ein. Er ermöglicht die Angabe, wie viele zusätzliche Schritte hinzugefügt werden sollen, der Methode zur Abstandsverteilung für die Interpolation sowie optionaler Start- und End-Sigma-Grenzen, um zu steuern, wo die Erweiterung innerhalb der Sigma-Sequenz erfolgt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `sigmas` | Die Eingabe-Sigma-Sequenz, die um intermediäre Werte erweitert werden soll | SIGMAS | Ja | - |
| `steps` | Steuert die Anzahl der intermediären Sigma-Werte, die zwischen jedem Paar vorhandener Sigmas eingefügt werden. Das Intervall zwischen zwei Sigmas wird in `steps` Teile unterteilt, wodurch pro Paar `steps - 1` neue Werte entstehen (Standard: 2, wodurch ein Wert pro Paar eingefügt wird) | INT | Ja | 1 bis 100 |
| `start_at_sigma` | Obere Sigma-Grenze für die Erweiterung. Nur Sigma-Intervalle, deren Start-Sigma kleiner oder gleich diesem Wert ist, werden erweitert. Wenn auf -1.0 gesetzt, wird dies als Unendlich behandelt, d. h. es wird keine Obergrenze angewendet. Standard: -1.0 | FLOAT | Ja | -1.0 bis 20000.0 |
| `end_at_sigma` | Untere Sigma-Grenze für die Erweiterung. Nur Sigma-Intervalle, deren Start-Sigma größer oder gleich diesem Wert ist, werden erweitert. Standard: 12.0 | FLOAT | Ja | 0.0 bis 20000.0 |
| `spacing` | Die Interpolationsmethode für die Abstandsverteilung der intermediären Sigma-Werte (Standard: "linear") | COMBO | Ja | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Hinweis:** Der Node fügt nur intermediäre Sigmas für Sigma-Intervalle ein, bei denen das Start-Sigma kleiner oder gleich `start_at_sigma` und größer oder gleich `end_at_sigma` ist. Wenn `start_at_sigma` auf -1.0 gesetzt ist, wird dies als Unendlich behandelt, sodass nur die untere Grenze `end_at_sigma` gilt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Die erweiterte Sigma-Sequenz mit zusätzlich eingefügten intermediären Werten | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/de.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
