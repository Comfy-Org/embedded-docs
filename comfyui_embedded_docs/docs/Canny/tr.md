> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/tr.md)

Fotoğraflardan tüm kenar çizgilerini çıkarır, bir fotoğrafın ana hatlarını çizmek için kalem kullanmak gibi, nesnelerin konturlarını ve detay sınırlarını çizer.

## Çalışma Prensibi

Bir fotoğrafın ana hatlarını çizmek için kalem kullanmanız gereken bir sanatçı olduğunuzu hayal edin. Canny düğümü, nereye çizgi (kenar) çizeceğinize ve nereye çizmeyeceğinize karar vermenize yardımcı olan akıllı bir asistan gibi davranır.

Bu süreç bir eleme işine benzer:

- **Yüksek eşik**, "kesinlikle çizgi çizme standardıdır": sadece çok belirgin ve net kontur çizgileri çizilir, örneğin insanların yüz konturları ve bina çerçeveleri gibi
- **Düşük eşik**, "kesinlikle çizgi çizmeme standardıdır": çok zayıf kenarlar, gürültü ve anlamsız çizgiler çizilmesini önlemek için göz ardı edilir
- **Orta alan**: iki standart arasındaki kenarlar, "kesinlikle çizilmesi gereken çizgilere" bağlanıyorsa birlikte çizilir, ancak izole durumdaysa çizilmez

Nihai çıktı, siyah beyaz bir görüntüdür; beyaz kısımlar tespit edilen kenar çizgileri, siyah kısımlar ise kenar olmayan alanlardır.

## Girdiler

| Parametre Adı    | Veri Türü | Girdi Türü | Varsayılan | Aralık     | İşlev Açıklaması |
|------------------|-----------|------------|---------|-----------|------------------|
| `image`          | IMAGE     | Girdi      | -       | -         | Kenar çıkarımı gerektiren orijinal fotoğraf |
| `low_threshold`  | FLOAT     | Widget     | 0.4     | 0.01-0.99 | Düşük eşik, ne kadar zayıf kenarların göz ardı edileceğini belirler. Daha düşük değerler daha fazla detay korur ancak gürültü üretebilir |
| `high_threshold` | FLOAT     | Widget     | 0.8     | 0.01-0.99 | Yüksek eşik, ne kadar güçlü kenarların korunacağını belirler. Daha yüksek değerler sadece en belirgin kontur çizgilerini tutar |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image`   | IMAGE     | Siyah beyaz kenar görüntüsü, beyaz çizgiler tespit edilen kenarlar, siyah alanlar kenar olmayan kısımlardır |

## Parametre Karşılaştırması

![Orijinal Görüntü](./asset/input.webp)

![Parametre Karşılaştırması](./asset/compare.webp)

**Yaygın Sorunlar:**

- Kopuk kenarlar: Yüksek eşiği düşürmeyi deneyin
- Çok fazla gürültü: Düşük eşiği yükseltin
- Önemli detayların eksik olması: Düşük eşiği düşürün
- Kenarların çok kaba olması: Girdi görüntüsünün kalitesini ve çözünürlüğünü kontrol edin