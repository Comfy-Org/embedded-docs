# BriaVideoEraser

Bria ile bir videoda kare başına maskenin kapladığı alanı siler ve oluşan boşluğu doldurur. Maske, silinmesi gereken alanda beyaz, diğer alanlarda siyah olmalıdır. Bria, en fazla 5,1 saniyelik, saniyede 20 ila 30 kare hızında ve çift sayılı piksel boyutlarına sahip klipleri kabul eder; ses varsayılan olarak korunur. Döndürülen klip, girdiden birkaç kare daha kısa olabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Üzerinden silme yapılacak klip. | VIDEO | Evet | - |
| `mask` | Videonun her karesi için bir maske; silinecek nesnenin bulunduğu yer beyazdır. Maske veya maske videosundan yalnızca birini sağlayın; ikisini birden sağlamayın. | MASK | Hayır | - |
| `mask_video` | Videoyla aynı boyutlara ve kare sayısına sahip, önceden kodlanmış bir maske videosu. Maske veya maske videosundan yalnızca birini sağlayın; ikisini birden sağlamayın. | VIDEO | Hayır | - |
| `preserve_audio` | Girdinin ses parçasını korur. Varsayılan: true. | BOOLEAN | Hayır | `true`<br>`false` |

**Kısıtlamalara ilişkin notlar:**

- `mask` veya `mask_video` öğelerinden tam olarak biri bağlanmalıdır. Hiçbiri sağlanmazsa veya ikisi de sağlanırsa hata oluşur.
- Video en fazla 5,1 saniye uzunluğunda olmalı ve saniyede 20 ila 30 kare hızında oynamalıdır. Gerekirse klibi Get Video Components ve Create Video ile yeniden zamanlayın.
- Video çift sayılı piksel boyutlarına sahip olmalıdır (genişlik ve yükseklik 2'ye bölünebilmelidir). Aksi takdirde önce kırpın veya ölçeklendirin.
- `mask` kullanıldığında, her video karesi için bir maske karesi içermeli ve en-boy oranı videoyla eşleşmelidir. Maskeler %50'de ikili hale getirilir: yarıdan daha düşük opaklıkla boyanmış alanlar yok sayılır ve boş bir maske hata verir. Maskenin çözünürlüğü videodan farklıysa, video boyutlarına yeniden boyutlandırılır.
- `mask_video` kullanıldığında, videoyla aynı boyutlara ve aynı kare sayısına sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Maskelenen alanların silindiği ve boşlukların doldurulduğu düzenlenmiş klip. Girdi klibinden birkaç kare daha kısa olabilir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/tr.md)

---
**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`
