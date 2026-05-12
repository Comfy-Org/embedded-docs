> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI **Topaz Video Enhance V2** :

# Topaz Video Enhance V2

Le nœud **Topaz Video Enhance V2** vous permet de suréchantillonner et d'améliorer une vidéo à l'aide des modèles d'IA de Topaz Labs. Il peut augmenter la résolution, ajuster la fréquence d'images par interpolation et appliquer des améliorations créatives ou réalistes pour redonner vie à vos séquences vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `video` | VIDEO | Oui | - | La vidéo d'entrée à traiter. Doit être au format conteneur MP4. |
| `upscaler_model` | COMBO | Oui | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` | Le modèle d'IA utilisé pour le suréchantillonnage de la vidéo. La sélection de "Disabled" signifie qu'aucun suréchantillonnage ne sera appliqué. |
| `upscaler_model.upscaler_resolution` | COMBO | Conditionnel | `"FullHD (1080p)"`<br>`"4K (2160p)"` | La résolution de sortie cible pour le suréchantillonneur. Ce paramètre est requis lorsqu'un modèle de suréchantillonnage est sélectionné (pas "Disabled"). |
| `upscaler_model.creativity` | FLOAT | Conditionnel | 0,0 à 1,0 (pas 0,1) | Force créative du suréchantillonnage. Disponible uniquement pour les modèles "Astra 2" et "Starlight (Astra) Creative". Par défaut : 0,5 pour Astra 2, "low" pour Starlight Creative. |
| `upscaler_model.prompt` | STRING | Non | - | Invite de scène descriptive facultative (non instructive). Disponible uniquement pour le modèle "Astra 2". Limité à 500 images d'entrée (~15s à 30 ips) lorsqu'elle est définie. Par défaut : vide. |
| `upscaler_model.sharp` | FLOAT | Non | 0,0 à 1,0 (pas 0,01) | Netteté de pré-amélioration : 0,0=flou gaussien, 0,5=transparent (par défaut), 1,0=accentuation USM. Disponible uniquement pour le modèle "Astra 2". Par défaut : 0,5. |
| `upscaler_model.realism` | FLOAT | Non | 0,0 à 1,0 (pas 0,01) | Oriente la sortie vers un réalisme photographique. Laissez à 0 pour la valeur par défaut du modèle. Disponible uniquement pour le modèle "Astra 2". Par défaut : 0,0. |
| `interpolation_model` | COMBO | Oui | `"Disabled"`<br>`"apo-8"` | Le modèle d'IA utilisé pour l'interpolation d'images. La sélection de "Disabled" signifie qu'aucune interpolation ne sera appliquée. |
| `interpolation_model.interpolation_frame_rate` | INT | Conditionnel | 15 à 240 | Fréquence d'images de sortie. Requis lorsque le modèle d'interpolation est "apo-8". Par défaut : 60. |
| `interpolation_model.interpolation_slowmo` | INT | Non | 1 à 16 | Facteur de ralenti appliqué à la vidéo d'entrée. Par exemple, 2 rend la sortie deux fois plus lente et double la durée. Par défaut : 1. |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | Non | True/False | Analyser l'entrée pour détecter les images en double et les supprimer. Par défaut : False. |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | Non | 0,001 à 0,1 (pas 0,001) | Sensibilité de détection des images en double. Par défaut : 0,01. |
| `dynamic_compression_level` | COMBO | Non | `"Low"`<br>`"Mid"`<br>`"High"` | Niveau CQP pour la compression vidéo. Par défaut : "Low". |

**Contraintes importantes :**
- Au moins l'un des paramètres `upscaler_model` ou `interpolation_model` doit être activé (pas "Disabled"), sinon une erreur est générée.
- La vidéo d'entrée doit être au format conteneur MP4.
- Le modèle "Astra 2" avec une invite est limité à 500 images d'entrée (~15 secondes à 30 ips). Sans invite, il est limité à un nombre d'images plus élevé.
- Lorsque `upscaler_model` n'est pas "Disabled", le sous-paramètre `upscaler_resolution` est requis.
- Lorsque `interpolation_model` n'est pas "Disabled", le sous-paramètre `interpolation_frame_rate` est requis.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video` | VIDEO | La sortie vidéo améliorée après application des filtres de suréchantillonnage et/ou d'interpolation sélectionnés. |