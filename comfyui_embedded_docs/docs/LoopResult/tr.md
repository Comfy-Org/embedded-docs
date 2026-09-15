# LoopResult

LoopResult, bir döngü bloğunun kapanış noktasını işaretleyen yalnızca geliştiriciler için çıktı düğümüdür. Kendisine sırayla aktarılan değerleri toplar (`output0`, `output1` vb. şeklinde adlandırılır) ve bir kapatma kimliği ile tanımlanan harici yürütme bloğunu serbest bırakır. Girdi parmak izleme her zaman NaN döndürdüğünden, düğüm her zaman değişmiş olarak değerlendirilir ve her çalıştırmada yeniden yürütülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `close_id` | Kapatılacak döngü bloğunun tanımlayıcısı; listenin yalnızca ilk değeri kullanılır | STRING | Evet | - |
| `output0`, `output1`, ... | Döngü bloğundan toplanan değerler. Düğüm herhangi bir ek girdiyi kabul eder ve bunları `output0` ile başlayarak sıralı düzende toplar, ilk eksik dizinde durur | Herhangi bir tür | Hayır | - |

Not: Bu düğüm tüm girdileri kabul eder (`accept_all_inputs`). `close_id` dışındaki herhangi bir girdi, toplanan bir döngü değeri olarak ele alınır ve sonuca dahil edilmesi için boşluk olmadan `output0`, `output1`, `output2` vb. şeklinde adlandırılmalıdır.

## Çıktılar

Bu düğüm herhangi bir çıktı döndürmez. Yalnızca `close_id` ile ilişkili harici yürütme bloğunu serbest bırakır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopResult/tr.md)

---
**Source fingerprint (SHA-256):** `637f8a39b0e99e8d4453cfc482463bd14d909b710264021ac2c27fdcd68b6063`
