# ChromaRadianceSeçenekleri

ChromaRadianceOptions düğümü, Chroma Radiance modeli için gelişmiş ayarları yapılandırmanıza olanak tanır. Mevcut bir modeli sarar ve sigma değerlerine dayalı olarak gürültü giderme işlemi sırasında belirli seçenekleri uygular; NeRF döşeme boyutu ve diğer ışınımla ilgili parametreler üzerinde ince ayarlı kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Chroma Radiance seçeneklerinin uygulanacağı model | MODEL | Evet | - |
| `preserve_wrapper` | Etkinleştirildiğinde, varsa mevcut bir model fonksiyon sarmalayıcısına devreder. Genellikle etkin bırakılmalıdır. (varsayılan: True) | BOOLEAN | Hayır | - |
| `start_sigma` | Bu seçeneklerin geçerli olacağı ilk sigma değeri. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ila 1.0 |
| `end_sigma` | Bu seçeneklerin geçerli olacağı son sigma değeri. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ila 1.0 |
| `nerf_tile_size` | Varsayılan NeRF döşeme boyutunu geçersiz kılmayı sağlar. -1, varsayılanın (32) kullanılacağı anlamına gelir. 0, döşemesiz modun kullanılacağı anlamına gelir (çok fazla VRAM gerektirebilir). (varsayılan: -1) | INT | Hayır | -1 ve üzeri |
| `force_sequential_txt_ids` | Sıfırlar yerine sıralı metin token kimliklerinin kullanımını zorunlu kılar. 2026-05-22 ile 2026-06-01 tarihleri arasındaki, bu şekilde eğitilmiş ancak durum sözlüğünde `__sequential__` anahtarını içermeyen kontrol noktaları için kullanılmalıdır. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** Chroma Radiance seçenekleri yalnızca geçerli sigma değeri `end_sigma` ile `start_sigma` arasında (sınırlar dahil) olduğunda etkili olur. `nerf_tile_size` parametresi yalnızca 0 veya daha yüksek değerlere ayarlandığında uygulanır. `force_sequential_txt_ids` parametresi yalnızca True olarak ayarlandığında uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model` | Chroma Radiance seçenekleri uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/tr.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
