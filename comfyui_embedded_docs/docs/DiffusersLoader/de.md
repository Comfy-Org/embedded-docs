# Diffusers-Modell laden (VERALTET)

The DiffusersLoader-Node lädt vortrainierte Modelle, die im Diffusers-Format gespeichert wurden. Er durchsucht die konfigurierten `diffusers`-Ordner nach Verzeichnissen, die eine `model_index.json`-Datei enthalten, ermöglicht die Auswahl eines Verzeichnisses und lädt es als MODEL-, CLIP- und VAE-Komponenten, die in der Pipeline verwendet werden. Dieser Node ist veraltet, bleibt jedoch aus Kompatibilitätsgründen mit Hugging Face Diffusers-Modellen verfügbar.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_path` | Der Pfad zum zu ladenden Diffusers-Modellverzeichnis. Der Node durchsucht automatisch die konfigurierten `diffusers`-Ordner (einschließlich verknüpfter Unterordner) nach Verzeichnissen, die eine `model_index.json`-Datei enthalten, und listet die verfügbaren Optionen auf. Der ausgewählte Pfad wird vor dem Laden validiert; ein ungültiges oder fehlendes Modell löst einen Fehler aus. | COMBO | Ja | Automatisch gefüllte Liste von Ordnern, die `model_index.json` enthalten<br>(relative Pfade innerhalb der konfigurierten `diffusers`-Ordner) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-----------|-------------|-----------|
| `MODEL` | Die geladene Modellkomponente aus dem Diffusers-Format. | MODEL |
| `CLIP` | Die geladene CLIP-Modellkomponente aus dem Diffusers-Format. | CLIP |
| `VAE` | Die geladene VAE-Komponente (Variational Autoencoder) aus dem Diffusers-Format. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/de.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
