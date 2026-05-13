> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/tr.md)

Kling Image(First Frame) to Video with Audio düğümü, tek bir başlangıç görüntüsü ve bir metin istemi kullanarak Kling AI modeli aracılığıyla kısa bir video oluşturur. Sağlanan görüntüyle başlayan bir video dizisi oluşturur ve isteğe bağlı olarak görüntülere eşlik etmesi için yapay zeka tarafından oluşturulmuş ses içerebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_adı` | COMBO | Evet | `"kling-v2-6"` | Video oluşturma için kullanılacak Kling AI modelinin belirli sürümü. |
| `başlangıç_kare` | IMAGE | Evet | - | Oluşturulan videonun ilk karesi olarak kullanılacak görüntü. Görüntü en az 300x300 piksel olmalı ve en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. |
| `istem` | STRING | Evet | - | Olumlu metin istemi. Oluşturmak istediğiniz video içeriğini tanımlar. İstem 1 ile 2500 karakter arasında olmalıdır. |
| `mod` | COMBO | Evet | `"pro"` | Video oluşturma için çalışma modu. |
| `süre` | COMBO | Evet | `5`<br>`10` | Oluşturulacak videonun saniye cinsinden uzunluğu. |
| `ses_oluştur` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, düğüm videoya eşlik etmesi için ses oluşturur. Devre dışı bırakıldığında, video sessiz olur. (varsayılan: True) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | `ses_oluştur` girişine bağlı olarak ses içerebilen oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`
