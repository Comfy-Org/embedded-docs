# MarigoldV2PostProcess

Dieser Node konvertiert eine dekodierte Marigold V2-Vorhersage in ein anzeigbares Bild. Er nimmt den rohen Vorhersage-Tensor und formatiert ihn abhängig davon, um welche Art von Vorhersage es sich handelt: normalisierte Tiefe (nahe Objekte erscheinen hell), Oberflächennormalen mit Einheitslänge oder sRGB-Albedo.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Die dekodierte Marigold V2-Vorhersage, die in ein anzeigbares Bild umgewandelt werden soll. | IMAGE | Ja | - |
| `prediction` | Der Typ der im Eingang enthaltenen Vorhersage, der bestimmt, wie die Daten umgewandelt werden. `"depth"` normalisiert die Tiefenwerte, sodass nahe Flächen hell und entfernte Flächen dunkel sind, und kopiert das Ergebnis anschließend in alle drei Farbkanäle. `"normals"` skaliert die Werte auf den Bereich -1..1 neu, normalisiert sie zu Oberflächennormalen mit Einheitslänge und bildet sie zurück auf 0..1 ab. `"albedo"` wendet eine Linear-zu-sRGB-Konvertierung auf die Werte an. | COMBO | Ja | `"depth"`<br>`"normals"`<br>`"albedo"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das verarbeitete Bild in der ausgewählten Darstellung: normalisierte Tiefe (Graustufen, über drei Kanäle wiederholt), Oberflächennormalen mit Einheitslänge oder sRGB-Albedo. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/de.md)

---
**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`
