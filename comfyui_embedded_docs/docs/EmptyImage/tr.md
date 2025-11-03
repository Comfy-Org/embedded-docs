> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/tr.md)

## İşlev Açıklaması

EmptyImage düğümü, belirtilen boyutlarda ve renklerde boş görüntüler oluşturmak için kullanılır. Düz renk arka plan görüntüleri oluşturabilir ve genellikle görüntü işleme iş akışları için başlangıç noktası veya arka plan görüntüsü olarak kullanılır.

## Çalışma Prensibi

Tıpkı bir ressamın yaratıcılık sürecine başlamadan önce boş bir tuval hazırlaması gibi, EmptyImage düğümü size bir "dijital tuval" sağlar. Tuvalin boyutunu (genişlik ve yükseklik) belirleyebilir, tuvalin zemin rengini seçebilir ve hatta aynı özelliklere sahip birden fazla tuvali aynı anda hazırlayabilirsiniz. Bu düğüm, boyut ve renk gereksinimlerinizi tam olarak karşılayan standartlaştırılmış tuvaller oluşturabilen akıllı bir sanat malzemesi mağazası gibidir.

## Girdiler

| Parametre Adı | Veri Türü | Açıklama |
|----------------|-----------|-------------|
| `genişlik` | INT | Oluşturulan görüntünün genişliğini (piksel cinsinden) ayarlar, tuvalin yatay boyutlarını belirler |
| `yükseklik` | INT | Oluşturulan görüntünün yüksekliğini (piksel cinsinden) ayarlar, tuvalin dikey boyutlarını belirler |
| `toplu_boyut` | INT | Aynı anda oluşturulacak görüntü sayısı, aynı özelliklere sahip görüntülerin toplu oluşturulması için kullanılır |
| `renk` | INT | Görüntünün arka plan rengi. Onaltılık (hexadecimal) renk ayarlarını girebilirsiniz, bunlar otomatik olarak ondalık sayıya dönüştürülecektir |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Oluşturulan boş görüntü tensörü, [batch_size, height, width, 3] formatında, RGB üç renk kanalını içerir |

## Yaygın Renk Referans Değerleri

Bu düğümün mevcut renk girdisi kullanıcı dostu olmadığından (tüm renk değerleri ondalık sayıya dönüştürülmektedir), hızlı bir şekilde uygulama yapabilmeniz için doğrudan kullanılabilecek bazı yaygın renk değerleri aşağıda verilmiştir.

| Renk Adı | Onaltılık Değer |
|------------|-------------------|
| Siyah      | 0x000000         |
| Beyaz      | 0xFFFFFF         |
| Kırmızı    | 0xFF0000         |
| Yeşil      | 0x00FF00         |
| Mavi       | 0x0000FF         |
| Sarı       | 0xFFFF00         |
| Camgöbeği | 0x00FFFF         |
| Macenta   | 0xFF00FF         |
| Turuncu   | 0xFF8000         |
| Mor        | 0x8000FF         |
| Pembe      | 0xFF80C0         |
| Kahverengi | 0x8B4513         |
| Koyu Gri  | 0x404040         |
| Açık Gri  | 0xC0C0C0         |
| Lacivert  | 0x000080         |
| Koyu Yeşil| 0x008000         |
| Koyu Kırmızı | 0x800000         |
| Altın      | 0xFFD700         |
| Gümüş      | 0xC0C0C0         |
| Bej        | 0xF5F5DC         |