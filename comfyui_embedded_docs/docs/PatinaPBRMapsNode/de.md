# Patina PBR Material Maps

Leitet aus einem vorhandenen Texturbild eine Reihe von PBR-Materialmaps ab: Basecolor, Normal, Roughness, Metalness und Height. Aktivieren Sie nur die Maps, die Sie benötigen, da jede aktivierte Map die Kosten erhöht. Verwenden Sie den Node, um eine Textur zu vervollständigen, die noch keine Materialmaps hat, oder um eine einzelne beschädigte Map neu zu erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Foto oder Rendering, aus dem die PBR-Maps abgeleitet werden. | IMAGE | Ja | - |
| `basecolor` | Die Basecolor-(Albedo-)Map generieren. Standard: True. | BOOLEAN | Ja | true<br>false |
| `normal` | Die Normal-Map generieren. Standard: True. | BOOLEAN | Ja | true<br>false |
| `roughness` | Die Roughness-Map generieren. Standard: False. | BOOLEAN | Ja | true<br>false |
| `metalness` | Die Metalness-Map generieren. Standard: False. | BOOLEAN | Ja | true<br>false |
| `height` | Die Height-(Displacement-)Map generieren. Standard: False. | BOOLEAN | Ja | true<br>false |
| `seed` | Seed für reproduzierbares Denoising. Standard: 42. | INT | Ja | 0 bis 2147483646 |
| `safety_checker` | Führt die Inhaltssicherheitsprüfung des Anbieters für die Anfrage aus. Erweiterte Einstellung. Standard: False. | BOOLEAN | Ja | true<br>false |
| `auto_downscale` | Skaliert ein Eingabebild automatisch herunter, dessen längste Seite 2048 Pixel überschreitet – das Eingabelimit des Modells –, wobei das Seitenverhältnis beibehalten wird; kleinere Bilder bleiben unverändert. Deaktivieren Sie die Option, damit bei übergroßen Bildern stattdessen ein Fehler ausgegeben wird. Erweiterte Einstellung. Standard: True. | BOOLEAN | Nein | true<br>false |

**Einschränkungen und Verhalten:**

* Mindestens eine Map muss aktiviert sein, sonst schlägt die Ausführung fehl.
* Das Eingabebild ist auf 2048 Pixel an seiner längsten Seite begrenzt; lassen Sie es entweder durch `auto_downscale` verkleinern, oder die Ausführung schlägt bei einem übergroßen Bild fehl.
* Jede deaktivierte Map gibt trotzdem eine Ausgabe zurück, jedoch als 1x1-Platzhalterbild; verbinden Sie daher nur die Ausgaben, die Sie tatsächlich generiert haben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `basecolor` | Die generierte Basecolor-(Albedo-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `normal` | Die generierte Normal-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `roughness` | Die generierte Roughness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `metalness` | Die generierte Metalness-Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |
| `height` | Die generierte Height-(Displacement-)Map oder ein 1x1-Platzhalter, wenn diese Map deaktiviert ist. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/de.md)

---
**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`
