> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/fr.md)

Voici la traduction en français de la documentation du nœud **Topaz Video Enhance V2**, en respectant toutes vos règles.

---

# Topaz Video Enhance V2

Le nœud **Topaz Video Enhance V2** permet de suréchantillonner et d'améliorer une vidéo à l'aide des modèles d'IA de Topaz Labs. Il peut augmenter la résolution, ajuster la fréquence d'images par interpolation et appliquer des améliorations créatives ou réalistes pour redonner vie à vos séquences vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `vidéo` | VIDEO | Oui | - | La vidéo d'entrée à traiter. Doit être au format conteneur MP4. |
| `modèle d’agrandissement` | COMBO | Oui | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` | Le modèle d'IA utilisé pour suréchantillonner la vidéo. La sélection de "Disabled" signifie qu'aucun suréchantillonnage ne sera appliqué. |
| `upscaler_model.upscaler_resolution` | COMBO | Conditionnel | `"FullHD (1080p)"`<br>`"4K (2160p)"` | La résolution de sortie cible pour le suréchantillonneur. Ce paramètre est requis lorsqu'un modèle de suréchantillonnage est sélectionné (autre que "Disabled"). |
| `upscaler_model.creativity` | FLOAT / COMBO | Conditionnel | Astra 2 : 0,0 à 1,0 (pas de 0,1)<br>Starlight Creative : `"low"`<br>`"middle"`<br>`"high"` | Force créative du suréchantillonnage. Disponible uniquement pour les modèles "Astra 2" et "Starlight (Astra) Creative". Pour Astra 2, il s'agit d'un curseur (par défaut : 0,5). Pour Starlight Creative, il s'agit d'une liste déroulante (par défaut : "low"). |
| `upscaler_model.prompt` | STRING | Non | - | Description facultative de la scène (descriptive, non impérative). Disponible uniquement pour le modèle "Astra 2". Limité à 500 images d'entrée (~15 s à 30 ips) lorsqu'il est défini. Par défaut : vide. |
| `upscaler_model.sharp` | FLOAT | Non | 0,0 à 1,0 (pas de 0,01) | Netteté de pré-amélioration : 0,0 = flou gaussien, 0,5 = passage direct (par défaut), 1,0 = accentuation USM. Disponible uniquement pour le modèle "Astra 2". Par défaut : 0,5. |
| `upscaler_model.realism` | FLOAT | Non | 0,0 à 1,0 (pas de 0,01) | Oriente la sortie vers un réalisme photographique. Laissez à 0 pour la valeur par défaut du modèle. Disponible uniquement pour le modèle "Astra 2". Par défaut : 0,0. |
| `modèle d’interpolation` | COMBO | Oui | `"Disabled"`<br>`"apo-8"` | Le modèle d'IA utilisé pour l'interpolation d'images. La sélection de "Disabled" signifie qu'aucune interpolation ne sera appliquée. |
| `interpolation_model.interpolation_frame_rate` | INT | Conditionnel | 15 à 240 | Fréquence d'images de sortie. Requis lorsque le modèle d'interpolation est "apo-8". Par défaut : 60. |
| `interpolation_model.interpolation_slowmo` | INT | Non | 1 à 16 | Facteur de ralenti appliqué à la vidéo d'entrée. Par exemple, 2 rend la sortie deux fois plus lente et double la durée. Par défaut : 1. |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | Non | True/False | Analyser l'entrée pour détecter les images en double et les supprimer. Par défaut : False. |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | Non | 0,001 à 0,1 (pas de 0,001) | Sensibilité de détection des images en double. Par défaut : 0,01. |
| `niveau de compression dynamique` | COMBO | Non | `"Low"`<br>`"Mid"`<br>`"High"` | Niveau CQP pour la compression vidéo. Par défaut : "Low". |

**Contraintes importantes :**
- Au moins l'un des paramètres `upscaler_model` ou `interpolation_model` doit être activé (autre que "Disabled"), sinon une erreur est générée.
- La vidéo d'entrée doit être au format conteneur MP4.
- Le modèle "Astra 2" avec un prompt est limité à 500 images d'entrée (~15 secondes à 30 ips). Sans prompt, il est limité à un nombre d'images plus élevé.
- Lorsque `upscaler_model` n'est pas "Disabled", le sous-paramètre `upscaler_resolution` est requis.
- Lorsque `interpolation_model` n'est pas "Disabled", le sous-paramètre `interpolation_frame_rate` est requis.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `vidéo` | VIDEO | La sortie vidéo améliorée après application des filtres de suréchantillonnage et/ou d'interpolation sélectionnés. |

---
**Source fingerprint (SHA-256):** `29b7538206327c35866126c1862c1d1ccea872ba84fbb9c84126114a06e2b00f`
