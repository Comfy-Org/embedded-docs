> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/tr.md)

Görüntüyü Döşeme Listesine Böl düğümü, tek bir giriş görüntüsünü döşeme adı verilen bir dizi daha küçük, örtüşen dikdörtgen bölüme ayırır. Bu döşemelerin toplu bir listesini oluşturur ve bu liste diğer düğümler tarafından ayrı ayrı işlenebilir. Her bir döşemenin boyutu ve aralarındaki örtüşme miktarı belirtilebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Döşemelere bölünecek giriş görüntüsü. |
| `tile_width` | INT | Hayır | 64 ila 1048576 | Her bir çıktı döşemesinin piksel cinsinden genişliği (varsayılan: 1024). |
| `tile_height` | INT | Hayır | 64 ila 1048576 | Her bir çıktı döşemesinin piksel cinsinden yüksekliği (varsayılan: 1024). |
| `overlap` | INT | Hayır | 0 ila 4096 | Bitişik döşemelerin örtüşeceği piksel sayısı (varsayılan: 128). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Tüm bireysel görüntü döşemelerini içeren toplu bir liste. |