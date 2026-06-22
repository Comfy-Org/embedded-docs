# Kling Görsel (İlk Kare) ile Videoya ve Sesli

Kling Image(First Frame) to Video with Audio düğümü, tek bir başlangıç görüntüsü ve bir metin istemi kullanarak Kling AI modeli aracılığıyla kısa bir video oluşturur. Sağlanan görüntüyle başlayan bir video dizisi oluşturur ve isteğe bağlı olarak görüntülere eşlik etmesi için yapay zeka tarafından oluşturulmuş ses içerebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_adı` | Video oluşturma için kullanılacak Kling AI modelinin belirli sürümü. | COMBO | Evet | `"kling-v2-6"` |
| `başlangıç_kare` | Oluşturulan videonun ilk karesi olarak kullanılacak görüntü. Görüntü en az 300x300 piksel olmalı ve en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Evet | - |
| `istem` | Olumlu metin istemi. Oluşturmak istediğiniz video içeriğini tanımlar. İstem 1 ile 2500 karakter arasında olmalıdır. | STRING | Evet | - |
| `mod` | Video oluşturma için çalışma modu. | COMBO | Evet | `"pro"` |
| `süre` | Oluşturulacak videonun saniye cinsinden uzunluğu. | COMBO | Evet | `5`<br>`10` |
| `ses_oluştur` | Etkinleştirildiğinde, düğüm videoya eşlik etmesi için ses oluşturur. Devre dışı bırakıldığında, video sessiz olur. (varsayılan: True) | BOOLEAN | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | `ses_oluştur` girişine bağlı olarak ses içerebilen oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/tr.md)

---
**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`
