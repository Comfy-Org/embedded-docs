# Hunyuan3D: 3D-Teil

Dieser Node verwendet die Tencent Hunyuan3D API, um Komponenten eines 3D-Modells anhand seiner Struktur automatisch zu identifizieren und zu generieren. Er akzeptiert ein FBX-Modell, verarbeitet es und gibt eine neue FBX-Datei zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 3D-Modell im FBX-Format. Das Modell sollte weniger als 30000 Flächen haben. | FILE3D | Ja | FBX, Any |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Die Eingabe `model_3d` unterstützt nur Dateien im FBX-Format. Wenn ein anderes 3D-Dateiformat bereitgestellt wird, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `FBX` | Das verarbeitete 3D-Modell, zurückgegeben als FBX-Datei. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/de.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`
