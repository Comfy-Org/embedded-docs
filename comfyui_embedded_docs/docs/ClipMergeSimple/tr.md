> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/tr.md)

`CLIPMergeSimple`, iki CLIP metin kodlayıcı modelini belirli bir orana göre birleştirmek için kullanılan gelişmiş bir model birleştirme düğümüdür.

Bu düğüm, iki CLIP modelini belirli bir orana göre birleştirerek özelliklerini etkili bir şekilde harmanlamada uzmanlaşmıştır. Bir modelden diğerine, konum kimlikleri (position IDs) ve logit ölçeği gibi belirli bileşenler hariç tutularak yama uygular ve bu sayede her iki kaynak modelin özelliklerini bir araya getiren melez bir model oluşturur.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `clip1`   | CLIP      | Birleştirilecek ilk CLIP modeli. Birleştirme işlemi için temel model olarak hizmet eder. |
| `clip2`   | CLIP      | Birleştirilecek ikinci CLIP modeli. Konum kimlikleri ve logit ölçeği hariç, anahtar yamaları, belirtilen orana bağlı olarak ilk modele uygulanır. |
| `oran`   | FLOAT     | Aralık `0.0 - 1.0`, ikinci modelin özelliklerinden ilk modele karıştırılacak oranı belirler. 1.0 oranı, ikinci modelin özelliklerinin tamamen benimsendiği, 0.0 oranı ise yalnızca ilk modelin özelliklerinin korunduğu anlamına gelir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `clip`    | CLIP      | Belirtilen orana göre her iki girdi modelinin özelliklerini içeren, ortaya çıkan birleştirilmiş CLIP modeli. |

## Birleştirme Mekanizması Açıklaması

### Birleştirme Algoritması

Düğüm, iki modeli birleştirmek için ağırlıklı ortalamayı kullanır:

1.  **Temel Modeli Klonla**: İlk olarak `clip1` temel model olarak klonlanır.
2.  **Yamaları Al**: `clip2`'den tüm anahtar yamaları alınır.
3.  **Özel Anahtarları Filtrele**: Sonu `.position_ids` ve `.logit_scale` ile biten anahtarlar atlanır.
4.  **Ağırlıklı Birleştirmeyi Uygula**: `(1.0 - ratio) * clip1 + ratio * clip2` formülü kullanılır.

### Oran Parametresi Açıklaması

-   **ratio = 0.0**: Tamamen `clip1` kullanır, `clip2`'yi yok sayar.
-   **ratio = 0.5**: Her modelden %50 katkı.
-   **ratio = 1.0**: Tamamen `clip2` kullanır, `clip1`'i yok sayar.

## Kullanım Alanları

1.  **Model Stili Füzyonu**: Farklı veriler üzerinde eğitilmiş CLIP modellerinin özelliklerini birleştirin.
2.  **Performans Optimizasyonu**: Farklı modellerin güçlü ve zayıf yönlerini dengeleyin.
3.  **Deneysel Araştırma**: Farklı CLIP kodlayıcıların kombinasyonlarını keşfedin.