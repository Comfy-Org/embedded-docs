> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/tr.md)

Google'ın Veo 3 API'sini kullanarak metin istemlerinden videolar oluşturur. Bu düğüm, hızlı ve hafif varyantlar dahil olmak üzere birden fazla Veo 3 modelini destekler ve video çözünürlüğü, süresi ve ses oluşturmayı belirlemenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `istem` | STRING | Evet | - | Videonun metin açıklaması (varsayılan: "") |
| `en_boy_oranı` | COMBO | Evet | "16:9"<br>"9:16" | Çıktı videosunun en-boy oranı (varsayılan: "16:9") |
| `çözünürlük` | COMBO | Hayır | "720p"<br>"1080p"<br>"4k" | Çıktı video çözünürlüğü. 4K, veo-3.1-lite ve veo-3.0 modellerinde kullanılamaz. (varsayılan: "720p") |
| `negatif_istem` | STRING | Hayır | - | Videoda nelerden kaçınılacağını belirten olumsuz metin istemi (varsayılan: "") |
| `süre_saniye` | INT | Hayır | 4-8 | Çıktı videosunun saniye cinsinden süresi, 2'şer adımlarla (varsayılan: 8) |
| `istem_geliştir` | BOOLEAN | Hayır | - | Bu parametre kullanımdan kaldırılmıştır ve yok sayılır. (varsayılan: True) |
| `kişi_oluşturma` | COMBO | Hayır | "ALLOW"<br>"BLOCK" | Videoda kişi oluşturmaya izin verilip verilmeyeceği (varsayılan: "ALLOW") |
| `tohum` | INT | Hayır | 0-4294967295 | Video oluşturma için tohum değeri (0 rastgele anlamına gelir) (varsayılan: 0) |
| `görsel` | IMAGE | Hayır | - | Video oluşturmaya rehberlik etmesi için isteğe bağlı referans görseli |
| `model` | COMBO | Hayır | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | Video oluşturma için kullanılacak Veo 3 modeli (varsayılan: "veo-3.0-generate-001") |
| `ses_oluştur` | BOOLEAN | Hayır | - | Video için ses oluştur. Tüm Veo 3 modelleri tarafından desteklenir. (varsayılan: False) |

**Not:** `enhance_prompt` parametresi kullanımdan kaldırılmıştır ve değeri yok sayılır. Düğüm, istemi dahili olarak her zaman geliştirir. Ayrıca, `resolution` parametresi yalnızca veo-3.1 modeli kullanılırken uygulanır; veo-3.0 modelleri için yok sayılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video dosyası |

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
