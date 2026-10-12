# TencentModelTo3DUVNode

Dieser Node verwendet die Tencent Hunyuan3D API, um eine UV-Entfaltung an einem 3D-Modell durchzuführen. Er nimmt eine 3D-Modell-Datei als Eingabe entgegen, sendet sie zur Verarbeitung an die API und gibt das verarbeitete Modell in den Formaten OBJ und FBX sowie ein generiertes UV-Texturbild zurück. Das Eingabemodell muss weniger als 30.000 Flächen haben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Eingabe-3D-Modell (GLB, OBJ oder FBX). Das Modell muss weniger als 30.000 Flächen haben. | FILE3D | Ja | GLB<br>OBJ<br>FBX |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 1) | INT | Nein | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `OBJ` | Die verarbeitete 3D-Modell-Datei im OBJ-Format. | FILE3D |
| `FBX` | Die verarbeitete 3D-Modell-Datei im FBX-Format. | FILE3D |
| `uv_image` | Das generierte UV-Texturbild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/de.md)

---
**Source fingerprint (SHA-256):** `b69519df055043555ab7f4d75cfb3b77b9011d5a8e93d0b3ba30c7a8674bd2cb`
