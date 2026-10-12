# Modell-Attention-Backend

Dieser Node wählt die Dense-Attention-Implementierung für ein Modell aus, klont das Modell, wendet das ausgewählte Backend an und gibt den gepatchten Klon zurück. In Kombination mit Block Sparse Attention wird dieses Backend verwendet, wann immer Sparse Attention inaktiv oder nicht unterstützt ist. Wenn das ausgewählte Backend nicht verfügbar ist, fällt der Node automatisch auf PyTorch Attention zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|---------|
| `model` | Das zu patchende Modell. | MODEL | Ja |  |
| `attention` | Das anzuwendende Dense-Attention-Backend. Comfy Kitchen Attention verwendet quantisierte INT8-Attention und ist nur auf Nvidia- und AMD-GPUs verfügbar. Standard: "pytorch attention". Wenn das ausgewählte Backend nicht verfügbar ist, wird PyTorch Attention als Fallback verwendet. | COMBO | Ja | "pytorch attention"<br>"comfy kitchen attention" |

Hinweis: Die Option "comfy kitchen attention" wird nur aufgeführt, wenn das Comfy Kitchen INT8-Attention-Modul in der aktuellen Umgebung verfügbar ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|-----------|
| `model` | Ein Klon des Eingabemodells, auf den das ausgewählte Attention-Backend angewendet wurde. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/de.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
