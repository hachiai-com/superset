APP_NAME = "My Portal"
APP_ICON = "/static/assets/images/hachiaiLogo.png"
LOGO_TARGET_PATH = "/"
LOGO_TOOLTIP = "My Portal"
# Override favicon to match custom branding
FAVICONS = [{"href": "/static/assets/images/favicon.png"}]

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