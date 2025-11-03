> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/tr.md)

`CLIP Text Encode (CLIPTextEncode)`, yaratıcı metin açıklamalarınızı AI'nın anlayabileceği özel bir "dile" dönüştüren, AI'nın ne tür bir görsel oluşturmak istediğinizi doğru bir şekilde yorumlamasına yardımcı olan bir çevirmen gibi davranır.

Yabancı bir sanatçıyla iletişim kurduğunuzu hayal edin - istediğiniz sanat eserini doğru bir şekilde iletmek için bir çevirmene ihtiyacınız vardır. Bu düğüm, metin açıklamalarınızı anlamak ve onları AI sanat modelinin anlayabileceği "talimatlara" dönüştürmek için CLIP modelini (çok sayıda görsel-metin çifti üzerinde eğitilmiş bir AI modeli) kullanan o çevirmenin rolünü üstlenir.

## Girdiler

| Parametre | Veri Türü | Girdi Yöntemi | Varsayılan | Aralık | Açıklama |
|-----------|-----------|--------------|---------|--------|-------------|
| text | STRING | Metin Girdisi | Boş | Herhangi bir metin | Bir sanatçıya verilen detaylı talimatlar gibi, görsel açıklamanızı buraya girin. Detaylı açıklamalar için çok satırlı metinleri destekler. |
| clip | CLIP | Model Seçimi | Yok | Yüklenen CLIP modelleri | Belirli bir çevirmen seçmek gibi, farklı CLIP modelleri, sanatsal stilleri biraz farklı şekilde anlayan farklı çevirmenler gibidir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| CONDITIONING | CONDITIONING | Bunlar, AI modelinin anlayabileceği detaylı yaratıcı rehberliği içeren, çevrilmiş "resim yapma talimatlarıdır". Bu talimatlar, AI modeline açıklamanıza uygun bir görseli nasıl oluşturacağını söyler. |

## Kullanım İpuçları

1. **Temel Metin İstemi Kullanımı**
   - Kısa bir deneme yazıyormuş gibi detaylı açıklamalar yazın
   - Daha spesifik açıklamalar, daha doğru sonuçlara yol açar
   - Farklı betimleyici öğeleri ayırmak için İngilizce virgüller kullanın

2. **Özel Özellik: Gömme Modellerini Kullanma**
   - Gömme modelleri, belirli sanatsal efektleri hızlıca uygulayabilen önceden ayarlanmış sanat stili paketleri gibidir
   - Şu anda .safetensors, .pt ve .bin dosya formatlarını destekler ve tam model adını kullanmanız gerekli değildir
   - Nasıl kullanılır:
     1. Gömme model dosyasını (.pt formatında) `ComfyUI/models/embeddings` klasörüne yerleştirin
     2. Metninizde `embedding:model_adi` kullanın
     Örnek: `EasyNegative.pt` adında bir modeliniz varsa, şu şekilde kullanabilirsiniz:

     ```
     a beautiful landscape, embedding:EasyNegative, high quality
     ```

3. **İstemi Ağırlık Ayarlama**
   - Belirli açıklamaların önemini ayarlamak için parantez kullanın
   - Örneğin: `(beautiful:1.2)` "güzel" özelliğini daha belirgin hale getirecektir
   - Normal parantezler `()` varsayılan olarak 1.1 ağırlığa sahiptir
   - Ağırlıkları hızlıca ayarlamak için klavye kısayollarını `ctrl + yukarı/aşağı ok` kullanın
   - Ağırlık ayarlama adım boyutu ayarlardan değiştirilebilir

4. **Önemli Notlar**
   - CLIP modelinin düzgün şekilde yüklendiğinden emin olun
   - Olumlu ve net metin açıklamaları kullanın
   - Gömme modellerini kullanırken, dosya adının doğru olduğundan ve mevcut ana modelinizin mimarisiyle uyumlu olduğundan emin olun