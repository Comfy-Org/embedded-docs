# Patina PBR Material Maps

Dérive un ensemble de cartes de matériau PBR à partir d'une image de texture existante : basecolor, normal, roughness, metalness et height. N'activez que les cartes dont vous avez besoin, car chaque carte activée augmente le coût. Utilisez-le pour compléter une texture qui n'a pas encore de cartes de matériau, ou pour reconstruire une seule carte défectueuse.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | La photographie ou le rendu à partir duquel dériver les cartes PBR. | IMAGE | Oui | - |
| `basecolor` | Générer la carte basecolor (albédo). Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `normal` | Générer la carte normale. Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `roughness` | Générer la carte de rugosité. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `metalness` | Générer la carte de métallicité. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `height` | Générer la carte de hauteur (déplacement). Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour un débruitage reproductible. Par défaut : 42. | INT | Oui | 0 à 2147483646 |
| `safety_checker` | Exécuter la vérification de sécurité du contenu du fournisseur sur la requête. Paramètre avancé. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `auto_downscale` | Réduire automatiquement l'échelle d'une image d'entrée dont le côté le plus long dépasse 2048 pixels, la limite d'entrée du modèle, en préservant le rapport hauteur/largeur ; les images plus petites sont laissées telles quelles. Désactivez-la pour générer une erreur sur les images surdimensionnées à la place. Paramètre avancé. Par défaut : True. | BOOLEAN | Non | true<br>false |

**Contraintes et comportement :**

* Au moins une carte doit être activée, sinon l'exécution échoue.
* L'image d'entrée est limitée à 2048 pixels sur son côté le plus long ; soit vous laissez `auto_downscale` la réduire, soit l'exécution échoue sur une image surdimensionnée.
* Chaque carte désactivée renvoie tout de même une sortie, mais sous forme d'une image de remplacement 1x1 ; ne connectez donc que les sorties que vous avez réellement générées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `basecolor` | La carte basecolor (albédo) générée, ou une image de remplacement 1x1 lorsque cette carte est désactivée. | IMAGE |
| `normal` | La carte normale générée, ou une image de remplacement 1x1 lorsque cette carte est désactivée. | IMAGE |
| `roughness` | La carte de rugosité générée, ou une image de remplacement 1x1 lorsque cette carte est désactivée. | IMAGE |
| `metalness` | La carte de métallicité générée, ou une image de remplacement 1x1 lorsque cette carte est désactivée. | IMAGE |
| `height` | La carte de hauteur (déplacement) générée, ou une image de remplacement 1x1 lorsque cette carte est désactivée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/fr.md)

---
**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`
