# 3D-Modell speichern

Der Node SaveGLB speichert 3D-Mesh-Daten oder 3D-Dateieingaben im Ausgabeverzeichnis. Er akzeptiert Mesh-Daten und gängige 3D-Dateiformate (GLB, GLTF, OBJ, FBX, STL, USDZ, PLY, SPLAT, SPZ, KSPLAT) und exportiert sie mit dem angegebenen Dateinamenpräfix. Mesh-Eingaben werden als GLB-Dateien geschrieben, eine pro Batch-Element, während 3D-Dateieingaben im Originalformat gespeichert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Mesh- oder 3D-Datei zum Speichern | MESH oder FILE3D | Ja | Mesh data<br>GLB<br>GLTF<br>OBJ<br>FBX<br>STL<br>USDZ<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT<br>Any splat format<br>Any point cloud format<br>Any 3D file format |
| `filename_prefix` | Das Präfix für den Ausgabedateinamen (Standard: "3d/ComfyUI"). Das Präfix kann einen Unterordnerpfad enthalten, sodass Dateien standardmäßig unter dem Unterordner "3d" des Ausgabeverzeichnisses gespeichert werden | STRING | Nein | - |

Hinweis: Wenn die Eingabe `mesh` eine 3D-Datei ist, speichert der Node sie mit der Dateiendung ihres Originalformats (GLB wird verwendet, wenn die Datei kein Format hat). Wenn es sich um Mesh-Daten handelt, wird jedes Element im Batch als separate `.glb`-Datei gespeichert; leere Elemente (ohne Vertices oder Faces) werden mit einer Warnung übersprungen. Ausgabedateinamen folgen dem Muster `{filename_prefix}_{counter:05}_.{ext}` mit einem fortlaufend erhöhten Zähler. Workflow-Metadaten (Prompt und zusätzliche PNG-Informationen) werden in die gespeicherten Dateien eingebettet, wenn Metadaten aktiviert sind.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `ui` | Zeigt die gespeicherten 3D-Dateien in der Benutzeroberfläche mit Dateiname, Unterordner und Typinformationen an | UI |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/de.md)

---
**Source fingerprint (SHA-256):** `366b56c4fd6e3c2f7783222990792a982857b3419a2becfa27ddfa37853bb22c`
