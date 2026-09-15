# Meshy: Modeli Canlandır

Bu düğüm, Meshy hizmetini kullanarak daha önce riglenmiş bir 3B karaktere belirli bir animasyon aksiyonu uygular. Daha önceki bir rigleme işleminden alınan görev kimliğini ve kitaplıktan istenen animasyonu seçmek için bir aksiyon kimliğini alır, ardından animasyonlu modeli hem GLB hem de FBX dosya biçimlerinde döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `rig_task_id` | Daha önce tamamlanmış bir Meshy karakter rigleme işleminden alınan benzersiz görev kimliği. | MESHY_RIGGED_TASK_ID | Evet | N/A |
| `action_id` | Uygulanacak animasyon aksiyonunun ID numarası. Kullanılabilir değerlerin listesi için https://docs.meshy.ai/en/api/animation-library adresini ziyaret edin. (varsayılan: 0) | INT | Evet | 0 - 696 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Animasyonlu model için bir dize tanımlayıcısı. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `GLB` | Animasyonlu 3B model dosyası GLB biçiminde. | FILE3DGLB |
| `FBX` | Animasyonlu 3B model dosyası FBX biçiminde. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`
