# Flux.1 Görüntüyü Genişlet

İşte ComfyUI **FluxProExpandNode** düğüm belgesinin Türkçe çevirisi:

## Genel Bakış

Görüntüyü, verilen metin açıklamasına uygun yeni içerik oluşturarak, üst, alt, sol ve sağ taraflara piksel ekleyerek genişletir. Bu düğüm, bir görüntüyü istem (prompt) temelinde dışa doğru genişletir (outpaint).

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Genişletilecek giriş görüntüsü | IMAGE | Evet | - |
| `istem` | Görüntü oluşturma için istem (varsayılan: "") | STRING | Hayır | - |
| `istem_yükseltme` | İstem üzerinde yukarı örnekleme (upsampling) yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı bir üretim için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum (seed) tam olarak aynı sonucu üretmez). (varsayılan: False) | BOOLEAN | Hayır | - |
| `üst` | Görüntünün üst kısmına eklenecek piksel sayısı (varsayılan: 0) | INT | Hayır | 0-2048 |
| `alt` | Görüntünün alt kısmına eklenecek piksel sayısı (varsayılan: 0) | INT | Hayır | 0-2048 |
| `sol` | Görüntünün sol kısmına eklenecek piksel sayısı (varsayılan: 0) | INT | Hayır | 0-2048 |
| `sağ` | Görüntünün sağ kısmına eklenecek piksel sayısı (varsayılan: 0) | INT | Hayır | 0-2048 |
| `rehberlik` | Görüntü oluşturma süreci için yönlendirme gücü (varsayılan: 60) | FLOAT | Hayır | 1.5-100 |
| `adımlar` | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) | INT | Hayır | 15-50 |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) | INT | Hayır | 0-18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Genişletilmiş çıktı görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/tr.md)

---
**Source fingerprint (SHA-256):** `15b21f1de8a98a6bcde131a61c01b062434c6a959bc563550d613972412973fe`
