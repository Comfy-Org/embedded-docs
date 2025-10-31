> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSetLastLayer/tr.md)

`CLIP Set Last Layer`, CLIP modellerinin işleme derinliğini kontrol etmek için ComfyUI'da bulunan temel bir düğümdür. Kullanıcıların CLIP metin kodlayıcısının işlemeyi nerede durduracağını hassas bir şekilde kontrol etmesine olanak tanır, bu da hem metin anlama derinliğini hem de oluşturulan görüntülerin stilini etkiler.

CLIP modelini 24 katmanlı bir akıllı beyin olarak hayal edin:

- Yüzeysel katmanlar (1-8): Temel harf ve kelimeleri tanır
- Orta katmanlar (9-16): Dilbilgisi ve cümle yapısını anlar
- Derin katmanlar (17-24): Soyut kavramları ve karmaşık anlam bilgisi kavramlarını kavrar

`CLIP Set Last Layer` bir **"düşünme derinliği kontrolcüsü"** gibi çalışır:

-1: Tüm 24 katmanı kullan (tam anlama)
-2: 23. katmanda dur (hafifçe basitleştirilmiş)
-12: 13. katmanda dur (orta düzey anlama)
-24: Sadece 1. katmanı kullan (temel anlama)

## Girişler

| Parametre | Veri Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|---------|--------|-------------|
| `clip` | CLIP | - | - | Değiştirilecek CLIP modeli |
| `stop_at_clip_layer` | INT | -1 | -24 ila -1 | Hangi katmanda durulacağını belirtir, -1 tüm katmanları kullanır, -24 sadece ilk katmanı kullanır |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| clip | CLIP | Belirtilen katmanın son katman olarak ayarlandığı değiştirilmiş CLIP modeli |

## Son Katman Neden Ayarlanır

- **Performans Optimizasyonu**: Basit cümleleri anlamak için doktora derecesine ihtiyaç duyulmadığı gibi, bazen yüzeysel anlama yeterlidir ve daha hızlıdır
- **Stil Kontrolü**: Farklı anlama seviyeleri farklı sanatsal stiller üretir
- **Uyumluluk**: Bazı modeller belirli katmanlarda daha iyi performans gösterebilir