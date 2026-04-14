"""
Smart Vault Co. — Google Drive Bulk Downloader
Pulls all shared files from Google Drive folders and saves locally.
Uses gdown for public links, falls back to Drive API for authenticated access.
"""
import os
import sys
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# All folder IDs from CJ's shared Drive
FOLDERS = {
    "Smart-Vault": "1ttlmum6zAHbWj_FsNyfVLCUBPtwDz4nr",
    "Smart-Vault-KB": "1eB17ZIbMf0VMkfMlOYDnPqhKX3-ca3bN",
    "Book-PDFs": "1WHyvDAttKuFWYooNjYrssdYeAkHvK1oU",
    "AI-100-Income-Streams": "1PZRP_wBXLptC4VEsu_-nb4v-n8v1xvGD",
    "AI-Automation": "1y3ynEOSFwBIvbzoFDXqKGjjcANbRk6x3",
    "Master-Project-Folder": "1jLVS7SsYK3BOUGUxwMmkbi_pK4KnqhHJ",
    "KTL-Media-PDFs": "10lRH0QygdAvEK1h2Bt66H8EU61qcvqLC",
    "Sheneil-Baez-Launch": "19w0EpUXKG7gaq2uWf5OVQXoz82t1tpkA",
    "Sir-AI-Tutor": "1F7pAA2EBVwjF5EQ3jcMmKY4DiJmlBAn5",
    "Google-AI-Studio": "1sN4FzHdFTNYqYynxiv0nl-yunuo8sta7",
    "Vaultron-Game-Studio": "1Ilvk_C6oidkcWdnsok1yB-JWhC6UnMLO",
    "House-Of-Peace": "1CG4YujyNZhuAUx_hClYlDn0bfD4oZP-k",
    "Bro-Panic-Lectures": "1Y2Z1OGU3dmJxxLhXKFz4d46PSc4TGVTk",
    "Spiritual-Operating-System": "1ypZ-tDC-6dw7beIKWZ4L7TVs4rqYJZ1A",
}

# Individual Google Docs to download as text
DOCS = {
    "comprehensive-automation-plan.txt": "1Qb0UnPMqchPVBoqE5LLnT0PBiYCUQF2l45gmeQ8y9ac",
    "war-room-blueprint.txt": "1UAh3N9DPerj01AxmrAIVbD9MN3YlyYKs0OJTpPYcjpg",
    "4-week-launch-plan.txt": "1k-bwrk_vvvkIoTBJ4h-yqA5eO_OUA6H6mMWqSv19lPo",
    "key-research-insights.txt": "1_vZQIcw844qI54yTH6GzcbKwojch77c1tFQJvXeNbU4",
    "cmo-agent-api.txt": "1ulrlvLOozciMyVFu4oygZWsApJ8eFs4_Hm1wXk8234g",
    "bob-iger-ip-strategy.txt": "1mHkcsA6io-vnz_BkRKPgq28G8NbBeeCvDDJZ5F5MrV0",
    "sbtlc-ai-agent-guide.txt": "1fhE7amwqMBVOB5-LTQ74x90pUCecBivDVNk0PtHA9XQ",
    "content-strategy-pain-points.txt": "17lwqNza126hF94P0ushTDEZrU9cd0NTlQWqM9rMdOm0",
    "sop-005-sales-consult.txt": "1S25QOPRHijUUsyAMgT047ArU45Bh-AGFoYWzmYE4FXg",
    "sop-007-analytics-utm.txt": "1yr5H2DCmLkXBLpGrdTgelAOBd7MbZQH6cs3PlRF5P9w",
    "sop-008-asset-library.txt": "1GZ6jIMPOlU-Ce9w_bhxqHvvWP-T4pJoIP4jBl7gPNtA",
    "sop-010-make-zapier.txt": "1ANbEhK1KomI_l9GcFI2RaWUIi-HzEUI751RqZ7USRRM",
    "sop-011-package-license.txt": "1I_-jkAbvDJ3MZOGVnzxYFjouI3nkWfaJoS9NNv5z3Bw",
    "dropshipping-strategy-2025.txt": "1HsUMiviWNa_ridhFfcbxMgOe8Ghz37MjE2rKRGj9--M",
    "cmo-ai-agent.txt": "1jJM8jFkn2EjNSzrw7awUVnRrflKTYFwmcOzlM41qQPk",
    "client-folder-structure-sheneil.txt": "13zLP3D-egEOJnnM5WsujexQc_Zl5nROfKIoN0dOAPLw",
    "master-project-setup.txt": "1J23Mxs8iuJiVK-vnj9K3aGC9bLzCjIz1s5a1qvhSngM",
    "chakra-course-kb.txt": "1DNTB8JXapvaZtnARL8818NwNHSJ7LG-RqTPLLtFjl8E",
    "cybersecurity-module4.txt": "1i1i_eU7pNuQrr_D1iucB_UE_VLVQ0BYBKMnPFBrdXno",
    "comprehensive-automation-plan-v2.txt": "1Qb0UnPMqchPVBoqE5LLnT0PBiYCUQF2l45gmeQ8y9ac",
    "conflict-policy.txt": "1M05mKo4KUeHFvAm8TuAZsmdjW8ekXUdr7Dq9SDJs1Qw",
}

BASE = "f:/Smart-Vault-Ai/KB/drive-dump"

def download_folder(name, folder_id):
    dest = os.path.join(BASE, name)
    os.makedirs(dest, exist_ok=True)
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    print(f"\n[FOLDER] {name}")
    print(f"  URL: {url}")
    try:
        import gdown
        gdown.download_folder(url, output=dest, quiet=False, use_cookies=False)
        count = len([f for f in os.listdir(dest) if not f.startswith('.')])
        print(f"  OK: {count} files downloaded to {dest}")
    except Exception as e:
        print(f"  FAIL: {e}")
        print(f"  -> Manual: download ZIP from {url}")

def download_doc(filename, doc_id):
    dest = os.path.join(BASE, "docs")
    os.makedirs(dest, exist_ok=True)
    filepath = os.path.join(dest, filename)
    if os.path.exists(filepath):
        print(f"  SKIP (exists): {filename}")
        return
    url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    print(f"  Downloading: {filename}")
    try:
        import gdown
        gdown.download(url, filepath, quiet=True, fuzzy=False)
        size = os.path.getsize(filepath) if os.path.exists(filepath) else 0
        if size > 100:
            print(f"  OK: {filename} ({size} bytes)")
        else:
            print(f"  FAIL: too small ({size} bytes) - may need public access")
            os.remove(filepath) if os.path.exists(filepath) else None
    except Exception as e:
        print(f"  FAIL: {e}")

def main():
    os.makedirs(BASE, exist_ok=True)

    print("=" * 60)
    print("Smart Vault Co. - Google Drive Bulk Downloader")
    print(f"Downloading to: {BASE}")
    print("=" * 60)

    print(f"\n--- Downloading {len(FOLDERS)} folders ---")
    for name, fid in FOLDERS.items():
        download_folder(name, fid)

    print(f"\n--- Downloading {len(DOCS)} individual docs ---")
    for filename, did in DOCS.items():
        download_doc(filename, did)

    print("\n" + "=" * 60)
    print("DONE!")
    total = 0
    for root, dirs, files in os.walk(BASE):
        total += len(files)
    print(f"Total files downloaded: {total}")
    print(f"Location: {BASE}")
    print("=" * 60)

if __name__ == "__main__":
    main()
