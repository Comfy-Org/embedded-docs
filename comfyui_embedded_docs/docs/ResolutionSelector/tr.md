# Çözünürlük Seçici

Resolution Selector düğümü, seçilen bir en boy oranına ve megapiksel cinsinden hedef toplam çözünürlüğe göre piksel genişliğini ve yüksekliğini hesaplar. Empty Latent Image düğümü gibi diğer düğümler için tutarlı boyutlar oluşturmak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Çıktı boyutları için en boy oranı (varsayılan: `"1:1 (Square)"`). | COMBO | Evet | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `megapixels` | Hedef toplam megapiksel. Kare için 1.0 MP ≈ 1024x1024 (varsayılan: 1.0). | FLOAT | Evet | 0.1 - 16.0 (adım: 0.1) |
| `preview` | Hesaplanan çıktı çözünürlüğünün canlı önizlemesi. Bu salt okunur widget otomatik olarak güncellenir ve kullanıcı girişi kabul etmez. | RESOLUTION_PREVIEW | Hayır | N/A |
| `multiple` | Seçilen çözünürlüğün ayarlanacağı en yakın kat (varsayılan: 8). | INT | Hayır | 8 - 128 (adım: 4) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `width` | Piksel cinsinden hesaplanan genişliğin seçilen katla çarpımı. | INT |
| `height` | Piksel cinsinden hesaplanan yüksekliğin seçilen katla çarpımı. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/tr.md)

---
**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`
