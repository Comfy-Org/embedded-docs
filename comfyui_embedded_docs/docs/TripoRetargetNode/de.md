# TripoRetargetNode

Der TripoRetargetNode wendet eine Preset-Animation auf ein vorhandenes geriggtes 3D-Modell an. Er verwendet die Task-ID eines zuvor geriggten Modells, sendet eine Retargeting-Anfrage an die Tripo-API und lädt die resultierende animierte Datei herunter. Das animierte Modell kann als GLB oder FBX zurückgegeben werden, mit optionaler Mesh-Geometrie und optionaler In-Place-Wiedergabe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | Die Task-ID des zuvor geriggten 3D-Modells, auf das das Retargeting angewendet werden soll. Die referenzierte Task muss eine Rig-Task sein. | RIG_TASK_ID | Ja | - |
| `animation` | Die Preset-Animation, die auf das geriggte Modell angewendet werden soll. `preset:*`-Animationen funktionieren mit beiden Rig-Modellen. `preset:biped:*`-Animationen sind für Rigs aus Modell v1.0-20240301 gedacht; ein v2.5-Rig akzeptiert nur chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn und walk. | COMBO | Ja | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>sowie zusätzliche `"preset:biped:*"`-Optionen, die in der Benutzeroberfläche angezeigt werden |
| `out_format` | Ausgabedateiformat; das Ergebnis erscheint am passenden Ausgang. (Standard: glb) | COMBO | Nein | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Mesh in den Export einschließen; deaktiviert wird nur das animierte Skelett exportiert. (Standard: True) | BOOLEAN | Nein | True<br>False |
| `animate_in_place` | Die Animation an Ort und Stelle abspielen, ohne Root-Verschiebung. (Standard: False) | BOOLEAN | Nein | True<br>False |
| `auth_token_comfy_org` | Authentifizierungstoken für den Comfy.org-API-Zugriff (versteckter Parameter). | AUTH_TOKEN_COMFY_ORG | Nein | - |
| `api_key_comfy_org` | API-Schlüssel für den Zugriff auf den Comfy.org-Dienst (versteckter Parameter). | API_KEY_COMFY_ORG | Nein | - |
| `unique_id` | Eindeutige Kennung zur Verfolgung des Vorgangs (versteckter Parameter). | UNIQUE_ID | Nein | - |

Hinweis: Animationen in der `preset:*`-Gruppe funktionieren mit beiden Rig-Modellen. Animationen in der `preset:biped:*`-Gruppe sind für Rigs aus Modell v1.0-20240301 gedacht; ein v2.5-Rig akzeptiert nur chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn und walk. Wenn das referenzierte Rig mit der Mixamo-Spezifikation und einer mit `v1.0` beginnenden Modellversion erstellt wurde, schlägt der Retargeting-Aufruf mit einem Fehler fehl. Das angeforderte Ausgabeformat muss GLB oder FBX sein; wenn der Dienst einen anderen Dateityp zurückgibt, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Die generierte animierte 3D-Modell-Datei (nur zur Abwärtskompatibilität). | STRING |
| `retarget task_id` | Die Task-ID zur Verfolgung des Retargeting-Vorgangs. | RETARGET_TASK_ID |
| `GLB` | Das animierte 3D-Modell im GLB-Format. Wird befüllt, wenn `out_format` glb ist. | FILE3DGLB |
| `FBX` | Das animierte 3D-Modell im FBX-Format. Wird befüllt, wenn `out_format` fbx ist. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/de.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
