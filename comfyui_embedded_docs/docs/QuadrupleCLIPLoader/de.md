# QuadrupleClipLoader

Der Quadruple CLIP Loader, QuadrupleCLIPLoader, ist einer der Kern-Nodes von ComfyUI und wurde ursprünglich hinzugefügt, um das Modell HiDream I1 zu unterstützen. Wenn dieser Node fehlt, versuchen Sie, ComfyUI auf die neueste Version zu aktualisieren, um die Node-Unterstützung sicherzustellen.

Er benötigt 4 CLIP-Modelle, die den Parametern `clip_name1`, `clip_name2`, `clip_name3` und `clip_name4` entsprechen, und stellt eine CLIP-Modell-Ausgabe für nachfolgende Nodes bereit.

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/text_encoders`
 und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind.
 Manchmal müssen Sie nach dem Hinzufügen von Modellen die **ComfyUI-Oberfläche neu laden**, damit sie die Modelldateien im entsprechenden Ordner lesen kann.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/de.md)
