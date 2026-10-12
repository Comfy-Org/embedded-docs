# TripoImageToModelNodeV2

Der Node Tripo: Image to Model wandelt ein einzelnes Referenzbild mithilfe des Bild-zu-Modell-Dienstes von Tripo in ein 3D-Modell um. Er lädt das Bild hoch, übermittelt einen Generierungsauftrag, wartet auf dessen Abschluss und gibt die resultierende 3D-Datei zusammen mit der Task-ID zurück. Dies ist ein API-Node, daher ist ein gültiger Comfy-API-Schlüssel erforderlich.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Referenzbild, das zur Generierung des 3D-Modells verwendet wird. | IMAGE | Ja | — |
| `model_version` | Die für die Generierung zu verwendende Modellversion. Wenn sie nicht festgelegt wird, verwendet der Node standardmäßig Tripos Version v3.1 (20260211). | COMBO | Nein | Liste der Tripo-Modellversionen |
| `texture` | Textur-Maps generieren. Aus liefert reine Geometrie und ignoriert `pbr` (Standard: true). | BOOLEAN | Nein | true<br>false |
| `pbr` | PBR-Material-Maps (Basisfarbe, Metallic, Rauheit, Normal). Erfordert `texture` (Standard: true). | BOOLEAN | Nein | true<br>false |
| `model_seed` | Seed für den Geometrie-Generierungsschritt (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `orientation` | Auf das generierte Modell angewendete Ausrichtungseinstellung (Standard: DEFAULT). | COMBO | Nein | Tripo-Orientierungsoptionen, Standard `DEFAULT` |
| `texture_seed` | Seed für den Textur-Generierungsschritt (Standard: 42). | INT | Nein | 0 bis 2147483647 |
| `texture_quality` | detailed = HD-Texturen, extreme = 8K-Ultra-Texturen (Standard: "standard"). | COMBO | Nein | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Wie Texturen auf der generierten Geometrie ausgerichtet werden (Standard: "original_image"). | COMBO | Nein | "original_image"<br>"geometry" |
| `face_limit` | Maximale Anzahl an Faces. -1 lässt Tripo adaptiv wählen (etwa 1,4 Mio. Faces bei v3.x standard, 2 Mio. bei detailed). Tripo begrenzt stillschweigend: v2.5 bei 500.000, Quad-Meshes bei 150.000 (Standard: -1). | INT | Nein | -1 bis 2000000 |
| `quad` | Quad-Mesh-Ausgabe. Tripo liefert Quad-Meshes als FBX, daher kommt das Ergebnis am FBX-Ausgang an und der GLB-Ausgang bleibt leer (Standard: false). | BOOLEAN | Nein | true<br>false |
| `geometry_quality` | Die Qualitätsstufe der generierten Geometrie (Standard: "standard"). | COMBO | Nein | "standard"<br>"detailed" |
| `smart_low_poly` | Low-Poly-Mesh mit sauberer Topologie im handgefertigten Stil (500–20.000 Faces, Quad 500–10.000). Am besten für einfache Motive geeignet; komplexe können fehlschlagen (Standard: false). | BOOLEAN | Nein | true<br>false |
| `auto_size` | Skaliert texturierte Modelle auf ihre reale Größe in Metern. Tripo speichert die Größe als Szenentransformation des Modells und backt sie ein, wenn das Modell konvertiert, geriggt oder retargetet wird; ohne Textur wird dies ignoriert (Standard: true). | BOOLEAN | Nein | true<br>false |

**Hinweise:**

- `image` ist erforderlich; der Node löst einen Fehler aus, wenn kein Bild bereitgestellt wird.
- Wenn `smart_low_poly` aktiviert ist und `face_limit` auf einen anderen Wert als -1 gesetzt ist, muss das Limit für Dreiecksmeshes zwischen 500 und 20.000 liegen oder zwischen 500 und 10.000, wenn `quad` aktiviert ist. Andere Werte lösen einen Fehler aus.
- Wenn `texture` deaktiviert ist, wird `pbr` unabhängig von seiner Einstellung zwangsweise deaktiviert, und `auto_size` hat keine Wirkung.
- Ein `face_limit` von -1 wird an Tripo als „kein Limit“ gesendet, wodurch der Dienst adaptiv wählen kann.
- Ein neues 3D-Dateiformat, das der Node nicht zurückgeben kann (alles andere als GLB oder FBX), verursacht einen Fehler.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model task_id` | Die Tripo-Task-ID des Generierungsauftrags. | MODEL_TASK_ID |
| `GLB` | Das generierte Modell als GLB-Datei. Leer, wenn `quad` aktiviert ist. | FILE3DGLB |
| `FBX` | Das generierte Modell als FBX-Datei. Wird nur befüllt, wenn `quad` aktiviert ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `c8c069432f67a019995b9f4dedbf5ca3f7594ae4004104277068106821189c11`
