# Çözünürlük Seçici

Çözünürlük Seçici düğümü, seçilen bir en-boy oranına ve megapiksel cinsinden hedef toplam çözünürlüğe göre bir görüntünün piksel genişliğini ve yüksekliğini hesaplar. Boş Gizli Görüntü düğümü gibi diğer düğümler için tutarlı boyutlar oluşturmada kullanışlıdır. Çıktı boyutları her zaman en yakın 8'in katına yuvarlanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `en_boy_orani` | Çıktı boyutları için en-boy oranı (varsayılan: `"SQUARE"`). | COMBO | Evet | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` |
| `megapiksel` | Hedef toplam megapiksel. Kare en-boy oranı için 1.0 MP ≈ 1024×1024 (varsayılan: 1.0). | FLOAT | Evet | 0.1 - 16.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `yukseklik` | Piksel cinsinden hesaplanan genişlik, 8'in katıdır. | INT |
| `height` | Piksel cinsinden hesaplanan yükseklik, 8'in katıdır. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/tr.md)

---
**Source fingerprint (SHA-256):** `221d38fa72c9989e06b706d33fd3e0dc4caa0f741dd2931864c58a6bd7f52613`
