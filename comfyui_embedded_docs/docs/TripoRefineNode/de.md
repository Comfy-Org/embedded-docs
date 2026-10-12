# TripoRefineNode

Der TripoRefineNode verfeinert 3D-Entwurfsmodelle, die speziell von Tripo v1.4-Modellen erstellt wurden. Er nimmt eine Modell-Task-ID entgegen und verarbeitet sie über die Tripo-API, um eine verbesserte Version des Modells zu erzeugen. Dieser Node ist darauf ausgelegt, ausschließlich mit Entwurfsmodellen zu arbeiten, die von Tripo v1.4-Modellen erzeugt wurden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Muss ein v1.4-Tripo-Modell sein | MODEL_TASK_ID | Ja | - |

**Hinweis:** Dieser Node akzeptiert nur Entwurfsmodelle, die von Tripo v1.4-Modellen erstellt wurden. Die Verwendung von Modellen aus anderen Versionen kann zu Fehlern führen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Der Dateipfad oder die Referenz zum verfeinerten Modell (nur aus Gründen der Abwärtskompatibilität) | STRING |
| `model task_id` | Die Task-Kennung für die Operation des verfeinerten Modells | MODEL_TASK_ID |
| `GLB` | Das verfeinerte 3D-Modell im GLB-Format | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/de.md)

---
**Source fingerprint (SHA-256):** `502064a5f153ed05b985f859f27b26eb5219427a17b876cfebedfdcf3194fe12`
