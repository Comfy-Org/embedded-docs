# TripoRigCheckNode

Dieser Node sendet die ID einer abgeschlossenen Tripo-3D-Modellaufgabe an die Tripo-API und prüft, ob dieses Modell geriggt werden kann. Er wartet, bis die Prüfung abgeschlossen ist, und gibt dann ein Ja/Nein-Ergebnis sowie den von Tripo empfohlenen Skeletttyp für das Modell zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Die Tripo-Aufgaben-ID des zu analysierenden Modells. Sie identifiziert ein Modell, das zuvor generiert, importiert oder anderweitig über eine Tripo-Aufgabe erstellt wurde. | MODEL_TASK_ID | Ja | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `riggable` | Gibt an, ob das Modell geriggt werden kann. | BOOLEAN |
| `rig_type` | Empfohlenes Skelett: biped, quadruped, hexapod, octopod, avian, serpentine oder aquatic; 'others', wenn das Modell nicht geriggt werden kann. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/de.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`
