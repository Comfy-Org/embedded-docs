# GetItemFromList

Bu düğüm, bir listeden konumuna göre seçilen tek bir öğe döndürür. İstediğiniz öğenin listesini ve indeks numarasını sağlarsınız ve düğüm o öğeyi çıktı olarak verir. Bu, bir grup değer içinden belirli bir öğeyi seçmek için kullanışlıdır; örneğin bir toplu işlemdeki belirli bir görüntüyü seçmek gibi.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `list` | Seçim yapılacak değerler listesi. Bu düğüm liste girdisi aldığı için bağlanan değer bir öğe grubu olarak işlenir. | Herhangi Bir Tür | Evet | Herhangi bir değer listesi |
| `index` | Döndürülecek öğenin konumu. Değer 0'dan başlar, yani `0` ilk öğeyi, `1` ikinci öğeyi döndürür ve bu şekilde devam eder (varsayılan: 0). | INT | Evet | Herhangi bir tam sayı indeksi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `OUTPUT` | Sağlanan `list` içinde verilen `index` konumunda bulunan tek öğe. | Herhangi Bir Tür |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetItemFromList/tr.md)

---
**Source fingerprint (SHA-256):** `11c1c90fed0e29f1110b4c1dda64d60797aff38d7f3af69f76b74e94fe94e976`
