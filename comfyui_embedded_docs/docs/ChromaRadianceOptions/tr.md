# ChromaRadianceSeçenekleri

ChromaRadianceOptions düğümü, Chroma Radiance modeli için gelişmiş ayarları yapılandırmanıza olanak tanır. Mevcut bir modele bir sarmalayıcı ekler ve seçilen seçenekleri, yalnızca geçerli sigma değeri yapılandırılan aralığa düştüğünde gürültü giderme işlemi sırasında uygular; böylece NeRF döşeme boyutu ve metin token kimliği işleme üzerinde kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Chroma Radiance seçeneklerinin uygulanacağı model | MODEL | Evet | - |
| `sarmalayıcıyı koru` | Etkinleştirildiğinde, varsa mevcut bir model işlevi sarmalayıcısına devreder. Genellikle etkin bırakılmalıdır. (varsayılan: True) | BOOLEAN | Hayır | - |
| `başlangıç sigma` | Bu seçeneklerin etkili olacağı ilk sigma. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 1.0 |
| `bitiş sigma` | Bu seçeneklerin etkili olacağı son sigma. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 1.0 |
| `nerf döşeme boyutu` | Varsayılan NeRF döşeme boyutunun geçersiz kılınmasına olanak tanır. -1, varsayılanı (32) kullan anlamına gelir. 0, döşemesiz modu kullan anlamına gelir (çok fazla VRAM gerektirebilir). (varsayılan: -1) | INT | Hayır | -1 ve üzeri |
| `force_sequential_txt_ids` | Sıfırlar yerine sıralı metin token kimliklerinin kullanımını zorlar. 2026-05-22 ile 2026-06-01 arasındaki, bu şekilde eğitilmiş ancak state dict içinde __sequential__ anahtarını içermeyen checkpoint'ler için kullanılmalıdır. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** Chroma Radiance seçenekleri yalnızca geçerli sigma değeri `end_sigma` ile `start_sigma` arasında (dahil) olduğunda etkili olur. `nerf_tile_size` seçeneği yalnızca 0 veya daha yüksek bir değere ayarlandığında uygulanır (-1 değeri varsayılan 32 döşeme boyutunu kullanır ve herhangi bir geçersiz kılma saklamaz). `force_sequential_txt_ids` seçeneği yalnızca True olarak ayarlandığında uygulanır. `nerf_tile_size` -1 olduğunda ve `force_sequential_txt_ids` False olduğunda, hiçbir seçenek yapılandırılmaz ve model herhangi bir sarmalayıcı uygulanmadan değiştirilmeden döndürülür.

**Not:** `model` dışındaki tüm girdiler gelişmiş seçeneklerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `model` | Chroma Radiance seçenekleri uygulanmış model veya hiçbir seçenek etkin değilse değiştirilmemiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/tr.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
