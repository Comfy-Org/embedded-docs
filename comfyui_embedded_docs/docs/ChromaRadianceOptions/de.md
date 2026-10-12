# ChromaRadianceOptions

Der Node ChromaRadianceOptions ermöglicht es Ihnen, erweiterte Einstellungen für das Chroma Radiance-Modell zu konfigurieren. Er hängt einen Wrapper an ein vorhandenes Modell an und wendet die ausgewählten Optionen während des Denoising-Prozesses nur dann an, wenn der aktuelle Sigma-Wert innerhalb des konfigurierten Bereichs liegt, wodurch Sie die Kontrolle über die NeRF-Tile-Größe und die Handhabung von Text-Token-IDs erhalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, auf das Chroma Radiance-Optionen angewendet werden | MODEL | Ja | - |
| `preserve_wrapper` | Wenn aktiviert, wird an einen vorhandenen Wrapper einer Modellfunktion delegiert, falls ein solcher existiert. Im Allgemeinen sollte dies aktiviert bleiben. (Standard: True) | BOOLEAN | Nein | - |
| `start_sigma` | Erstes Sigma, bei dem diese Optionen wirksam sind. (Standard: 1.0) | FLOAT | Nein | 0.0 bis 1.0 |
| `end_sigma` | Letztes Sigma, bei dem diese Optionen wirksam sind. (Standard: 0.0) | FLOAT | Nein | 0.0 bis 1.0 |
| `nerf_tile_size` | Ermöglicht das Überschreiben der standardmäßigen NeRF-Tile-Größe. -1 bedeutet, den Standardwert (32) zu verwenden. 0 bedeutet, den Nicht-Tiling-Modus zu verwenden (kann viel VRAM erfordern). (Standard: -1) | INT | Nein | -1 und höher |
| `force_sequential_txt_ids` | Erzwingt die Verwendung sequenzieller Text-Token-IDs anstelle von Nullen. Sollte für Checkpoints vom 2026-05-22 bis 2026-06-01 verwendet werden, die auf diese Weise trainiert wurden, aber den Schlüssel `__sequential__` nicht im State Dict enthalten. (Standard: False) | BOOLEAN | Nein | - |

**Hinweis:** Die Chroma Radiance-Optionen werden nur wirksam, wenn der aktuelle Sigma-Wert zwischen `end_sigma` und `start_sigma` (einschließlich) liegt. Die Option `nerf_tile_size` wird nur angewendet, wenn sie auf 0 oder einen höheren Wert gesetzt ist (ein Wert von -1 verwendet die Standard-Tile-Größe von 32 und speichert kein Überschreiben). Die Option `force_sequential_txt_ids` wird nur angewendet, wenn sie auf True gesetzt ist. Wenn `nerf_tile_size` den Wert -1 hat und `force_sequential_txt_ids` False ist, werden keine Optionen konfiguriert und das Modell wird unverändert ohne angewendeten Wrapper zurückgegeben.

**Hinweis:** Alle Eingaben außer `model` sind erweiterte Optionen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model` | Das Modell mit angewendeten Chroma Radiance-Optionen oder das unveränderte Modell, wenn keine Optionen aktiv sind | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/de.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
