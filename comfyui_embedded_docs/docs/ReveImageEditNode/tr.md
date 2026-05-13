> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/tr.md)

Reve Image Edit düğümü, mevcut bir görseli metin açıklamasına göre değiştirmenizi sağlar. Sağladığınız görsele istenen değişiklikleri uygulamak için Reve API'sini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görsel` | IMAGE | Evet | - | Düzenlenecek görsel. |
| `düzenleme_talimatı` | STRING | Evet | - | Görselin nasıl düzenleneceğine dair metin açıklaması. Maksimum 2560 karakter. |
| `model` | MODEL | Evet | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` | Düzenleme için kullanılacak model sürümü. |
| `model.aspect_ratio` | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Düzenlenmiş görsel için en-boy oranı. "auto" olarak ayarlandığında en-boy oranı otomatik olarak belirlenir. |
| `model.test_time_scaling` | FLOAT | Hayır | - | Model için test zamanı ölçekleme faktörü. Daha yüksek değerler kaliteyi artırabilir ancak işlem süresini uzatır. |
| `upscale` | COMBO | Hayır | `"disabled"`<br>`"enabled"` | Oluşturulan görselin yükseltilip yükseltilmeyeceğini kontrol eder. |
| `upscale.upscale_factor` | FLOAT | Hayır | - | Yükseltme etkinleştirildiğinde görselin yükseltme faktörü. |
| `remove_background` | BOOLEAN | Hayır | - | Oluşturulan görselden arka planın kaldırılıp kaldırılmayacağını kontrol eder. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) |

**Not:** `upscale.upscale_factor` parametresi yalnızca `upscale` parametresi `"enabled"` olarak ayarlandığında geçerlidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görsel` | IMAGE | Talimata göre oluşturulan düzenlenmiş görsel. |

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`
