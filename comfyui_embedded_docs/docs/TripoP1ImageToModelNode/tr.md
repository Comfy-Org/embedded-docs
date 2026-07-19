# Tripo P1: Görüntüden Modele

## Genel Bakış

Bu düğüm, Tripo P1 API'sini kullanarak tek bir 2D görüntüyü 3D modele dönüştürür. Düşük poligonlu, oyunlara hazır ağlar (mesh) oluşturmak için optimize edilmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | 3D modele dönüştürülecek giriş görüntüsü. | IMAGE | Evet | - |
| `çıktı_modu` | Çıktı modunu ve kalite ayarlarını belirten bir sözlük. Bu parametre, oluşturulan modelin türünü ve doku kalitesini kontrol eder. Mevcut seçenekler `_build_p1_output_mode` yardımcı fonksiyonu tarafından tanımlanır ve `texture_quality` ("standard", "high", "ultra" gibi) ile `image_alignment` ayarlarını içerir. | DICT | Evet | Açıklamaya bakın |
| `görüntü_oto_düzeltme_aktif` | Daha iyi üretim kalitesi için giriş görüntüsünü ön işleme tabi tutar. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `yüz_sınırı` | Oluşturulan ağdaki yüz sayısını sınırlar. -1 değeri sınırlama olmadığı anlamına gelir. (varsayılan: -1) | INT | Hayır | - |
| `model_tohumu` | Tekrarlanabilir model üretimi için tohum değeri. Sağlanmazsa rastgele bir tohum kullanılır. (varsayılan: None) | INT | Hayır | - |
| `oto_boyut` | Oluşturulan model için en uygun boyutu otomatik olarak belirler. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `uv_dışa_aktar` | Modelle birlikte UV koordinatlarını dışa aktarır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `geometriyi_sıkıştır` | Dosya boyutunu küçültmek için geometri verilerini sıkıştırır. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_dosyası` | Oluşturulan 3D modelin dosya yolu. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `model_task_id` | Model oluşturma isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3D model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
