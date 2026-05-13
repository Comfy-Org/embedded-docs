> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSetLastLayer/tr.md)

`CLIP Set Last Layer`, ComfyUI'de CLIP modellerinin işleme derinliğini kontrol etmek için kullanılan temel bir düğümdür. Kullanıcıların CLIP metin kodlayıcısının işlemeyi durduracağı katmanı hassas bir şekilde belirlemesine olanak tanır; bu durum hem metin anlama derinliğini hem de oluşturulan görsellerin stilini etkiler.

CLIP modelini 24 katmanlı zeki bir beyin olarak düşünün:

- Sığ katmanlar (1-8): Temel harfleri ve kelimeleri tanır
- Orta katmanlar (9-16): Dil bilgisi ve cümle yapısını anlar
- Derin katmanlar (17-24): Soyut kavramları ve karmaşık anlamları kavrar

`CLIP Set Last Layer`, bir **"düşünme derinliği denetleyicisi"** gibi çalışır:

-1: 24 katmanın tamamını kullan (tam anlama)
-2: 23. katmanda dur (hafif basitleştirilmiş)
-12: 13. katmanda dur (orta düzey anlama)
-24: Yalnızca 1. katmanı kullan (temel anlama)

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Değiştirilecek CLIP modeli |
| `stop_at_clip_layer` | INT | Evet | -24 ile -1 arası | İşlemin hangi katmanda duracağını belirtir. -1 değeri tüm katmanları kullanırken, -24 yalnızca ilk katmanı kullanır (varsayılan: -1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `clip` | CLIP | Belirtilen katmanın son katman olarak ayarlandığı, değiştirilmiş CLIP modeli |

## Son Katmanı Neden Ayarlamalısınız

- **Performans Optimizasyonu**: Basit cümleleri anlamak için doktora derecesine ihtiyaç duymamak gibi, bazen sığ bir anlayış yeterlidir ve daha hızlıdır
- **Stil Kontrolü**: Farklı anlama seviyeleri, farklı sanatsal stiller üretir
- **Uyumluluk**: Bazı modeller belirli katmanlarda daha iyi performans gösterebilir

---
**Source fingerprint (SHA-256):** `82f3e7fb1d4c0bdd2b242a449085a5497ba8af8616d1800c5c0ee7a85ab42c15`
