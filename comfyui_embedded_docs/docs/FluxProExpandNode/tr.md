> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/tr.md)

İşte ComfyUI **FluxProExpandNode** düğüm belgesinin Türkçe çevirisi:

## Genel Bakış

Görüntüyü, verilen metin açıklamasına uygun yeni içerik oluşturarak, üst, alt, sol ve sağ taraflara piksel ekleyerek genişletir. Bu düğüm, bir görüntüyü istem (prompt) temelinde dışa doğru genişletir (outpaint).

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Genişletilecek giriş görüntüsü |
| `istem` | STRING | Hayır | - | Görüntü oluşturma için istem (varsayılan: "") |
| `istem_yükseltme` | BOOLEAN | Hayır | - | İstem üzerinde yukarı örnekleme (upsampling) yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı bir üretim için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum (seed) tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `üst` | INT | Hayır | 0-2048 | Görüntünün üst kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `alt` | INT | Hayır | 0-2048 | Görüntünün alt kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `sol` | INT | Hayır | 0-2048 | Görüntünün sol kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `sağ` | INT | Hayır | 0-2048 | Görüntünün sağ kısmına eklenecek piksel sayısı (varsayılan: 0) |
| `rehberlik` | FLOAT | Hayır | 1.5-100 | Görüntü oluşturma süreci için yönlendirme gücü (varsayılan: 60) |
| `adımlar` | INT | Hayır | 15-50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `tohum` | INT | Hayır | 0-18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Genişletilmiş çıktı görüntüsü |

---
**Source fingerprint (SHA-256):** `15b21f1de8a98a6bcde131a61c01b062434c6a959bc563550d613972412973fe`
