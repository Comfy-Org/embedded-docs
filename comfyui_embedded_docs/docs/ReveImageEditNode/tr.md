# Reve Görsel Düzenle

Reve Image Edit düğümü, mevcut bir görseli metin açıklamasına göre değiştirmenizi sağlar. Sağladığınız görsele istenen değişiklikleri uygulamak için Reve API'sini kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görsel` | Düzenlenecek görsel. | IMAGE | Evet | - |
| `düzenleme_talimatı` | Görselin nasıl düzenleneceğine dair metin açıklaması. Maksimum 2560 karakter. | STRING | Evet | - |
| `model` | Düzenleme için kullanılacak model sürümü. | MODEL | Evet | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `model.aspect_ratio` | Düzenlenmiş görsel için en-boy oranı. "auto" olarak ayarlandığında en-boy oranı otomatik olarak belirlenir. | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Model için test zamanı ölçekleme faktörü. Daha yüksek değerler kaliteyi artırabilir ancak işlem süresini uzatır. | FLOAT | Hayır | - |
| `upscale` | Oluşturulan görselin yükseltilip yükseltilmeyeceğini kontrol eder. | COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `upscale.upscale_factor` | Yükseltme etkinleştirildiğinde görselin yükseltme faktörü. | FLOAT | Hayır | - |
| `remove_background` | Oluşturulan görselden arka planın kaldırılıp kaldırılmayacağını kontrol eder. | BOOLEAN | Hayır | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |

**Not:** `upscale.upscale_factor` parametresi yalnızca `upscale` parametresi `"enabled"` olarak ayarlandığında geçerlidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görsel` | Talimata göre oluşturulan düzenlenmiş görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`
