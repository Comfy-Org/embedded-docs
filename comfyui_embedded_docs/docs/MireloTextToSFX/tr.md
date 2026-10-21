# Mirelo Text to SFX

Mirelo SFX ile bir metin açıklamasından ses efekti oluşturun. Sesin ait olduğu görüntüyü değil, sesin kendisini tanımlayın; düğüm, istenen uzunlukta tek bir ses parçası döndürür. Video çekmeden veya yüklemeden foley, ortam sesi, darbe sesleri ve kısa müzikal dokular için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `prompt`, `negative_prompt`, `duration` ve `seed`. | DYNAMIC_COMBO | Evet | `"sfx-2.0"` |
| `prompt` | Görüntüyü değil sesi tanımlayın. 1 ila 2000 karakter. | STRING | Evet | 1 ila 2000 karakter |
| `negative_prompt` | Kaçınılacak sesler; virgülle ayrılmış kısa bir liste olarak. Boş bırakılabilir (varsayılan: boş). En fazla 1000 karakter. | STRING | Evet | 1000 karaktere kadar |
| `duration` | Sesin saniye cinsinden uzunluğu. (varsayılan: 5.0) | FLOAT | Evet | 0.1 ila 600.0 (adım 0.1) |
| `seed` | İstek için seed değeri. Sonuçlar deterministik değildir; bu nedenle aynı seed değeri aynı sesi tekrar etmez. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |

Düğüm, `prompt` boş olduğunda veya 2000 karakterden uzun olduğunda ve `negative_prompt` 1000 karakterden uzun olduğunda hatayla durur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `AUDIO` | Oluşturulan ses efekti, `duration` uzunluğunda. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloTextToSFX/tr.md)

---
**Source fingerprint (SHA-256):** `b09a9562cea636702acd9fc50feb38b272a558f8b8509da21f5fada2abd9fd48`
