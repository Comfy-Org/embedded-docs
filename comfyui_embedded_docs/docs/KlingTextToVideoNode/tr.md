# Kling Metinden Videoya

ComfyUI Kling Metinden Videoya Düğümü, metin açıklamalarını video içeriğine dönüştürür. Metin istemlerini alır ve belirtilen yapılandırma ayarlarına göre karşılık gelen video dizilerini oluşturur. Düğüm, farklı en boy oranlarını ve üretim modlarını destekleyerek çeşitli süre ve kalitede videolar üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Olumlu metin istemi | STRING | Evet | - |
| `negatif_istem` | Olumsuz metin istemi | STRING | Evet | - |
| `cfg_ölçeği` | Yapılandırma ölçek değeri (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `en_boy_oranı` | Video en boy oranı ayarı (varsayılan: "16:9") | COMBO | Hayır | KlingVideoGenAspectRatio seçenekleri |
| `mod` | Video oluşturma için kullanılacak yapılandırma. Biçim: mod / süre / model_adı. (varsayılan: modes[8]) | COMBO | Hayır | Birden çok seçenek mevcut |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_kimliği` | Oluşturulan video çıktısı | VIDEO |
| `süre` | Oluşturulan video için benzersiz tanımlayıcı | STRING |
| `duration` | Oluşturulan videonun süre bilgisi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`
