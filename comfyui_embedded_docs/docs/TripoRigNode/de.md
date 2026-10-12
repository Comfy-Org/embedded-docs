# TripoRigNode

Dieser Node nimmt ein vorhandenes Tripo-3D-Modell und erstellt eine geriggte Version davon, das heißt, das Modell erhält ein Skelett, damit es animiert werden kann. Sie geben die Task-ID des zu riggenden Modells an, wählen Rig-Version, Skeletttyp, Knochenbenennungsstil und Ausgabedateiformat, und der Node sendet den Auftrag an Tripo, wartet, bis er abgeschlossen ist, und gibt anschließend das heruntergeladene Ergebnis zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `original_model_task_id` | Die Task-ID des ursprünglichen 3D-Modells, das geriggt werden soll. Dies ist normalerweise die ID, die von einem früheren Tripo-Modellgenerierungs-Node erzeugt wurde. | MODEL_TASK_ID | Ja | - |
| `model_version` | Zu verwendende Rig-Modellversion. v1.0: nur humanoide (bipedale) Charaktere, 90+ Animationsvoreinstellungen. v2.5: nicht-humanoide Kreaturen (quadruped, hexapod, octopod, avian, serpentine, aquatic). Standard: `v1.0-20240301`. | COMBO | Nein | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | Skeletttyp. "auto" führt zuerst Tripos kostenlosen Rig-Check aus und verwendet den empfohlenen Typ. Standard: "auto". | COMBO | Nein | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Knochenbenennung: Tripo-nativ oder Mixamo-kompatibel. Tripo kann seine Animationsvoreinstellungen nicht auf ein v1.0-Rig retargeten, das mit der mixamo-Spezifikation erstellt wurde; verwenden Sie tripo für Tripo: Retarget rigged model. Standard: "tripo". | COMBO | Nein | "tripo"<br>"mixamo" |
| `out_format` | Ausgabedateiformat; das Ergebnis wird an der passenden Ausgabe bereitgestellt. Standard: "glb". | COMBO | Nein | "glb"<br>"fbx" |

**Hinweis:** Die Modellversion v1.0 (`v1.0-20240301`) unterstützt nur Skelette vom Typ `biped`. Wenn mit dieser Version ein `rig_type` verwendet wird, der nicht `biped` ist, löst der Node einen Fehler aus und weist Sie an, stattdessen `v2.5-20260210` zu verwenden.

**Hinweis:** Wenn `rig_type` auf "auto" gesetzt ist, prüft Tripo zuerst, ob das Modell geriggt werden kann, und wählt den empfohlenen Skeletttyp. Wenn Tripo meldet, dass das Modell nicht geriggt werden kann, bricht der Node mit einem Fehler ab.

**Hinweis:** Der Node erwartet, dass Tripo eine GLB- oder FBX-Datei zurückgibt. Wenn Tripo einen anderen Dateityp zurückgibt, löst der Node einen Fehler aus.

**Hinweis:** Nur die zu `out_format` passende Ausgabe wird befüllt: `GLB`, wenn `out_format` "glb" ist, und `FBX`, wenn `out_format` "fbx" ist. Die andere 3D-Ausgabe bleibt leer.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `model_file` | Der Dateiname des generierten geriggten Modells (Task-ID plus Formatendung). Nur aus Gründen der Abwärtskompatibilität beibehalten. | STRING |
| `rig task_id` | Die Task-ID zur Verfolgung des Rig-Generierungsprozesses. | RIG_TASK_ID |
| `GLB` | Das geriggte Modell als GLB-3D-Datei. Wird befüllt, wenn `out_format` "glb" ist. | FILE3DGLB |
| `FBX` | Das geriggte Modell als FBX-3D-Datei. Wird befüllt, wenn `out_format` "fbx" ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/de.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
