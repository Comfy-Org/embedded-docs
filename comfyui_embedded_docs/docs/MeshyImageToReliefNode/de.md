# Meshy: Image to Relief

Dieser Node verwandelt ein Foto in ein Basrelief-Modell sowie eine 16-Bit-Tiefenkarte für den 3D-Druck, die Lasergravur und das CNC-Fräsen. Dunkle Motive auf einem hellen Hintergrund werden erhaben dargestellt, helle Bereiche bleiben niedrig. Nur die Ausgaben, die Sie verbinden, werden generiert und heruntergeladen. Ist also keine Modellausgabe verbunden, liefert die Aufgabe nur die Tiefenkarte.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Foto, das in ein Relief umgewandelt werden soll. Dunkle Motive auf einem hellen Hintergrund werden erhaben dargestellt. Transparenz wird vor dem Hochladen entfernt, flachen Sie ein transparentes Logo daher zuerst auf einem weißen Hintergrund ab. | IMAGE | Ja | Einzelbild |
| `relief_type` | Schnitzvoreinstellung. `"low"` ist eine flache Gravur für Lasergravur, CNC-Arbeiten und Schilder; `"high"` ist tiefer für 3D-gedruckte Stücke. Die Voreinstellung legt den Wert von `carving_depth_mm` fest. | DYNAMIC_COMBO | Ja | `"low"`<br>`"high"` |
| `carving_depth_mm` | Tiefe der Gravur in Millimetern. Verfügbar, wenn `relief_type` gesetzt ist (Standard: 3.0 für `"low"`, 6.0 für `"high"`). | FLOAT | Ja | 0.1 bis 60.0 (Schritt 0.1) |
| `size_mm` | Länge der längeren Seite des Fotos auf dem Modell in Millimetern, flach gemessen vor jeglicher Biegung (Standard: 60.0). | FLOAT | Ja | 20.0 bis 250.0 (Schritt 1.0) |
| `carving_mode` | `"emboss"` hebt die näheren Teile des Fotos hervor, `"engrave"` schneidet sie ein. | COMBO | Ja | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` behält eine Grundplatte unter dem Relief bei, `"none"` schneidet den Hintergrund weg und erzeugt keine Platte. Die Auswahl einer Option zeigt deren Parameter an. | DYNAMIC_COMBO | Ja | `"plate"`<br>`"none"` |
| `base_thickness_mm` | Dicke der Grundplatte in Millimetern. Verfügbar, wenn `base` auf `"plate"` gesetzt ist (Standard: 1.0). | FLOAT | Ja | 0.1 bis 10.0 (Schritt 0.1) |
| `removal_threshold` | Tiefe, unterhalb derer der Hintergrund weggeschnitten wird, auf der Tiefenkarte von 0 bis 1. 0.3 hält eine Büste als Ganzes zusammen, 0.8 zerlegt sie in Fragmente. Verfügbar, wenn `base` auf `"none"` gesetzt ist (Standard: 0.01). | FLOAT | Ja | 0.01 bis 1.0 (Schritt 0.01) |
| `bend` | `"convex"` wölbt die Vorderseite nach außen, `"concave"` krümmt sie nach innen, `"off"` hält das Relief flach. Die Auswahl einer Biegung zeigt `bend_axis` und `bend_angle` an. | DYNAMIC_COMBO | Ja | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` rollt die linken und rechten Kanten ein, `"yz"` die oberen und unteren Kanten. Verfügbar, wenn `bend` auf `"convex"` oder `"concave"` gesetzt ist. | COMBO | Ja | `"xz"`<br>`"yz"` |
| `bend_angle` | Bogen, den die Biegung in Grad umfasst; 360 schließt das Relief zu einem Zylinder. Verfügbar, wenn `bend` auf `"convex"` oder `"concave"` gesetzt ist (Standard: 60.0). | FLOAT | Ja | 1.0 bis 360.0 (Schritt 1.0) |
| `seed` | Seed, der steuert, ob der Node erneut ausgeführt wird; das Ergebnis ist ungeachtet des Seeds nicht deterministisch. Ändern Sie ihn, um eine Ausgabe anzufordern, die nach dem letzten Lauf verbunden wurde (Standard: 42). | INT | Ja | 0 bis 2147483647 |
| `mesh_resolution` | Netzpunkte entlang der längeren Seite des Fotos. Bei 1024 ist das GLB etwa 50 MB und das STL etwa 105 MB groß, bei 2048 etwa 200 MB und 420 MB; eine Biegung verdoppelt diese Werte. (Standard: 1024; erweiterte Option) | INT | Ja | 512 bis 2048 |
| `color_mapping` | Färbt die Dateien GLB, OBJ, FBX und USDZ mit dem Foto ein. STL und 3MF bleiben weiß. (Standard: False; erweiterte Option) | BOOLEAN | Ja | True / False |

**Hinweis:** Ein Modellformat wird nur generiert und heruntergeladen, wenn seine Ausgabe verbunden ist. Ist keine Modellausgabe verbunden, liefert die Aufgabe nur die Tiefenkarte. Bei alleiniger `preview`-Ausgabe wird das Modell dennoch für das Vorschaubild generiert, es wird jedoch keine Modelldatei zurückgegeben. `depth_map` behält den vollen 16-Bit-Bereich; Save Image (Advanced) schreibt sie als 16-Bit-PNG.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `GLB` | Das heruntergeladene Reliefmodell im GLB-Format. | FILE3DGLB |
| `STL` | Das heruntergeladene Reliefmodell im STL-Format. | FILE3DSTL |
| `OBJ` | Das heruntergeladene Reliefmodell im OBJ-Format. | FILE3DOBJ |
| `FBX` | Das heruntergeladene Reliefmodell im FBX-Format. | FILE3DFBX |
| `USDZ` | Das heruntergeladene Reliefmodell im USDZ-Format. | FILE3DUSDZ |
| `3MF` | Das heruntergeladene Reliefmodell im 3MF-Format. | FILE3D |
| `depth_map` | Tiefenkarte mit dem vollen 16-Bit-Bereich; Save Image (Advanced) schreibt sie als 16-Bit-PNG. | IMAGE |
| `preview` | Vom Meshy gerendertes Vorschaubild für das fertige Relief. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/de.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
