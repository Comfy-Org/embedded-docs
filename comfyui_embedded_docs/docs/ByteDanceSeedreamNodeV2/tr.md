> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/tr.md)

ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

## Genel Bakış

Bu düğüm, ByteDance'in Seedream modellerini (sürüm 4.0, 4.5 ve 5.0) kullanarak görseller oluşturur veya düzenler. Bir metin isteminden yeni görseller oluşturabilir veya referans görseller sağlayarak mevcut görselleri düzenleyebilir; 4K'ya kadar çözünürlükleri destekler.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Bir görsel oluşturmak veya düzenlemek için metin istemi. |
| `model` | COMBO | Evet | `"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` | Oluşturma için kullanılacak Seedream model sürümü. Her modelin farklı yetenekleri ve fiyatlandırması vardır. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). |
| `watermark` | BOOLEAN | Hayır | Doğru / Yanlış | Görsele "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği (varsayılan: Yanlış). |

### Modele Özgü Parametreler

Bir model seçtiğinizde, ek parametreler kullanılabilir hale gelir:

- **Boyut Ön Ayarı**: Önceden tanımlanmış bir görsel çözünürlüğü seçmek için bir açılır menü (ör. "2048x2048", "1024x1024"). Mevcut ön ayarlar seçilen modele bağlıdır.
- **Genişlik**: Oluşturulan görselin piksel cinsinden genişliği (varsayılan: 2048).
- **Yükseklik**: Oluşturulan görselin piksel cinsinden yüksekliği (varsayılan: 2048).
- **Maksimum Görsel**: Oluşturulacak maksimum görsel sayısı (varsayılan: 1). 1 olarak ayarlandığında, sıralı görsel oluşturma devre dışı bırakılır.
- **Referans Görseller**: Düzenleme için en fazla 10 (Seedream 4.0 ve 4.5 için) veya 14 (Seedream 5.0 Lite için) referans görsel. Görsellerin en boy oranı 1:3 ile 3:1 arasında olmalıdır.
- **Kısmi Başarısızlıkta Hata Ver**: Etkinleştirilirse, istenen tüm görseller başarıyla oluşturulamazsa düğüm bir hata verecektir (varsayılan: Yanlış).

### Çözünürlük Kısıtlamaları

- **Seedream 5.0 Lite ve 4.5**: Minimum çözünürlük 3,68 megapikseldir (ör. 1920x1920).
- **Seedream 4.0**: Minimum çözünürlük 0,92 megapikseldir (ör. 960x960).
- **Tüm modeller**: Maksimum çözünürlük 16,78 megapikseldir (ör. 4096x4096).

### Görsel Sayısı Kısıtlamaları

- Referans görsellerin ve oluşturulan görsellerin toplam sayısı 15'i geçemez.
- Seedream 5.0 Lite için en fazla 14 referans görsel desteklenir.
- Seedream 4.0 ve 4.5 için en fazla 10 referans görsel desteklenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Oluşturulan veya düzenlenen görsel, bir tensör olarak. Birden fazla görsel talep edildiyse, bunlar tek bir toplu iş halinde birleştirilir. |