# Metin Yer Paylaşımı Çiz

Bu düğüm, bir görüntünün veya bir görüntü grubunun üzerine metin çizer. Yapılandırılabilir yazı tipi boyutu, renk, dikey konum, yatay hizalama ve isteğe bağlı siyah dış çizgi kullanarak bir metin katmanı oluşturur, ardından bu katmanı özgün görüntü pikselleriyle birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | Üzerine metin çizilecek girdi görüntüsü veya görüntü grubu | IMAGE | Evet | |
| `metin` | Görüntünün üzerine bindirilecek metin (varsayılan: ""). Çok satırı destekler: `\n` ve `\t` kaçış dizileri yeni satır ve sekme karakterlerine dönüştürülür ve uzun satırlar görüntü genişliğine sığacak şekilde otomatik olarak kaydırılır. | STRING | Evet | |
| `yazı tipi boyutu` | Görüntü yüksekliğinin yüzdesi olarak yazı tipi boyutu (varsayılan: 5.0) | FLOAT | Evet | 0.5 - 50.0 (adım 0.5) |
| `renk` | Metnin rengi (varsayılan: "#ffffff") | COLOR | Evet | |
| `konum` | Metnin görüntü üzerindeki dikey konumu (varsayılan: "top") | COMBO | Evet | "top"<br>"bottom" |
| `hizalama` | Metnin yatay hizalaması (varsayılan: "left") | COMBO | Evet | "left"<br>"center"<br>"right" |
| `dış çizgi` | Metnin çevresine siyah dış çizgi çizer (varsayılan: True) | BOOLEAN | Evet | |

Not: `text` boşsa veya yalnızca boşluk karakterleri içeriyorsa, düğüm girdi görüntülerini değiştirmeden döndürür. Metin katmanı bir kez oluşturulur ve gruptaki her görüntüye uygulanır. Oluşturulan metin bloğu kullanılabilir görüntü alanından daha yüksekse, sığana veya minimum boyuta ulaşana kadar yazı tipi boyutu otomatik olarak küçültülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Metin katmanı üzerine yerleştirilmiş girdi görüntüleri | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/tr.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
