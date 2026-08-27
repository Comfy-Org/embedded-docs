# Kling Görüntüden Videoya

Kling Image to Video düğümü, başlangıç görüntüsünü ilk kare olarak kullanarak kısa bir video oluşturur. Görüntüyü metin istemleri ve oluşturma ayarlarıyla birleştirir ve elde edilen videoyu kimliği ve süresiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `başlangıç_karesi` | Videoyu oluşturmak için kullanılan referans görüntü. Görüntü en az 300x300 piksel olmalı ve en boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. | IMAGE | Evet | - |
| `istem` | Pozitif metin istemi. Boş olmamalıdır. En fazla 500 karakter. | STRING | Evet | - |
| `negatif_istem` | Negatif metin istemi. En fazla 500 karakter. Kullanılmıyorsa boş bırakın. | STRING | Evet | - |
| `model_adı` | Video oluşturma için kullanılan model (varsayılan: `"kling-v2-5-turbo"`). | COMBO | Evet | `"kling-v2-5-turbo"` |
| `cfg_ölçeği` | Videonun istemi ne kadar yakından takip edeceğini kontrol eder. Daha yüksek değerler daha güçlü bağlılık anlamına gelir (varsayılan: 0.8). | FLOAT | Evet | 0.0 ile 1.0 |
| `mod` | Oluşturma modu (varsayılan: `"pro"`). | COMBO | Evet | `"pro"` |
| `en_boy_oranı` | Oluşturulan videonun en boy oranı (varsayılan: `"16:9"`). | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `süre` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: `"5"`). | COMBO | Evet | `"5"`<br>`"10"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video çıktısı. | VIDEO |
| `video_kimliği` | Oluşturulan video için benzersiz tanımlayıcı. | STRING |
| `süre` | Oluşturulan video için süre bilgisi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
