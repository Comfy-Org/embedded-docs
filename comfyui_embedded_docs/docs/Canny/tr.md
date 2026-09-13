# Canny

Fotoğraflardaki tüm kenar çizgilerini, bir kalemle fotoğrafın ana hatlarını çiziyormuş gibi çıkarın; nesnelerin konturlarını ve ayrıntı sınırlarını ortaya koyun.

## Çalışma Prensibi

Bir sanatçı olduğunuzu ve bir fotoğrafın ana hatlarını kalemle çizmeniz gerektiğini hayal edin. Canny düğümü, çizgileri (kenarları) nereye çizeceğinize ve nereye çizmeyeceğinize karar vermenize yardımcı olan akıllı bir asistan gibi davranır.

Bu süreç bir eleme işi gibidir:

- **Yüksek eşik**, "mutlaka çizgi çizme standardı"dır: yalnızca çok belirgin ve net kontur çizgileri çizilir; örneğin insanların yüz hatları ve bina çerçeveleri
- **Düşük eşik**, "kesinlikle çizgi çizme standardı"dır: çok zayıf kenarlar yok sayılır; böylece gürültü ve anlamsız çizgiler çizilmez
- **Ara alan**: iki standart arasındaki kenarlar, "mutlaka çizilecek çizgiler"e bağlanıyorsa birlikte çizilir; ancak yalıtılmışlarsa çizilmez

Nihai çıktı, beyaz kısımların algılanan kenar çizgileri, siyah kısımların ise kenar bulunmayan alanlar olduğu siyah beyaz bir görüntüdür.

## Girdiler

| Parametre Adı | İşlev Açıklaması | Veri Türü | Girdi Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `görüntü` | Kenar çıkarımı yapılacak orijinal fotoğraf | IMAGE | Girdi | - | - |
| `düşük_eşik` | Düşük eşik; yok sayılacak kenarların ne kadar zayıf olabileceğini belirler. Daha düşük değerler daha fazla ayrıntıyı korur ancak gürültü üretebilir | FLOAT | Widget | 0.4 | 0.01-0.99 |
| `yüksek_eşik` | Yüksek eşik; korunacak kenarların ne kadar güçlü olması gerektiğini belirler. Daha yüksek değerler yalnızca en belirgin kontur çizgilerini korur | FLOAT | Widget | 0.8 | 0.01-0.99 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Siyah beyaz kenar görüntüsü; beyaz çizgiler algılanan kenarlar, siyah alanlar kenar bulunmayan kısımlardır | IMAGE |

## Parametre Karşılaştırması

![Orijinal Görüntü](./asset/input.webp)

![Parametre Karşılaştırması](./asset/compare.webp)

**Yaygın Sorunlar:**

- Kopuk kenarlar: Yüksek eşiği düşürmeyi deneyin
- Aşırı gürültü: Düşük eşiği yükseltin
- Önemli ayrıntılar eksik: Düşük eşiği düşürün
- Kenarlar çok pürüzlü: Girdi görüntüsünün kalitesini ve çözünürlüğünü kontrol edin

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/tr.md)
