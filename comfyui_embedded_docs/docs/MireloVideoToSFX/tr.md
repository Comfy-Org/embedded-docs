# Mirelo Video to SFX

Mirelo SFX ile bir videoyu takip eden ses efektleri oluşturun. Klip yüklenir, model ekrandaki eylemi takip eder ve bir ses efektleri miksi ile birlikte, ses kaydından diyalogların çıkarıldığı ayrı bir konuşma kanalı döndürür. Sessiz veya kısmen sessiz kliplere foley, ambiyans ve çarpma sesleri eklemek için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech` ve `seed`. | DYNAMIC_COMBO | Evet | `"sfx-2.0"` |
| `video` | Ses oluşturulacak video. Ses, tüm klip için oluşturulur, 1 ila 600 saniye. | VIDEO | Evet | 1 ila 600 saniye |
| `audio` | `preserve_speech` için ve `speech` çıktısı için videonun kendi ses kaydı yerine kullanılacak diyalog kanalı. Videonun içindeki sesi kullanmak için bağlantısız bırakın. | AUDIO | Hayır | - |
| `prompt` | Sesin nasıl olması gerektiği. Boş bırakılabilir (varsayılan: boş) çünkü model videoyu kendisi tanımlar ve her zaman isteme uymaz. En fazla 2000 karakter. | STRING | Evet | En fazla 2000 karakter |
| `negative_prompt` | Kaçınılacak sesler, kısa ve virgülle ayrılmış bir liste olarak. Boş bırakılabilir (varsayılan: boş). En fazla 1000 karakter. | STRING | Evet | En fazla 1000 karakter |
| `preserve_speech` | Diyaloğu oluşturulan sesin altında karışık tut. Kapalı, yalnızca ses efektleri döndürür. (varsayılan: True) | BOOLEAN | Evet | false<br>true |
| `seed` | İstek için tohum. Sonuçlar belirleyici değildir, bu nedenle aynı tohum bir klibi tekrarlamaz. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |

Klip 1 saniyeden kısa veya 600 saniyeden uzun olduğunda düğüm bir hatayla durur. Bağlı bir `audio` kanalı, `preserve_speech`'in koruduğu ve `speech` çıktısının ayırdığı diyaloğu belirler; bağlı değilse, diyalog videonun kendi ses kaydından gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Klip için ses efektleri miksi, `preserve_speech` açıkken diyalog altına karıştırılmış olarak. | AUDIO |
| `speech` | Ses kaydından ayrılan diyalog. Konuşma bulunamadığında veya konuşma ayırma hiçbir şey döndürmediğinde, `audio` ile aynı örnekleme hızında sessiz. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/tr.md)

---
**Source fingerprint (SHA-256):** `fa09525e6c9b10412823e358652220850fbc7109d81cc207d31ffa8921956495`
