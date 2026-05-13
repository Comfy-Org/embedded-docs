> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/tr.md)

TripoRetargetNode, önceden tanımlanmış animasyonları, hareket verilerini yeniden hedefleyerek 3D karakter modellerine uygular. Daha önce iskeletlenmiş bir 3D modeli alır ve birkaç hazır animasyondan birini uygulayarak çıktı olarak animasyonlu bir 3D model dosyası oluşturur. Düğüm, animasyon yeniden hedefleme işlemini gerçekleştirmek için Tripo API'si ile iletişim kurar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | Evet | - | Animasyon uygulanacak, daha önce işlenmiş iskeletli 3D modelin görev kimliği |
| `animation` | STRING | Evet | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" | 3D modele uygulanacak animasyon ön ayarı. Seçenekler arasında insansı animasyonlar (bekleme, yürüme, koşma, dalış, tırmanma, zıplama, kesme, ateş etme, yaralanma, düşme, dönme) ve yaratık animasyonları (dört ayaklı yürüme, altı ayaklı yürüme, sekiz ayaklı yürüme, yılan gibi sürünme, suda yürüme) bulunur. |
| `auth_token_comfy_org` | AUTH_TOKEN_COMFY_ORG | Hayır | - | Comfy.org API erişimi için kimlik doğrulama belirteci (gizli parametre) |
| `api_key_comfy_org` | API_KEY_COMFY_ORG | Hayır | - | Comfy.org hizmet erişimi için API anahtarı (gizli parametre) |
| `unique_id` | UNIQUE_ID | Hayır | - | İşlemi izlemek için benzersiz tanımlayıcı (gizli parametre) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan animasyonlu 3D model dosyası (yalnızca geriye dönük uyumluluk için) |
| `retarget task_id` | RETARGET_TASK_ID | Yeniden hedefleme işlemini izlemek için görev kimliği |
| `GLB` | FILE3DGLB | GLB formatında animasyonlu 3D model |

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
