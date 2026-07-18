# Metin Yer Paylaşımı Çiz

Bu düğüm, bir görüntü veya görüntü grubu üzerine metin çizer. Özel metin, yazı tipi boyutu, renk, konum, hizalama ve isteğe bağlı bir anahat desteği sunarak metni orijinal görüntünün üzerine yerleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | Metin çizilecek giriş görüntüsü veya görüntü grubu. | IMAGE | Evet | |
| `metin` | Üzerine yerleştirilecek metin dizesi. Yeni satır (`\n`) ve sekme (`\t`) karakterlerini destekler. Varsayılan: "" | STRING | Evet | |
| `yazı tipi boyutu` | Görüntü yüksekliğinin yüzdesi olarak yazı tipi boyutu. Varsayılan: 5.0 | FLOAT | Evet | 0.5 ila 50.0 |
| `renk` | Metnin rengi. Varsayılan: "#ffffff" (beyaz) | STRING | Evet | |
| `konum` | Metnin görüntü üzerindeki dikey konumu. Varsayılan: "top" | COMBO | Evet | "top"<br>"bottom" |
| `hizalama` | Metnin yatay hizalaması. Varsayılan: "left" | COMBO | Evet | "left"<br>"center"<br>"right" |
| `dış çizgi` | Metnin etrafına siyah bir anahat çizer. Varsayılan: True | BOOLEAN | Evet | |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntüler` | Üzerine metin yerleştirilmiş görüntü veya görüntü grubu. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/tr.md)

---
**Source fingerprint (SHA-256):** `baffaa4ec9d3565e3533673658399271234def8c49e2e4a5f16767ec3f98cb22`
