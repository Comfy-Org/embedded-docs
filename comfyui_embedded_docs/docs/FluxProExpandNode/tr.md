> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/tr.md)

İşte ComfyUI **FluxProExpandNode** düğüm belgesinin Türkçe çevirisi:

## Genel Bakış

Görüntüyü, verilen metin açıklamasına uygun yeni içerik oluşturarak, üst, alt, sol ve sağ taraflara piksel ekleyerek genişletir. Bu düğüm, bir görüntüyü istem (prompt) temelinde dışa doğru genişletir (outpaint).

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Genişletilecek giriş görüntüsü |
| `prompt` | STRING | Hayır | - | Görüntü oluşturma için istem (varsayılan: "") |
| `prompt_upsampling` | BOOLEAN | Hayır | - | İstem üzerinde yukarı örnekleme (upsampling) yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı bir üretim için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum (seed) tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `top` | INT | Hayır | 0-2048 | Görüntünün üst kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `bottom` | INT | Hayır | 0-2048 | Görüntünün alt kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `left` | INT | Hayır | 0-2048 | Görüntünün sol kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `right` | INT | Hayır | 0-2048 | Görüntünün sağ kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `guidance` | FLOAT | Hayır | 1.5-100 | Görüntü oluşturma süreci için yönlendirme gücü (varsayılan: 60) |
| `steps` | INT | Hayır | 15-50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `seed` | INT | Hayır | 0-18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Genişletilmiş çıktı görüntüsü |

---
**Source fingerprint (SHA-256):** `15b21f1de8a98a6bcde131a61c01b062434c6a959bc563550d613972412973fe`
