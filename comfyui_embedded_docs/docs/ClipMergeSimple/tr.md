> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/tr.md)

`CLIPMergeSimple`, iki CLIP metin kodlayıcı modelini belirtilen bir orana göre birleştirmek için kullanılan gelişmiş bir model birleştirme düğümüdür.

Bu düğüm, iki CLIP modelini belirtilen bir orana göre birleştirme konusunda uzmanlaşmıştır ve özelliklerini etkili bir şekilde harmanlar. Her iki kaynak modelden gelen özellikleri birleştiren hibrit bir model oluşturmak için, konum kimlikleri ve logit ölçeği gibi belirli bileşenleri hariç tutarak, bir modelden diğerine seçici olarak yamalar uygular.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | ZORUNLU | - | - | Birleştirilecek ilk CLIP modeli. Birleştirme işlemi için temel model görevi görür. |
| `clip2` | CLIP | ZORUNLU | - | - | Birleştirilecek ikinci CLIP modeli. Konum kimlikleri ve logit ölçeği dışındaki anahtar yamaları, belirtilen orana göre ilk modele uygulanır. |
| `oran` | FLOAT | ZORUNLU | 1.0 | 0.0 - 1.0 (adım: 0.01) | İkinci modelden gelen özelliklerin birinci modele ne oranda karıştırılacağını belirler. 1.0 oranı, ikinci modelin özelliklerinin tamamen benimsendiği anlamına gelirken, 0.0 oranı yalnızca birinci modelin özelliklerini korur. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `clip` | CLIP | Belirtilen orana göre her iki giriş modelinin özelliklerini içeren, birleştirilmiş CLIP modeli. |

## Birleştirme Mekanizması Açıklaması

### Birleştirme Algoritması

Düğüm, iki modeli birleştirmek için ağırlıklı ortalama kullanır:

1.  **Temel Modeli Kopyala**: İlk olarak `clip1`'i temel model olarak kopyalar
2.  **Yamaları Al**: `clip2`'den tüm anahtar yamalarını alır
3.  **Özel Anahtarları Filtrele**: `.position_ids` ve `.logit_scale` ile biten anahtarları atlar
4.  **Ağırlıklı Birleştirmeyi Uygula**: `(1.0 - ratio) * clip1 + ratio * clip2` formülünü kullanır

### Oran Parametresi Açıklaması

-   **ratio = 0.0**: Tamamen clip1'i kullanır, clip2'yi yok sayar
-   **ratio = 0.5**: Her modelden %50 katkı
-   **ratio = 1.0**: Tamamen clip2'yi kullanır, clip1'i yok sayar

## Kullanım Durumları

1.  **Model Stili Füzyonu**: Farklı veriler üzerinde eğitilmiş CLIP modellerinin özelliklerini birleştirme
2.  **Performans Optimizasyonu**: Farklı modellerin güçlü ve zayıf yönlerini dengeleme
3.  **Deneysel Araştırma**: Farklı CLIP kodlayıcıların kombinasyonlarını keşfetme

---
**Source fingerprint (SHA-256):** `0d3c8388dbe88675ea7fb51161ab41ce898bcf63983b3d2817b16ec5bfa613e5`
