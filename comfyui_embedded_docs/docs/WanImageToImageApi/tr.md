> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/tr.md)

WanImageToImageApi düğümü, bir veya iki giriş görüntüsü ve bir metin istemi kullanarak yeni bir görüntü oluşturur. Sağladığınız açıklamaya göre giriş görüntülerinizi dönüştürür ve orijinal girişinizin en-boy oranını koruyan yeni bir görüntü oluşturur. Çıktı görüntüsü, giriş boyutundan bağımsız olarak 1,6 megapiksel olarak sabitlenmiştir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-i2i-preview" | Kullanılacak model (varsayılan: "wan2.5-i2i-preview"). |
| `görsel` | IMAGE | Evet | - | Tek görüntü düzenleme veya çoklu görüntü birleştirme, en fazla 2 görüntü. |
| `istem` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler (varsayılan: boş). |
| `negatif_istem` | STRING | Hayır | - | Kaçınılması gerekenleri tanımlayan olumsuz istem (varsayılan: boş). |
| `tohum` | INT | Hayır | 0 ile 2147483647 arası | Oluşturma için kullanılacak tohum (varsayılan: 0). |
| `filigran` | BOOLEAN | Hayır | - | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: false). |

**Not:** Bu düğüm tam olarak 1 veya 2 giriş görüntüsü kabul eder. 2'den fazla görüntü veya hiç görüntü sağlamamanız durumunda düğüm bir hata döndürecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `görsel` | IMAGE | Giriş görüntülerine ve metin istemlerine dayalı olarak oluşturulan görüntü. |

---
**Source fingerprint (SHA-256):** `d69811ddaba718e5468f539fb9b25827efdf79f3ee9cbf31ad8f9387cea9b9be`
