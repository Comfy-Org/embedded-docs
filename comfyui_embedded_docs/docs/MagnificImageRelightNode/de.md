# Magnific Bild-Neubeleuchtung

Der Magnific Image Relight-Node passt die Beleuchtung eines Eingabebildes an. Er kann eine stilistische Beleuchtung basierend auf einem Text-Prompt anwenden oder die Beleuchtungseigenschaften von einem optionalen Referenzbild übertragen. Der Node bietet verschiedene Steuerungsmöglichkeiten zur Feinabstimmung von Helligkeit, Kontrast und der Gesamtstimmung der endgültigen Ausgabe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Bild, dessen Beleuchtung angepasst werden soll. Es ist genau ein Bild erforderlich. Die Mindestabmessungen betragen 160x160 Pixel. Das Seitenverhältnis muss zwischen 1:3 und 3:1 liegen. | IMAGE | Ja | N/A |
| `prompt` | Beschreibende Anleitung für die Beleuchtung. Unterstützt Hervorhebungsnotation (1-1.4). Standard ist eine leere Zeichenkette. | STRING | Nein | N/A |
| `light_transfer_strength` | Intensität der Lichttransferanwendung. Standard: 100. | INT | Ja | 0 bis 100 |
| `style` | Stilistische Ausgabepräferenz. | COMBO | Ja | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` |
| `interpolate_from_original` | Schränkt die Generierungsfreiheit ein, um das Original genauer zu treffen. Standard: False. | BOOLEAN | Ja | N/A |
| `change_background` | Ändert den Hintergrund basierend auf Prompt/Referenz. Standard: True. | BOOLEAN | Ja | N/A |
| `preserve_details` | Behält Textur und feine Details aus dem Original bei. Standard: True. | BOOLEAN | Ja | N/A |
| `advanced_settings` | Feinabstimmungsoptionen für erweiterte Lichtsteuerung. Wenn auf `"enabled"` gesetzt, werden zusätzliche Parameter verfügbar. | DYNAMICCOMBO | Ja | `"disabled"`<br>`"enabled"` |
| `reference_image` | Optionales Referenzbild, von dem die Beleuchtung übertragen wird. Falls angegeben, ist genau ein Bild erforderlich. Die Mindestabmessungen betragen 160x160 Pixel. Das Seitenverhältnis muss zwischen 1:3 und 3:1 liegen. | IMAGE | Nein | N/A |

**Hinweis zu erweiterten Einstellungen:** Wenn `advanced_settings` auf `"enabled"` gesetzt ist, werden die folgenden verschachtelten Parameter aktiv:

* `whites`: Passt die hellsten Töne im Bild an. Bereich: 0 bis 100. Standard: 50.
* `blacks`: Passt die dunkelsten Töne im Bild an. Bereich: 0 bis 100. Standard: 50.
* `brightness`: Gesamtanpassung der Helligkeit. Bereich: 0 bis 100. Standard: 50.
* `contrast`: Kontrastanpassung. Bereich: 0 bis 100. Standard: 50.
* `saturation`: Farbsättigungsanpassung. Bereich: 0 bis 100. Standard: 50.
* `engine`: Auswahl der Verarbeitungs-Engine. Optionen: `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
* `transfer_light_a`: Die Intensität des Lichttransfers. Optionen: `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
* `transfer_light_b`: Ändert ebenfalls die Intensität des Lichttransfers. Kann mit der vorherigen Steuerung kombiniert werden, um unterschiedliche Effekte zu erzielen. Optionen: `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
* `fixed_generation`: Sorgt für konsistente Ausgabe bei denselben Einstellungen. Standard: True.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das neu beleuchtete Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/de.md)

---
**Source fingerprint (SHA-256):** `45fe68b21e1da7c367800915c803ad4cf1c5b80e9a2e91d80cae51b8a9531144`
