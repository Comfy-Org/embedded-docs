# Boş Görüntü

## Fonksiyon Açıklaması

EmptyImage düğümü, belirtilen boyut ve renklerde boş görüntüler oluşturmak için kullanılır. Düz renkli arka plan görüntüleri üretebilir ve genellikle görüntü işleme iş akışları için başlangıç noktası veya arka plan görüntüsü olarak kullanılır.

## Çalışma Prensibi

Tıpkı bir ressamın yaratmaya başlamadan önce boş bir tuval hazırlaması gibi, EmptyImage düğümü de size bir "dijital tuval" sağlar. Tuval boyutunu (genişlik ve yükseklik) belirleyebilir, tuvalin temel rengini seçebilir ve hatta aynı özelliklere sahip birden fazla tuvali tek seferde hazırlayabilirsiniz. Bu düğüm, boyut ve renk gereksinimlerinizi mükemmel şekilde karşılayan standartlaştırılmış tuvaller oluşturabilen akıllı bir sanat malzemeleri mağazası gibidir.

## Girdiler

| Parametre Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `genişlik` | Oluşturulan görüntünün genişliğini (piksel cinsinden) ayarlar, tuvalin yatay boyutlarını belirler | INT |
| `yükseklik` | Oluşturulan görüntünün yüksekliğini (piksel cinsinden) ayarlar, tuvalin dikey boyutlarını belirler | INT |
| `toplu_boyut` | Aynı anda oluşturulacak görüntü sayısı, aynı özelliklere sahip görüntülerin toplu olarak oluşturulması için kullanılır | INT |
| `renk` | Görüntünün arka plan rengi. Onaltılık renk ayarları girebilirsiniz, bunlar otomatik olarak ondalık sisteme dönüştürülür | INT |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan boş görüntü tensörü, [batch_size, height, width, 3] biçiminde, RGB üç renk kanalını içerir | IMAGE |

## Yaygın Renk Referans Değerleri

Bu düğümün mevcut renk girişi kullanıcı dostu olmadığından ve tüm renk değerleri ondalık sisteme dönüştürüldüğünden, hızlı uygulama için doğrudan kullanılabilecek bazı yaygın renk değerleri aşağıda listelenmiştir.

| Renk Adı | Onaltılık Değer |
|----------|-----------------|
| Siyah    | 0x000000        |
| Beyaz    | 0xFFFFFF        |
| Kırmızı  | 0xFF0000        |
| Yeşil    | 0x00FF00        |
| Mavi     | 0x0000FF        |
| Sarı     | 0xFFFF00        |
| Camgöbeği| 0x00FFFF        |
| Eflatun  | 0xFF00FF        |
| Turuncu  | 0xFF8000        |
| Mor      | 0x8000FF        |
| Pembe    | 0xFF80C0        |
| Kahverengi| 0x8B4513       |
| Koyu Gri | 0x404040        |
| Açık Gri | 0xC0C0C0        |
| Lacivert | 0x000080        |
| Koyu Yeşil| 0x008000       |
| Bordo    | 0x800000        |
| Altın    | 0xFFD700        |
| Gümüş    | 0xC0C0C0        |
| Bej      | 0xF5F5DC        |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/tr.md)
