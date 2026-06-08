TripoRetargetNode, önceden tanımlanmış animasyonları, hareket verilerini yeniden hedefleyerek 3D karakter modellerine uygular. Daha önce iskeletlenmiş bir 3D modeli alır ve birkaç hazır animasyondan birini uygulayarak çıktı olarak animasyonlu bir 3D model dosyası oluşturur. Düğüm, animasyon yeniden hedefleme işlemini gerçekleştirmek için Tripo API'si ile iletişim kurar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `orijinal_model_görev_id` | Animasyon uygulanacak, daha önce işlenmiş iskeletli 3D modelin görev kimliği | RIG_TASK_ID | Evet | - |
| `animasyon` | 3D modele uygulanacak animasyon ön ayarı. Seçenekler arasında insansı animasyonlar (bekleme, yürüme, koşma, dalış, tırmanma, zıplama, kesme, ateş etme, yaralanma, düşme, dönme) ve yaratık animasyonları (dört ayaklı yürüme, altı ayaklı yürüme, sekiz ayaklı yürüme, yılan gibi sürünme, suda yürüme) bulunur. | STRING | Evet | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" |
| `auth_token_comfy_org` | Comfy.org API erişimi için kimlik doğrulama belirteci (gizli parametre) | AUTH_TOKEN_COMFY_ORG | Hayır | - |
| `api_key_comfy_org` | Comfy.org hizmet erişimi için API anahtarı (gizli parametre) | API_KEY_COMFY_ORG | Hayır | - |
| `unique_id` | İşlemi izlemek için benzersiz tanımlayıcı (gizli parametre) | UNIQUE_ID | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `yeniden hedefleme task_id` | Oluşturulan animasyonlu 3D model dosyası (yalnızca geriye dönük uyumluluk için) | STRING |
| `GLB` | Yeniden hedefleme işlemini izlemek için görev kimliği | RETARGET_TASK_ID |
| `GLB` | GLB formatında animasyonlu 3D model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/tr.md)

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
