# Module Video Generation IDs
## Use these to check status and download when complete

| Module | Notebook ID | Task ID |
|--------|------------|---------|
| 1 | 56edbd6f-a851-401d-aa94-9c08eb2e0f23 | b01f21c7-b487-42a1-9978-0b080c420d20 |
| 2 | b0122d79-ba5b-4462-bdf3-589cbeeb92af | 556e19d6-8292-47bd-85e6-b56f2e8c2a05 |
| 3 | 7cb7ded6-0966-4848-9002-4087396f454d | 653757fb-7482-4588-9148-950ceec31df0 |
| 4 | aea8b065-b716-4792-aaa0-c962c3abe80f | 6e64f5eb-4cf3-4b0d-9a79-06e060079ff4 |
| 5 | 082f6e34-7d9b-4957-9a16-dfe25e18cceb | fa529f07-77bb-4499-98cb-7be29dbf653e |
| 6 | 29db2e65-09ae-4b0a-a7b0-ffb0eaf57755 | 16dc2c42-cd91-4700-bae3-ff6697475c8a |
| 7 | 6ee1a149-a7b0-439e-858c-de20e1ca308b | 6cdee0bc-9bd5-4153-8ac8-cf4bed1a1ab5 |
| 8 | 18d35eb7-5787-443b-8ed3-215c1b405762 | 273f1b33-b9a6-4825-b44c-4ac996b3b46d |
| 9 | 8cc0d7e0-5ca9-41cd-8c58-c1df10bd032a | a625b7e7-4e20-4c8c-9b8e-822cf751896e |
| 10 | 9eacd9b8-2ced-4bc1-8ef0-db3b5288df5c | 89ff1dc8-0d5b-457c-a43a-716e8251d819 |

## To check status:
```bash
python -m notebooklm artifact list --notebook [notebook_id] --json
```

## To download when complete:
```bash
python -m notebooklm download video "e:/Smart-Vault-Ai/output/course-assets/module-XX-video.mp4" -n [notebook_id]
```
