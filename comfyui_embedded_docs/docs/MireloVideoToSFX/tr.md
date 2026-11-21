# Mirelo Videodan SFX'e

Mirelo SFX ile bir videoyu takip eden ses efektleri oluşturun. Klip yüklenir, model ekrandaki hareketi takip eder ve bir ses efektleri miksı ile ses bandından çıkarılmış diyaloğu içeren ayrı bir konuşma kanalı döndürür. Sessiz veya kısmen sessiz kliplere foley, ortam sesi ve çarpma sesleri eklemek için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech`, `seed` ve `auto_downscale`. | DYNAMIC_COMBO | Evet | `"sfx-2.0"` |
| `video` | Ses üretilecek video. Ses, 1 ile 600 saniye arasındaki tüm klip için üretilir. | VIDEO | Evet | 1 ile 600 saniye arası |
| `audio` | `preserve_speech` ve `speech` çıktısı için videonun kendi ses bandı yerine kullanılacak diyalog kanalı. Videonun içindeki sesi kullanmak için bağlantısız bırakın. | AUDIO | Hayır | - |
| `prompt` | Sesin nasıl olması gerektiği. Model videoyu kendisi tanımladığı ve prompt'a her zaman uymadığı için boş bırakılabilir (varsayılan: boş). En fazla 2000 karakter. | STRING | Evet | 2000 karaktere kadar |
| `negative_prompt` | Kaçınılacak sesler, virgülle ayrılmış kısa bir liste olarak. Boş bırakılabilir (varsayılan: boş). En fazla 1000 karakter. | STRING | Evet | 1000 karaktere kadar |
| `preserve_speech` | Diyaloğu üretilen sesin altında karışık tutun. Kapalı olduğunda yalnızca ses efektleri döndürür. (varsayılan: True) | BOOLEAN | Evet | false<br>true |
| `seed` | İstek için seed. Sonuçlar deterministik değildir, bu nedenle aynı seed bir klibi tekrarlamaz. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 arası |
| `auto_downscale` | Yüklemeden önce kısa kenarı 2160 pikselin üzerinde olan bir klibi en-boy oranını koruyarak küçültün; daha küçük klipler değiştirilmez (varsayılan: True). | BOOLEAN | Hayır | `True`<br>`False` |

Düğüm, klip 1 saniyeden kısa veya 600 saniyeden uzun olduğunda hata vererek durur. Bağlı bir `audio` kanalı, `preserve_speech` tarafından korunan ve `speech` çıktısının ayırdığı diyaloğu belirler; böyle bir kanal yoksa diyalog videonun kendi ses bandından gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Klip için ses efektleri miksı; `preserve_speech` açık olduğunda diyalog bunun altına karıştırılmıştır. | AUDIO |
| `speech` | Ses bandından ayrılmış diyalog. Konuşma bulunamadığında veya konuşma ayırma bir sonuç döndürmediğinde, `audio` ile aynı örnekleme hızında sessizdir. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/tr.md)

---
**Source fingerprint (SHA-256):** `a6bd749a902d5ca2e91863fd6c4df57cdeba7fd9505026053b72b29d588587fa`
