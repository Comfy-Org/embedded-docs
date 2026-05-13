> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/tr.md)

Görüntüyü Döşeme Listesine Böl düğümü, tek bir giriş görüntüsünü döşeme adı verilen bir dizi daha küçük, üst üste binen dikdörtgen bölüme ayırır. Bu döşemelerin toplu bir listesini oluşturur ve bu liste diğer düğümler tarafından ayrı ayrı işlenebilir. Her bir döşemenin boyutu ve aralarındaki örtüşme miktarı belirtilebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Döşemelere bölünecek giriş görüntüsü. |
| `tile_width` | INT | Evet | 64 ila 1048576 | Her bir çıktı döşemesinin piksel cinsinden genişliği (varsayılan: 1024). |
| `tile_height` | INT | Evet | 64 ila 1048576 | Her bir çıktı döşemesinin piksel cinsinden yüksekliği (varsayılan: 1024). |
| `overlap` | INT | Evet | 0 ila 4096 | Bitişik döşemelerin örtüşeceği piksel sayısı (varsayılan: 128). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Tüm bireysel görüntü döşemelerini içeren toplu bir liste. |

---
**Source fingerprint (SHA-256):** `26991a325b7b9358cd7338348e93c57695b1ed1aa1983962794f889c94c34547`
