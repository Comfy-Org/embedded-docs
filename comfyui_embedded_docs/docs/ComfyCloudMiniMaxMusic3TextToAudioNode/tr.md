# Comfy Cloud MiniMax Music 3 Metinden Sese [BETA]

MiniMax Music 3 iş akışını bir Comfy Cloud GPU üzerinde çalıştırır ve oluşturulan bir şarkı döndürür. İstem; stili, enstrümantasyonu ve ruh halini taşır; şarkı sözleri tarif edilmek yerine söylenir ve boş şarkı sözü parçayı enstrümantal bırakır. Bu bir beta düğümdür ve GPU saniyesi başına ücretlendirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Şarkının açıklaması: stil, enstrümantasyon ve ruh hali. Gönderimden önce baştaki ve sondaki boşluklar kaldırılır. | STRING | Evet | 1 ile 4096 karakter |
| `lyrics` | Söylenecek sözler. Enstrümantal için boş bırakın. | STRING | Hayır | 0 ile 4096 karakter |
| `seed` | Oluşturulan sonucu kontrol eden rastgele tohum (varsayılan: 42). | INT | Evet | 0 ile 9223372036854775807 |
| `max_duration` | Parçanın çalabileceği en uzun süre, saniye cinsinden (varsayılan: 120.0). Model şarkıyı daha erken bitirebilir. | FLOAT | Evet | 0.04 ile 360.0 arası (adım 0.04) |
| `audio_quality` | Çıktı bit hızı. `"V0"` değişken bit hızlıdır ve üç seçenek arasında en yüksek kalitedir (varsayılan: `"V0"`). | COMBO | Evet | `"V0"`<br>`"128k"`<br>`"320k"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | Oluşturulan şarkı. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxMusic3TextToAudioNode/tr.md)

---
**Source fingerprint (SHA-256):** `defc8d97071f2eaef4b00c6df721f4d10756e4867fefa22c1db7b8c3aafb6b7b`
