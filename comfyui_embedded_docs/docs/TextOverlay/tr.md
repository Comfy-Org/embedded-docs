# Metin Yer Paylaşımı Çiz

Bu düğüm, bir görüntü veya görüntü grubu üzerine metin çizer. Özelleştirilebilir yazı tipi boyutu, renk, konum, hizalama ve isteğe bağlı bir anahat ile bir metin katmanı oluşturur ve ardından metni orijinal görüntülerin üzerine yerleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | Metin çizilecek giriş görüntüsü veya görüntü grubu | IMAGE | Evet | |
| `metin` | Görüntü üzerine yerleştirilecek metin (varsayılan: "") | STRING | Evet | |
| `yazı tipi boyutu` | Görüntü yüksekliğinin yüzdesi olarak yazı tipi boyutu (varsayılan: 5.0) | FLOAT | Evet | 0.5 ila 50.0 |
| `renk` | Metnin rengi (varsayılan: "#ffffff") | STRING | Evet | |
| `konum` | Metnin görüntü üzerindeki dikey konumu (varsayılan: "top") | COMBO | Evet | `"top"`<br>`"bottom"` |
| `hizalama` | Metnin yatay hizalaması (varsayılan: "left") | COMBO | Evet | `"left"`<br>`"center"`<br>`"right"` |
| `dış çizgi` | Metnin etrafına siyah bir anahat çizer (varsayılan: True) | BOOLEAN | Evet | |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntüler` | Üzerine metin katmanı yerleştirilmiş giriş görüntüleri | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/tr.md)

---
**Source fingerprint (SHA-256):** `baffaa4ec9d3565e3533673658399271234def8c49e2e4a5f16767ec3f98cb22`
