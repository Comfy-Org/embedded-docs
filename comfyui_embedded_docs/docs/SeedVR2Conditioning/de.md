# SeedVR2Conditioning

Erstellt positive und negative Konditionierung aus einem VAE-Latent zur Verwendung mit dem SeedVR2-Modell. Es validiert das Eingabe-Latent und die Modellstruktur, fügt dem Latent einen Maskenkanal hinzu und gibt beide Conditioning-Ausgaben zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das SeedVR2-Modell. | MODEL | Ja | - |
| `vae_conditioning` | Das SeedVR2-VAE-Latent, aus dem die Konditionierung erstellt wird (Anzeigename: latent). | LATENT | Ja | - |

Hinweis: Das `vae_conditioning`-Latent muss ein 5-D-Tensor im Comfy-Channel-First-Layout (B, C, T, H, W) sein, wobei C die erwartete Kanalanzahl des SeedVR2-VAE ist. Der Node löst einen Fehler aus, wenn das Latent nicht 5-D ist, wenn die Kanalanzahl nicht übereinstimmt oder wenn der Tensor im Channel-Last-Layout vorzuliegen scheint. Die Eingabe `model` muss die erwartete SeedVR2-Struktur aufweisen; der Node löst ihr internes Diffusionsmodell auf und liest dessen positive und negative Konditionierung aus. Intern fügt der Node dem Latent einen konstanten Maskenkanal hinzu und hängt die resultierende Konditionierung sowohl an die positive als auch an die negative Conditioning-Ausgabe an.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Die positive Konditionierung für das Sampling. | CONDITIONING |
| `negative` | Die negative Konditionierung für das Sampling. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
