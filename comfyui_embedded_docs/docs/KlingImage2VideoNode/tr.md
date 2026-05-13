> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/tr.md)

## Giriş

Kling Görüntüden Videoya Düğümü, bir başlangıç referans görüntüsü kullanarak metin istemleri aracılığıyla video oluşturur. İlk kare olarak bir görüntü alır ve pozitif ile negatif metin açıklamalarına dayanarak, model, süre, en-boy oranı ve oluşturma modu gibi yapılandırılabilir seçeneklerle bir video dizisi oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `başlangıç_karesi` | IMAGE | Evet | - | Videoyu oluşturmak için kullanılan referans görüntüsü. |
| `istem` | STRING | Evet | - | Pozitif metin istemi. |
| `negatif_istem` | STRING | Evet | - | Negatif metin istemi. |
| `model_adı` | COMBO | Evet | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` | Video oluşturma için kullanılan model (varsayılan: `"kling-v2-master"`). |
| `cfg_ölçeği` | FLOAT | Evet | 0.0 ile 1.0 | Videonun istemi ne kadar yakından takip edeceğini kontrol eder. Daha yüksek değerler daha güçlü bağlılık anlamına gelir (varsayılan: 0.8). |
| `mod` | COMBO | Evet | `"std"`<br>`"pro"` | Oluşturma modu. `"std"` standart kalite, `"pro"` daha yüksek kalitedir (varsayılan: `"std"`). |
| `en_boy_oranı` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulan videonun en-boy oranı (varsayılan: `"16:9"`). |
| `süre` | COMBO | Evet | `"5"`<br>`"10"` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: `"5"`). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Oluşturulan video çıktısı. |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı. |
| `süre` | STRING | Oluşturulan video için süre bilgisi. |

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
