APP_NAME = "My Portal"
LOGO_TARGET_PATH = "/"
LOGO_TOOLTIP = "My Portal"

# ============================================================================
# PRODUCTION CONFIGURATION: External URL/CDN (Recommended)
# ============================================================================
# Upload your logo and favicon to a CDN, S3, or static file server, then
# replace the URLs below with your actual CDN URLs.
#
# Examples:
# - AWS S3: "https://your-bucket.s3.amazonaws.com/assets/hachiaiLogo.png"
# - Cloudflare CDN: "https://cdn.yourdomain.com/assets/hachiaiLogo.png"
# - GitHub Pages: "https://yourusername.github.io/assets/hachiaiLogo.png"
# - Any static host: "https://static.yourdomain.com/images/hachiaiLogo.png"
#
# IMPORTANT: Replace these placeholder URLs with your actual CDN URLs
# ============================================================================
APP_ICON = "https://your-cdn.com/assets/hachiaiLogo.png"  # REPLACE WITH YOUR CDN URL
FAVICON_URL = "https://your-cdn.com/assets/favicon.png"    # REPLACE WITH YOUR CDN URL

# Override favicon to match custom branding
FAVICONS = [{"href": FAVICON_URL}]

THEME_DEFAULT = {
    "token": {
        "brandLogoUrl": APP_ICON,
        "brandLogoAlt": "My Portal",
        "brandLogoHeight": "24px",  # adjust to your logo
    },
    "algorithm": "default",
}

THEME_DARK = {
    "token": {
        "brandLogoUrl": APP_ICON,
        "brandLogoAlt": "My Portal",
        "brandLogoHeight": "24px",
    },
    "algorithm": "dark",
}