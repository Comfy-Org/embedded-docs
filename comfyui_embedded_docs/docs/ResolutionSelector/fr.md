# Sélecteur de résolution

Le nœud Resolution Selector calcule la largeur et la hauteur en pixels en fonction d'un rapport d'aspect choisi et d'une résolution totale cible en mégapixels. Il est utile pour générer des dimensions cohérentes pour d'autres nœuds, tels que le nœud Empty Latent Image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `ratio d'aspect` | Le rapport d'aspect pour les dimensions de sortie (par défaut : `"1:1 (Square)"`). | COMBO | Oui | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `mégapixels` | Mégapixels totaux cibles. 1.0 MP ≈ 1024x1024 pour un carré (par défaut : 1.0). | FLOAT | Oui | 0.1 - 16.0 (pas : 0.01) |
| `aperçu` | Aperçu en direct de la résolution de sortie calculée. Ce widget en lecture seule se met à jour automatiquement et n'accepte aucune saisie utilisateur. | RESOLUTION_PREVIEW | Non | N/A |
| `multiple` | Multiple le plus proche du résultat pour définir la résolution sélectionnée (par défaut : 8). | INT | Non | 8 - 128 (pas : 4) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `width` | Largeur calculée en pixels multipliée par le multiple sélectionné. | INT |
| `height` | Hauteur calculée en pixels multipliée par le multiple sélectionné. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/fr.md)

---
**Source fingerprint (SHA-256):** `d97624227fa02cd2e2f9bdecb3443f9877402092dcee8c45b721a83739454e18`
