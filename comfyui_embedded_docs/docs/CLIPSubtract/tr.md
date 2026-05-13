> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/tr.md)

CLIPSubtract düğümü, iki CLIP modeli arasında çıkarma işlemi gerçekleştirir. İlk CLIP modelini temel alır ve ikinci CLIP modelindeki anahtar yamaları çıkarır; çıkarma gücünü kontrol etmek için isteğe bağlı bir çarpan kullanılabilir. Bu sayede, bir modelden belirli özellikleri başka bir model kullanarak kaldırarak ince ayarlı model harmanlaması yapılabilir.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Zorunlu | - | - | Değiştirilecek temel CLIP modeli |
| `clip2` | CLIP | Zorunlu | - | - | Anahtar yamaları temel modelden çıkarılacak CLIP modeli |
| `multiplier` | FLOAT | Zorunlu | 1.0 | -10.0 ila 10.0, adım 0.01 | Çıkarma işleminin gücünü kontrol eder. Pozitif değerler clip2'den özellikleri çıkarır, negatif değerler ise özellikleri ekler. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Çıkarma işlemi sonucunda elde edilen CLIP modeli |

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
