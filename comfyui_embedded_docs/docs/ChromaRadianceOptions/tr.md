# ChromaRadianceSeçenekleri

ChromaRadianceOptions düğümü, Chroma Radiance modeli için gelişmiş ayarları yapılandırmanıza olanak tanır. Mevcut bir modeli sarar ve sigma değerlerine dayalı olarak gürültü giderme işlemi sırasında belirli seçenekleri uygulayarak NeRF döşeme boyutu ve diğer radiance ile ilgili parametreler üzerinde ince ayarlı kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Chroma Radiance seçeneklerinin uygulanacağı model | MODEL | Evet | - |
| `sarmalayıcıyı koru` | Etkinleştirildiğinde, varsa mevcut model işlev sarmalayıcısına devreder. Genellikle etkin bırakılmalıdır. (varsayılan: True) | BOOLEAN | Hayır | - |
| `başlangıç sigma` | Bu seçeneklerin geçerli olacağı ilk sigma. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0 |
| `bitiş sigma` | Bu seçeneklerin geçerli olacağı son sigma. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ile 1.0 |
| `nerf döşeme boyutu` | Varsayılan NeRF döşeme boyutunu geçersiz kılmayı sağlar. -1 varsayılanı (32) kullanmak anlamına gelir. 0, döşemesiz modu kullanmak anlamına gelir (çok fazla VRAM gerektirebilir). (varsayılan: -1) | INT | Hayır | -1 and above |
| `force_sequential_txt_ids` | Sıfırlar yerine sıralı metin belirteci kimliklerinin kullanımını zorlar. Bu şekilde eğitilmiş ancak durum sözlüğünde __sequential__ anahtarını içermeyen 2026-05-22 ile 2026-06-01 tarihleri arasındaki kontrol noktaları için kullanılmalıdır. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** Chroma Radiance seçenekleri yalnızca geçerli sigma değeri `end_sigma` ile `start_sigma` arasında olduğunda (uç değerler dahil) etkili olur. `nerf_tile_size` parametresi yalnızca 0 veya daha yüksek değerlere ayarlandığında uygulanır. `force_sequential_txt_ids` parametresi yalnızca True olarak ayarlandığında uygulanır. `nerf_tile_size` -1 ve `force_sequential_txt_ids` False olduğunda hiçbir seçenek yapılandırılmaz ve model herhangi bir sarmalayıcı uygulanmadan değiştirilmemiş olarak döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Chroma Radiance seçenekleri uygulanmış model veya hiçbir seçenek etkin değilse değiştirilmemiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/tr.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
