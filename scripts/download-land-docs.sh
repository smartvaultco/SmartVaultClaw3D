#!/bin/bash
DEST='/mnt/f/Smart-Vault-Ai/KB/realestate/land-flipping-raw'
mkdir -p "$DEST"

download() {
  local NAME="$1"
  local ID="$2"
  local OUT="$DEST/$NAME"
  local CODE=$(curl -L "https://drive.google.com/uc?id=$ID&export=download" \
    -s -o "$OUT" -w '%{http_code}' \
    -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
    --max-time 30)
  local SIZE=$(stat -c%s "$OUT" 2>/dev/null || echo 0)
  if [ "$CODE" = "200" ] && [ "$SIZE" -gt 10000 ]; then
    echo "OK: $NAME ($SIZE bytes)"
  else
    echo "FAIL($CODE,$SIZE): $NAME"
    rm -f "$OUT"
  fi
}

download "6FBlueprint.pdf"                    "1qqpUeHMJC8mPycIV756Sas_md6OVAyfn"
download "67-ways-guide.pdf"                  "1LRA2d14XseC0v0Y1TfVM_Qhm6t9eG491"
download "affidavit.pdf"                      "1m6KFN8a07BVhxOUsmSfkuRdHpfNzlRKT"
download "Agent_Scripts_Cash_Buyers.pdf"      "1zkSpidGjkulhyKd5eOC-ACg29bZuUt5o"
download "Cash_Buyer_Scripts.pdf"             "1KwYiuo3KbISBr9I23wUtqD7lpV4NHojo"
download "Contractor_Agreement.pdf"           "1dHY_4SQKNWbJxss00iYcNONRmflz6V2Z"
download "creative-financing-hacks.pdf"       "1TDo0g8OijBw2LL5ApumuIWvwMOn92cVz"
download "Escalation-Addendum.pdf"            "1OZKpn--tFbFF_yJ3i0wFW9A1LfXtWHzI"
download "facebook-ad-hacks.pdf"              "1yzeC_Sj_S4OvUi6MH5AbfXS2GI6hzhkT"
download "flipping-notes-ebook.pdf"           "1ES0kvpkAYuuYxp0GcFAarrtp10BeX_g2"
download "funding_kit.pdf"                    "1EiZwFRYYbDSRLP2aoQOWltenJmdmnllM"
download "Guide_Flipping_Houses_IRA.pdf"      "1OExM8xWCRHoeRQp7Q3_x94iwNUtLnTqa"
download "INVESTOR_DISCLOSURE.pdf"            "1C8sArj6q_3lXr4hoWhmf4NWOX4HvVmzo"
download "InvestorHacks2023.pdf"              "1_IGWeqV7P2gQP3paD-szspTbUJsaWEPm"
download "jerry-norton-making-money-RE.pdf"   "1O6zTt3buYyDOcVLrXhV8mX-h1O-Ve6Ip"
download "Jerrys-Goals-workbook.pdf"          "17dT87z8FKZb4c6ICf-Obhq8MUo584osQ"
download "Make_Million_Flipping_Houses.pdf"   "1UNfMzooyJhgVD-gUQG9CvwODu-Z2USvm"
download "NDNCA.pdf"                          "1NCpk7TGai31X1-SNbZoMi_Tu5f5yjD_k"
download "Purchase-Agreement-Addendum.pdf"    "1kNuo0kxsgdEuE8vNx_ibftQiJtJ38qlI"
download "Purchase-Agreement-Termination.pdf" "1mr1JfQMYvDs_oiG1DAVFhFX5plB3Nsk0"
download "Real-Estate-SEO-Guide.pdf"          "1ZCE4X9lQ7e-383cssPr4Xn665EeJ2EcN"
download "SellerInstructions.pdf"             "1sjFyFxa0XFe0JMx7V9byYFDsPNBd9WlT"

echo ""
echo "Files in $DEST:"
ls -lh "$DEST"
