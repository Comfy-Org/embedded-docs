> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/tr.md)

# Çözünürlük Seçici

Çözünürlük Seçici düğümü, seçilen bir en-boy oranına ve megapiksel cinsinden hedef toplam çözünürlüğe göre bir görüntünün piksel genişliğini ve yüksekliğini hesaplar. Boş Gizli Görüntü düğümü gibi diğer düğümler için tutarlı boyutlar oluşturmada kullanışlıdır. Çıktı boyutları her zaman 8'in en yakın katına yuvarlanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `aspect_ratio` | COMBO | Evet | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | Çıktı boyutları için en-boy oranı (varsayılan: `"SQUARE"`). |
| `megapixels` | FLOAT | Evet | 0.1 - 16.0 | Hedef toplam megapiksel değeri. Kare en-boy oranı için 1,0 MP ≈ 1024×1024 (varsayılan: 1,0). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `width` | INT | Piksel cinsinden hesaplanan genişlik, 8'in katıdır. |
| `height` | INT | Piksel cinsinden hesaplanan yükseklik, 8'in katıdır. |